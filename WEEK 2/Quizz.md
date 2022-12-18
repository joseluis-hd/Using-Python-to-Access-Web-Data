**1. Which of the following best describes "Regular Expressions"?**
```
  1) A way to solve Algebra formulas for the unknown value
  
  2) The way Python handles and recovers from errors that would otherwise cause a traceback
  
  3) A small programming language unto itself
  
  4) A way to calculate mathematical values paying attention to operator precedence
```
Answer is:  _3) A small programming language unto itself_

**2. Which of the following regular expressions would extract 'uct.ac.za' from this string using re.findall?**
``` Python
  From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
```
```
1) @\S+

2) @(\S+)

3) ..@\S+..

4) F.+:
```
Answer is: _@(\S+)_

**3. What will the '\$' regular expression match?**
```
1) A dollar sign

2) A new line at the end of a line

3) The beginning of a line

4) The end of a line

5) An empty line
```
Answer is: _1) A dollar sign_

**4. What would the following mean in a regular expression? [a-z0-9]**
```
1) Match a lowercase letter or a digit

2) Match any text that is surrounded by square braces

3) Match anything but a lowercase letter or digit

4) Match an entire line as long as it is lowercase letters or digits

5) Match any number of lowercase letters followed by any number of digits
```
Answer is: _1) Match a lowercase letter or a digit_

**5. What is the type of the return value of the re.findall() method?**
```
1) A list of strings

2) A boolean

3) An integer

4) A string

5) A single character
```
Answer is: _1) A list of strings_

**6. What is the "wild card" character in a regular expression (i.e., the character that matches any character)?**
```
1) ?

2) $

3) .

4) +

5) *

6) ^
```
Answer is: _3) ._

**7. What is the difference between the "+" and "*" character in regular expressions?**
```
1) The "+" matches at least one character and the "*" matches zero or more characters

2) The "+" matches upper case characters and the "*" matches lowercase characters

3) The "+" matches the beginning of a line and the "*" matches the end of a line

4) The "+" matches the actual plus character and the "*" matches any character

5) The "+" indicates "start of extraction" and the "*" indicates the "end of extraction"
```
Answer is: _1) The "+" matches at least one character and the "*" matches zero or more characters_

**8. What does the "[0-9]+" match in a regular expression?**
```
1) Any number of digits at the beginning of a line

2) Any mathematical expression

3) Zero or more digits

4) One or more digits

5) Several digits followed by a plus sign
```
Answer is: _4) One or more digits_

**9. What does the following Python sequence print out?**
```Python
x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)
```
```
1) ['From:']

2) :

3) ['From: Using the :']

4) ^F.+:

5) From:
```
Answer is: _3) ['From: Using the :']_

**10. What character do you add to the "+" or "*" to indicate that the match is to be done in a non-greedy manner?**
```
1) ?

2) $

3) **

4) \g

5) ++

6) ^
```
Answer is: _1) ?_

11. Given the following line of text:
```Python
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
What would the regular expression '\S+?@\S+' match?
```
```
1) From

2) marquard@uct

3) d@uct.ac.za

4) stephen.marquard@uct.ac.za

5) \@\
```
Answer is: _4) stephen.marquard@uct.ac.za_
