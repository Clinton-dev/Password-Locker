# Password-Locker
### Table of Contents
* Description
* Technology Used
* Setup Instructions and Installation
* Behaviour Driven Development
* Copyright & Licence Info
* Authors Info

## Description

Simple Python App that creates new contacts with properties. Touches on Test Driven Development using unittest (Python test framework).

## Technologies Used

- Python3.8
- unittest (test framework)
- password_generator
- PyperClip

##### Setup Instructions and Installation

- Clone this repository to your computer. `git clone https://github.com/Clinton-dev/Password-Locker.git`
- Open terminal command line then navigate to the root folder `cd Contact-List`
- Run `./run.py`


## Behaviour Driven Development

1. Displays Intro Message to user
    - OUTPUT: "Hello Welcome to your contact list. What is your name?"
   - INPUT: "Samora"
   - OUTPUT: "Hello Samora. what would you like to do?"
2. Enter Short Code
   - INPUT: "cc"
   - INPUT: "first_name", "last_name", "phone-number", "email"
   - OUTPUT: "New Contact Samora Yommie created" - Create new contact by providing required properties
3. Enter Short Code
   - INPUT: "dc"
   - OUTPUT: "Enter the number you want to search for" - Prompts user to enter number to search for
   - OUTPUT: "Samora Yommie .....0712345678" - Displays existing contacts
4. Enter Short Code
   - INPUT: "fc"
   - INPUT: "0712345678" - Search by Phone Number
   - OUTPUT: "Phone number.......0712345678, Email address....... samora.y@adzumi.co.ke" - Returns contact if exists



### Copyright & Licence Info
MIT Copyright (c) 2022 Clinton Wambugu

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

### Author's Information
[Clinton-dev](https://github.com/Clinton-dev)
