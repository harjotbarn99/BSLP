# BSLP
BlackStone Launchpad at UB 

## setting up virtual environment
  open the cloned repo directory in command line/ terminal and use `pipenv install --dev`
  
   this will instrall all the dependencies required to run the project in a pip virtual environment
   
  use `pipenv shell` to activate the virtual environment and `deactivate` to deactivate it.
  
  
## setting up application
  use `python manage.py migrate` to set up database
  
  then create a super user to acces the admin site `python manage.py createsuperuser`
