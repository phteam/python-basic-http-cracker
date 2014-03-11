python-basic-http-cracker
=========================

pybasichttpscan.py - Python Basic HTTP Cracker

Is a threaded pentesting scanner for basic HTTP authorization using dictionary attack. It is an attempt in which the script tries to log in with username and a password. Each time the script tries it uses a different word in the dictionary file.

A dictionary attack is a technique for defeating a cipher or authentication mechanism by trying to determine its decryption key or passphrase by trying hundreds or sometimes millions of likely possibilities, such as words in a dictionary.

In this tool, you have two dictionary files needed for arguments:

    A list of user dictionary
    A list of password dictionary

Basically you have 3 arguments. The host, user dictionary file and password dictionary file. Here's a a simple help on how to use this tool.

    :: [PH] Index Python HTTP Auth Scanner ::
          http://asianzines.blogspot.com
Usage:
python pybasichttpscan.py [URL] [userdict.txt] [passdict.txt]

Example: $ python pybasichttpscan.py http://192.168.1.1 user.txt pass.txt


It uses interactive text based while scanning so that you can view what username/password that is being check for authorization. For a quick experiment, I tried attacking my router's basic http authorization on my local area network and here's the result.

Check out: http://asianzines.blogspot.com/2014/03/pybasichttpscanpy-python-basic-http.html for more details.
