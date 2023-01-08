**1. What is "serialization" when we are talking about web services?**
```
  a) The act of taking data stored in a program and formatting it so it can be sent across the network

  b) Sorting all the data stored in a tuple

  c) Making it so that dictionaries can maintain their keys in sorted order

  d) Marking each network packet so it can be put back into order on the receiving system
```
Answer is: _a) The act of taking data stored in a program and formatting it so it can be sent across the network_

**2. Which of the following are not commonly used serialization formats?**
```
  a) TCP

  b) HTTP

  c) Dictionaries

  d) XML

  e) JSON
```
Answer is: _a) TCP, b) HTTP and c) Dictionaries_

**3. In this XML, which are the "complex elements"?**
``` HTML
<people>
    <person>
       <name>Chuck</name>
       <phone>303 4456</phone>
    </person>
    <person>
       <name>Noah</name>
       <phone>622 7421</phone>
    </person>
</people>
```
```
  a) person

  b) phone

  c) people

  d) Noah

  e) name
```
Answer is: _a) person and c) people_

**4. In the following XML, which are attributes?**
```HTML
<person>
  <name>Chuck</name>
  <phone type="intl">
     +1 734 303 4456
  </phone>
  <email hide="yes" />
</person>
```
```
  a) email

  b) hide

  c) type

  d) person

  e) name
```
Answer is: _b) hide and c) type_

**5. In the following XML, which node is the parent node of node e?**
```HTML
<a>
  <b>X</b>
  <c>
    <d>Y</d>
    <e>Z</e>
  </c>
</a>
```
```
  a) e

  b) a

  c) c

  d) b
```
Answer is: _c) c_

**6. Looking at the following XML, what text value would we find at path "/a/c/e"**
```HTML
<a>
  <b>X</b>
  <c>
    <d>Y</d>
    <e>Z</e>
  </c>
</a>
```
```
  a) Z

  b) b

  c) a

  d) Y

  e) e
```
Answer is: _e) Z_

**7. What is the purpose of XML Schema?**
```
  1) To establish a contract as to what is valid XML

  2) A Python program to tranform XML files

  3) To transfer XML data reliably during network outages

  4) To compute SHA1 checksums on data to make sure it is not modified in transit
```
Answer is: _1) To establish a contract as to what is valid XML_

**8. For this XML Schema:**
```HTML
<xs:complexType name=”person”>
  <xs:sequence>
    <xs:element name="lastname" type="xs:string"/>
    <xs:element name="age" type="xs:integer"/>
    <xs:element name="dateborn" type="xs:date"/>
  </xs:sequence>
</xs:complexType>
```
**And this XML,**
```HTML
<person>
   <lastname>Severance</lastname>
   <Age>17</Age>
   <dateborn>2001-04-17</dateborn>
</person>
```
**Which tag is incorrect?**
```
  a) Age

  b) person

  c) lastname

  d) age

  e) dateborn
```
Answer is: _a) Age_

**9. What does the "Z" mean in this representation of a time:**
```
2002-05-30T09:30:10Z
```
```
  a) This time is in the UTC timezone

  b) The hours value is in the range 0-12

  c) The local timezone for this time is New Zealand

  d) This time is Daylight Savings Time
```
Answer is: _a) This time is in the UTC timezone_

**10. Which of the following dates is in ISO8601 format?**
```
a) 2002-May-30

b) 05/30/2002

c) 2002-05-30T09:30:10Z

d) May 30, 2002
```
Answer is: _c) 2002-05-30T09:30:10Z_
