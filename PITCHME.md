# Unit Testing
# Python 


---

### Agenda

- Principles
- unittest
- nose2
- PyCharm tools

---

### Principles of Unit Tests

@fa[arrow-down]
+++

- Goal of testing is to produce high quality / correct software
- Who is an engineer? developer? tester?

+++

![](https://martinfowler.com/bliki/images/unitTest/sketch.png)

+++

- a unit as the smallest testable part of an application
- could be an entire module, but it is more commonly an individual function or procedure
- each test case is independent from the others

+++
- unit tests are low-level, focusing on a small part of the software system
- unit tests are usually written by the programmers themselves using their regular tools
- unit tests are expected to be significantly faster than other kinds of tests
- run unit tests after any change to the code


---
### Principles continued

@fa[arrow-down]
+++

- Each test unit must be fully independent. 
- Each test must be able to run alone, and also within the test suite, regardless of the order that they are called. 
- May have to load with a fresh dataset and may have to do some cleanup handled by setUp() and tearDown() methods.

+++

- The first step when you are debugging your code is to write a new test pinpointing the bug. 
- bug catching tests are among the most valuable pieces of code in your project.

+++

- A huge use of the testing code is as an introduction to new developers. running and reading the related testing code is often the best thing that they can do to start.

- Use long and descriptive names for testing functions.

---

### Unittest

`unittest` is the batteries-included test module in the Python standard library. Its API will be familiar to anyone who has used any of the JUnit/nUnit/etc..

@fa[arrow-down]
+++

Creating test cases is accomplished by subclassing `unittest.TestCase`.

+++

```python
import unittest

def add_one(x):
    return x + 1

class MyTest(unittest.TestCase):
    def test_add_one(self):
        self.assertEqual(add_one(3), 4)

```

---
### unittest Common Methods

```python
assertEqual(a, b)
assertNotEqual(a, b) 
assertTrue(x)	 
assertFalse(x)	 
assertIs(a, b)
assertIsNot(a, b)
assertIsNone(x)
assertIsNotNone(x)
assertIn(a, b)
assertNotIn(a, b)
assertIsInstance(a, b)
assertNotIsInstance(a, b)
```

---
### Nose2

Nose2 is an extention of unittest, providing a framework for plug-ins, test discovery and loading.

@fa[arrow-down]
+++
Getting started:
```shell
$ pip install nose2
```

+++
Run tests simply with
```shell
nose2
```

+++
This will find and run tests in all packages in the current working directory, and any sub-directories of the current working directory whose names start with ‘test’.

+++
To find tests, nose2 looks for modules whose names start with ‘test’. In those modules, nose2 will load tests from all unittest.TestCase subclasses, as well as functions whose names start with ‘test’.

---
### Code Demo

See webcrawler folder for a real project example

---

### References

https://martinfowler.com/bliki/UnitTest.html

https://en.wikipedia.org/wiki/Unit_testing

http://docs.python-guide.org/en/latest/writing/tests/

https://docs.python.org/2/library/unittest.html

https://nose2.readthedocs.io/en/latest/