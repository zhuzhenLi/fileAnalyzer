# fileAnalyzer
This is the project assigned by Capital One

#### Author: Zhuzhen Li, McGill University
#### Date: 2019/10/02

## Desription:
This python project aims to automatically check and anaylze a code file's infomation during a developing process. It meets and exceeds all the user reqirments by implementing all the key fetures described following. Results will be printed clearly to user.

## Key Features:
    - The input file can be any file format
    - When a file passed in, check if it is valid or not first
    - Count the total number of valid lines (ignore empty lines)
    - Count the total number of comments
    - Count the number of single line comments
    - Count the number of block line comments
    - Count the number of comments blocks
    - Count total number of TODO tasks


## Design Decisions:
- To generalize the usage of this python script, it should be able to anylze any format input files. Due to the different comments symbol for different coding languages, I design the script to take four arguments in total: [testfile, "single line comment symbol", "block comments starting symbol", "block comments ending symbol"]
- If the user arguments did not meet above format, reminder of argument format will send to user
- Before open and analzing a file, this script checks if the file is valid, exit if not valid and report to user.
- The checkComment function return a list which contains all needed info about comments, which only read through the testfile once to get all results stored in list.
- An important variable called "block_start" indicate if this current line is the start of a block comments, acts as a signal variable.
- For future imporvment, this python script is designed in modularity, highly maintainable, and easy to understand by other developers.


## Running Procedure:
- `python checkComments.py testfile "single line comment symbol" "block comments starting symbol" "block comments ending symbol" `

(please notice that the 3 symbols need to be around by "")


## Example Test Result:
- ` python checkComments.py testfile1.txt "//" "/*" "*/" `
  -  Total # of lines: 54
  - Total # of comment lines: 33
  - Total # of single line comments: 6
  - Total # of comment lines within block comments: 27
  - Total # of block line comments: 2
  - Total # of TODO's : 1

- `python checkComments.py testfile2.txt "#" "'''" "'''" `
  - Total # of lines: 22
  - Total # of comment lines: 15
  - Total # of single line comments: 12
  - Total # of comment lines within block comments: 3
  - Total # of block line comments: 1
  - Total # of TODO's : 3



## Assumptions:
- All empty lines should not count
- Todo tasks description must followed by "TODO:"
- Single comments and block comments are mutually exclusive, adding them will result total comments lines
- Assume that the single line comment symbol is different from either block comment start symbol or block comment end symbol. If these three are the same, then all comeents are treated as single line comments.
- Block comment start symbol or block comment end symbol can be the same, refer the second example above


## Environrment Requirement:
- This is a python3 script
