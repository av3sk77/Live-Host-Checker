# Live-Host-Checker
Live Host Checker is a Python Script for Detection the Availability of Website to Check Website is live or Not. As well as you can get response is fast & reliable within Short Period of time. In this Script you have to Provide a Domain list to Check Exist or Not & Also You can get a Output of existing Domains in file.

## Requirement
You must be Install Python3 Version<br/>

## How To Work
### Help Menu
```bash
# python3 live-host-checker.py

usage: live-host-checker.py [-h] [-o OUT] -w WORDLIST

optional arguments:
  -h, --help   show this help message and exit
  -o OUT       Output File [Ex. -o "found.txt"]

Required Arguments:
  -w WORDLIST  Wordlist file Location [Ex. -w "/root/Desktop/domains.txt"]
```

### domains.txt
```bash
google.com
mail.google.com
yahoo.com
facebook.com
```

### Usage
#### Run Script
```bash
# python3 live-host-checker.py -w /root/Desktop/domains.txt
```
#### Get Output in File
```bash
# python3 live-host-checker.py -w /root/Desktop/domains.txt -o found.txt
```



