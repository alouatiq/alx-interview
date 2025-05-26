# 0x06. Star Wars API

## Description

This project involves interacting with the [Star Wars API (SWAPI)](https://swapi-api.alx-tools.com/) to fetch and display character names from a specific Star Wars movie. The goal is to make HTTP requests using Node.js and handle asynchronous responses properly.

The main task is to print all character names from a given movie ID, preserving the order in which they appear in the API response.

## Requirements

- Ubuntu 20.04 LTS
- Node.js version 10.14.x
- Code must be semistandard compliant (Standard + semicolons)
- The first line of every file should be `#!/usr/bin/node`
- Use of the `request` module is mandatory
- No use of `var` (only `const` and `let`)
- All files must be executable and end with a new line

## Installation

Install Node.js:

```bash
curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
sudo apt-get install -y nodejs
```

Install semistandard for linting:

```bash
sudo npm install semistandard --global
```

Install the request module globally:

```bash
sudo npm install request --global
export NODE_PATH=/usr/lib/node_modules
```

Usage
Run the script with a movie ID as the first argument:

```bash
./0-starwars_characters.js <Movie_ID>
```

Example:

```bash
./0-starwars_characters.js 3
```

Output:
```
python-repl
Luke Skywalker
C-3PO
R2-D2
...
```
