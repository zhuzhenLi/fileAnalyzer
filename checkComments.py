#! /usr/bin/python3

import sys, os
from os.path import splitext
import ntpath
import re

# check if file valid
def validFile(filename):
    fname,extension = splitext(filename)
    # if not valid
    if not extension or len(extension)==1: 
        print(filename, "does not have valid extention, please provide a valid file!")
        sys.exit(-1)

    if fname.startswith('.'):
        print(filename, "starts with . , please provide a valid file!")
        sys.exit(-1)


# return number of non-empty lines in total
def nonblank_lines(f):
    true_line = 0
    for l in f:
        line = l.strip() 
        if line:
            true_line = true_line+1
    return true_line


# get comment line info at once, always ignor empty line
def checkComment(file, comments_symbol):
    comment= [0]*4
    block_start = 0
    block_line = 0
    
    lines = open(file, "r")
    for line in lines:
        l_strip= line.strip()  
        
        # single line comment
        if comments_symbol[0] in l_strip:
            comment[1]= comment[1]+1 
        
        # block comment ends
        if comments_symbol[2] in l_strip and block_start==1 and comments_symbol[2] != comments_symbol[0]:
            if block_line != 1 :
                comment[3]=comment[3]+1
                comment[2]=comment[2]+block_line+1
            block_start = 0
            block_line = 0
        
        
        # block comment starts
        if comments_symbol[1] in line and block_start==0 and comments_symbol[1] != comments_symbol[0]:
            block_start = 1
            
        # cumulate valid block comment lines
        if block_start == 1 and l_strip:
            block_line = block_line +1
    

        
    lines.close()
    
    comment[0]=comment[1]+comment[2] # total comments = single comments + block comments
    return comment


# count number of pattern "TODO:" in file, case sensitive.
def checkTodo (f):
    todo_line = 0
    for l in f:
        line = l.strip()
        if "TODO:" in line:
            todo_line = todo_line+1
    return todo_line

# call above functions and print results to user
def main(file, symbol):
    
    # check if filename valid, exit if not
    head, tail = ntpath.split(file)
    validFile(tail)
    
    # get number of lines, ignore empty lines
    with open(file) as f_in:
         num_lines=nonblank_lines(f_in)
    f_in.close()
    print("Total # of lines:", num_lines)
    
    # get commend line info at once
    commentInfo = checkComment(file, symbol)
    print("Total # of comment lines:", commentInfo[0])
    print("Total # of single line comments:", commentInfo[1])
    print("Total # of comment lines within block comments:", commentInfo[2])
    print("Total # of block line comments:", commentInfo[3])
    
    # check todo, assume each TODO task must be represented by: "TODO" + ":"
    with open(file) as f_in:
         num_todo=checkTodo(f_in)  
    f_in.close()
    print("Total # of TODO's :", num_todo)



if __name__ == '__main__':
    
    if len(sys.argv) !=5:
        print("Incorrect arguments given, Arguments in format [filename, single line comment symbol, block comment starts symbol, block comment ends symbol] are needed! Please double check!")
        sys.exit(-1)
    else:
        file = sys.argv[1]
        comments_format = [str(sys.argv[2]), str(sys.argv[3]), str(sys.argv[4])]
        
    if not os.path.exists(file):
        print(file, "does not exist, please double check the name or path!")
        sys.exit(-1)
    else:
        main(file, comments_format)    
    
