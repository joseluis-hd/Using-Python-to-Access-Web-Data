**1. Which of the following Python data structures is most similar to the value returned in this line of Python:**
```Python
x = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
```
```
  1) dictionary

  2) regular expression

  3) list

  4) socket

  5) file handle
```
Answer is: _5) file handle_

**2: In this Python code, which line actually reads the data?**
```Python
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
```
```
  1) mysock.recv()

  2) socket.socket()

  3) mysock.close()

  4) mysock.connect()

  5) mysock.send()
```
Answer is: _1) mysock.recv()_

**3. Which of the following regular expressions would extract the URL from this line of HTML:**
```
<p>Please click <a href="http://www.dr-chuck.com">here</a></p>
```
```
  1) href="(.+)"

  2) href=".+"

  3) http://.*

  4) <.*>
```
Answer is: _1) href="(.+)"_

**4. In this Python code, which line is most like the open() call to read a file:**
```Python
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
```
```
  1) mysock.connect()

  2) import socket

  3) mysock.recv()

  4) mysock.send()

  5) socket.socket()
```
Answer is: _1) mysock.connect()_

**5. Which HTTP header tells the browser the kind of document that is being returned?**
```
  1) Content-Type:

  2) HTML-Document:

  3) ETag:

  4) Metadata:

  5) Document-Type:
```
Answer is: _1) Content-Type:_

**6. What should you check before scraping a web site?**
```
  1) That the web site allows scraping

  2) That the web site supports the HTTP GET command

  3) That the web site only has links within the same site

  4) That the web site returns HTML for all pages
```
Answer is: _1) That the web site allows scraping_

**7. What is the purpose of the BeautifulSoup Python library?**
```
  1) It allows a web site to choose an attractive skin

  2) It optimizes files that are retrieved many times

  3) It repairs and parses HTML to make it easier for a program to understand

  4) It animates web operations to make them more attractive

  5) It builds word clouds from web pages
```
Answer is: _3) It repairs and parses HTML to make it easier for a program to understand_

**8. What ends up in the "x" variable in the following code:**
```
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
x = soup('a')
```
```
  1) A list of all the anchor tags (<a..) in the HTML from the URL

  2) True if there were any anchor tags in the HTML from the URL

  3) All of the externally linked CSS files in the HTML from the URL

  4) All of the paragraphs of the HTML from the URL
```
Answer is: _1) A list of all the anchor tags (<a..) in the HTML from the URL_

**9. What is the most common Unicode encoding when moving data between systems?**
```
  1) UTF-64

  2) UTF-128

  3) UTF-32

  4) UTF-8

  5) UTF-16
```
Answer is: _4) UTF-8_

**10. What is the ASCII character that is associated with the decimal value 42?**
```
  1) !

  2) ^

  3) /

  4) *

  5) +
```
Answer is: 4) *

**11. What word does the following sequence of numbers represent in ASCII:**
```
108, 105, 110, 101
```
```
  1) line

  2) lost

  3) func

  4) ping

  5) tree
```
Answer is: _1) line_

**12. How are strings stored internally in Python 3?**
```
  1) EBCDIC

  2) Byte Code

  3) UTF-8

  4) Unicode

  5) ASCII
```
Answer is: _4) Unicode_

**13. When reading data across the network (i.e. from a URL) in Python 3, what method must be used to convert it to the internal format used by strings?**
```
  1) find()

  2) encode()

  3) decode()

  4) trim()

  5) upper()
```
Answer is: _3) decode()_
