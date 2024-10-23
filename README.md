geoAlign

geoAlign Project

marcot branch added this

Installs: 
for orb.py install, 
pip install numpy
pip install opencv-python

for sortCords.py install,
pip install matplotlib
pip install shapely

-------------------------------------------------------------------------------------------------------------------

There are requirements for each of us to have accurate, synced dependencies for the project. 

Follow the instructions to get it working:

Remove any active local branches. To do this:
> git checkout main
> git branch -d <branch_name>

Pull main. To do this: 
> git pull

Now, delete any virtual environments you may have. 

Make sure you're in geoAlign root directory.
Next, create a new virtual environment. To do this:
> python -m venv env

run the virtual enviroment
> source env/bin/activate (Lily, for windows the command is different, and is as follows: > .\env\Scripts\activate)

Now, you must install the dependencies. To do so:
> pip install -r requirements.txt 

Note:
- If you name your virtual environment something different than env, please add the path to our .gitignore file. 
- Make sure you activate your local virtual environment every time you work on the project. 
- if you introduce new dependencies to the project, make sure to add them to the requirements file, and inform the group so they can install the dependency. 
          - to add dependencies to the requirement file, run the following command:
            > pip freeze > requirements.txt