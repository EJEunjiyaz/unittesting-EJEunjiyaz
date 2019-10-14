[![Build Status](https://travis-ci.com/EJEunjiyaz/ unittesting-EJEunjiyaz-.svg?branch=master)](https://travis-ci.com/EJEunjiyaz/unittesting-EJEunjiyaz)

## Unit Testing Assignment

by Vichyawat Nakarugsa and Bill Gates.


## Test Cases for unique

Write a table describing your test cases.

| Test case              |  Expected Result    |
|------------------------|---------------------|
| empty list             |  empty list         |
| one item               |  list with 1 item   |
| one item many times    |  list with 1 item   |
| 2 items, many times, many orders | 2 item list, items in same order  |
| what other test case?  |  what result?       |
| string not list        |  list with string   |
| string not list many times | raises TypeError |
| integer not list one item | raises TypeError |
| float not list one item | raises TypeError   |
| all empty              | raises TypeError    |
| two list               | raises TypeError    |


## Test Cases for Fraction

| Test case              |  Expected Result    |
|------------------------|---------------------|
| string method          | string with proper fraction |
|                        |                     |
| add method             |                     |
| - integer + integer    | proper fraction     |
| - float + 0/1          | proper fraction     |
| - interger or float + 0/0 | raises ZeroDivisonError |
|                        |                     |
| equal method           |                     |
| - fraction             | boolean             |
| - 1/0, -1/0            | boolean             |
| - 0/0                  | raises ZeroDivisonError |
|                        |                     |
| multiply method        |                     |
| - fraction             | proper fraction     |
| - 0/1*0/1              | 0/1                 |
| - float fraction       | proper fraction     |
|                        |                     |
| substraction method    |                     |
| - fraction             | proper fraction     |
| - 1-1                  | 0/1                 |
|                        |                     |
| negative method        | negative fraction   |
|
| input string           | raises ValueError   |
| input many value       | raises TypeError    |