PySwitchy
Switch function for python.

Table of Contents
Overview
Features
Installation
Usage
Contributing
License
Overview
This project is a python library which allows developer to use simple switch statment in python. Python doesn't provide any switch statment like c, c++, java and other prograing languages. To over come this we can use this library which provides basic switch stament features.

The time complexity for adding cases is O(n) and for  calling a case, it's O(1) where n is the number of added cases. ThisThis package provides a simple way to switch between different cases.

Features
- Supports Python 2 and 3.
- no need to install other libraries.
- Lightweight, only depends on the built.
- provide efficient switch function for simple uses.
...
Installation

to install this package in pip is give bellow.

pip install PySwitchy

Usage

from PySwitchy import switchy

obj = switchy()
#to add cases pass the list containg cases
case = ['case1','case2','case3',....]
cases = obj.add_cases(case)
result =  obj.switch(cases, option) #where option is the choice
print(result)

Contributing

Any one can contribute to this by suggesting any improvement, mentioning bugs, issues etc 

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes and commit them (git commit -am 'Add new feature').
Push to the branch (git push origin feature-branch).
Submit a pull request.

License

This project is licensed under the MIT License - see the LICENSE file for details.