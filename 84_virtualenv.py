# Virtual Environment: A tool to create isolated Python environments. 
# It solves the problem of dependencies and versioning.
# It allows you to work on a specific project without affecting the entire system.
# It is a folder that contains a Python installation for a specific version of Python, plus a number of additional packages.


'''
   # Steps to create a virtual environment:
      1. Install virtualenv: pip install virtualenv
      2. Create a virtual environment: virtualenv myprojectenv
      3. Activate the virtual environment: .\myprojectenv\Scripts\\activate.ps1
      4. Install packages: eg: pip install flask
      5. Deactivate the virtual environment: deactivate          { # To exit from the virtual environment }

   # Using venv module:
      1. python -m venv myprojectenv
      2. .\myprojectenv\Scripts\\activate.ps1
      3. pip install flask
      4. deactivate

   # Importing a package from a virtual environment:
      import flask
   
'''


import flask as fk
import numpy as np



#----------------------------------------------------------------------------------------------------------
# For MacOS/linux users: source myprojectenv/bin/activate
# For windows powershell users: .\myprojectenv\Scripts\activate.ps1
# https://stackoverflow.com/questions/18713086/virtualenv-wont-activate-on-windows