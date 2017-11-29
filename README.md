"# CSC440-Wiki-Project" 

##Project Setup Instructions

NOTE: These instructions are for Linux. Some of the commands may be different on other systems, consult the relevant application's documentation if this is the case.

1 . Install python 2.7 and virtualenv

2. Create a virtualenv with the command 'virtualenv (whatever you want)"

2b. Activate the virtual environment with the command ( from the home dir ) ". (virtual environment directory)/bin/activate"

3. Install requirements into virtualenv with provided requirements.txt. The command is:

python -m pip install -r (path to requirements.txt)

This must be done with the virtual environment activated, or it will not install the requirements to the correct directory

4. Install JetBrains Toolbox, and using this tool then install Pycharm Professional ( the Community version is not sufficient). You may need to request a student license for this step, using your NKU email.

5. Create a new project in PycharmProfessional, selecting Flask instead of Pure Python at the project creation screen.

6. Under File -> Settings -> Project -> Project Interpreter, select the virtual environment you just created. This should present as an option in the drop down menu, if it is not you may need to point Pycharm to the path of the python executable inside the virtual environment directory

7. Unzip the instructor-provided code into the project directory. The directory structure in the project should not include "wiki-master", just it's sub-dirs. They should go directly under your top level directory for the project.

8. Pycharm may ask to install requirements at this point, agree to this

9. In the file config.py, add 'import os' to top of file and change CONTENT_DIR to os.cwd()

10. The executable for this project is the python file riki, not the executable Pycharm created for you during project creation ( this will have the same name as your project ). To run wiki from inside Pycharm, first set the run configuration.

Select Run -> Edit Configurations, set "Script Path" to the path of riki, then add "web" to the parameters. This corresponds to running riki from the command-line with the "web" option.

Also, make sure the current working directory of this run configuration is the project directory

11. Run the script.

12. In the run box at the bottom of the screen, a web address will be displayed. Navigate to this in your browser to access wiki

{% if display_github %}
    <li><a href="https://github.com/{{ github_user }}/{{ github_repo }}
    /blob/{{ github_version }}{{ conf_py_path }}{{ pagename }}.rst">
    Show on GitHub</a></li>
{% endif %}