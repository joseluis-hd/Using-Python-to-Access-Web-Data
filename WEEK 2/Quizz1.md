Pregunta 1

**Which of the following regular expressions would extract 'uct.ac.za' from this string using re.findall?**
```
  From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
```
```
1) @\S+

2) @(\S+)

3) ..@\S+..

4) F.+:
```
Answer: 
2.
Pregunta 2
What will the '\$' regular expression match?

1 punto

A dollar sign


A new line at the end of a line


The beginning of a line


The end of a line


An empty line

3.
Pregunta 3
What would the following mean in a regular expression? [a-z0-9]

1 punto

Match a lowercase letter or a digit


Match any text that is surrounded by square braces


Match anything but a lowercase letter or digit


Match an entire line as long as it is lowercase letters or digits


Match any number of lowercase letters followed by any number of digits

4.
Pregunta 4
What is the type of the return value of the re.findall() method?

1 punto

A list of strings


A boolean


An integer


A string


A single character

5.
Pregunta 5
What is the "wild card" character in a regular expression (i.e., the character that matches any character)?

1 punto

?


$


.


+


*


^

6.
Pregunta 6
What is the difference between the "+" and "*" character in regular expressions?

1 punto

The "+" matches at least one character and the "*" matches zero or more characters


The "+" matches upper case characters and the "*" matches lowercase characters


The "+" matches the beginning of a line and the "*" matches the end of a line


The "+" matches the actual plus character and the "*" matches any character


The "+" indicates "start of extraction" and the "*" indicates the "end of extraction"

7.
Pregunta 7
What does the "[0-9]+" match in a regular expression?

1 punto

Any number of digits at the beginning of a line


Any mathematical expression


Zero or more digits


One or more digits


Several digits followed by a plus sign

8.
Pregunta 8
What does the following Python sequence print out?

231
x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)

1 punto

['From:']


:


['From: Using the :']


^F.+:



From:

9.
Pregunta 9
What character do you add to the "+" or "*" to indicate that the match is to be done in a non-greedy manner?

1 punto

?


$


**


\g


++


^

10.
Pregunta 10
Given the following line of text:

1
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
What would the regular expression '\S+?@\S+' match?

1 punto

From


marquard@uct


d@uct.ac.za


stephen.marquard@uct.ac.za


\@\

