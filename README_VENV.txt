The purpose is to create a development enviroment that is consistent for everyone (just the both of us). So that we both know which library
each of us have, so that we won't get compiler error when importing moduels, etc... Update the pip install list so that I know which library
you've downloaded so that I can download it for myself as well.

pip install in virtual enviroment:
----------------------------------
pip install pymongo 
pip install dnspython

For Tensorflow and Setting Up Virtual Enviroment:
------------------------------------------------
1. Install Python 3.5 64bit version (must be 64bit version).
https://www.python.org/downloads/release/python-352/

2. cmd: py -3.5 -m pip install virtualenv

3. navigate to project folder

4. cmd: py -3.5 virtualenv venv
looks something like this: ..\Artificial-Intelligence-Hand-Writing> py -3.5 virtualenv venv

How To Use Virtual Environment:
-------------------------------
1. Go to project folder
looks something like this: ..\Artificial-Intelligence-Hand-Writing>

2. Type 'venv\Scripts\activate
looks something like this: ..\Artificial-Intelligence-Hand-Writing>venv\Scripts\activate

3. should look something like: (venv) C:\...

4. start developing in virtual enviroment type 'deactivate' to simply deactivate.

5. Note that you need to pip install everything again while in the virtual enviroment 
so, pip install tensorflow, pip install scipy, pip install panda, etc...