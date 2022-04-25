# Password-Locker
### Table of Contents
* Description
* Technology Used
* Setup Instructions and Installation
* Behaviour Driven Development
* Copyright & Licence Info
* Authors Info

## Description

An amazing application that will help you in managing your numerous account details including your passwords and even generate new passwords for you. Test Driven Development approach using unittest (Python test framework) is used in the creation of the application.

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
   - OUTPUT: "Create an account - ca or login into an existing acc -lo?"
2. Enter Short Code
   - INPUT: "ca"
   - INPUT: "name", "password"
   - OUTPUT: "New Contact User test created"

3. Enter Short Code
   - INPUT: "lo"
   - INPUT: "name", "password"
   - OUTPUT: "login successful"

4. Displays Intro Message to user
   - OUTPUT: "Create a credential - cd, display existing credential -dc, delete credential- dl, search credential -fc?"
5. Enter Short Code
   - INPUT: "dc"
   - OUTPUT: "Enter the name of credential account you want to search for" - Prompts user to enter name to search for
   - OUTPUT: "twitter .....username: twitter_username" - Displays existing credentials
6. Enter Short Code
   - INPUT: "fc"
   - INPUT: "twitter" - Search by credential acc name
   - OUTPUT: "Name.......twitter, Username....... username, Email address....... user.@test.com, Password....... password," - Returns credential if exists



### Copyright & Licence Info
MIT Copyright (c) 2022 Clinton Wambugu

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

### Author's Information
[Clinton-dev](https://github.com/Clinton-dev)
