dlp-assignment1
===============

This contains the django project assigned in the training program.


Installation:
==============

Linux Debian:
------------
Assumptions: You have Python 2.7 (or above) installed:
    If you don't, run the command
        $ sudo apt-get install python

1. Check if you have `pip` installed, and install it if required
    1.1.Go to the console, and run the command
        $ pip
    1.2. If the output contains "Usage: pip COMMAND [OPTIONS] skip to step 2
    1.3. If the output contained "No command 'pip' found..."
        1.3.1. Run the command
            $ sudo apt-get install python-pip

2. Check if you have virtualenv, and installing if required
    Note: This step can be entirely skipped if you don't want to install
        the packages into a virtualenv. Skipping this step however installs
        the packages globally, and might overwrite some of your other packages

        Other installed packages contain south 0.8.4 and django 1.6.1

    2.1. Go to the console and run the command
        $ virtualenv

    2.2. If the output contains "You must provide a DEST_DIR" skip to
            step 2.4.

    2.3. If the output contains "No command 'virtualenv'..."
        2.3.1. Run the command
            $sudo apt-get install virtualenv

    2.4. Creating the virtual environment
        2.4.1. Create a virtual environment inside a custom folder
            $ virtualenv /path_to_custom_folder

    2.5. Activating the virtual environment
        $ source /path_to_custom_folder/bin/activate

        Say your virtual environment folder was ~/ve/DPL1_env, you should see
            your console prompt change, to include a (DPL1_env) at the
            beginning of the line. From now on, if you run the command
            `pip install`, every Python package should be installed in this
            custom folder. If the prompt doesn't change, check out the
            documentation for virtualenv http://www.virtualenv.org/en/latest/

3. Install the DPL1 packages from the Pypi.
    3.1. Run the command
        $ pip install dj-vga-w1

        This will install the package `dpl1_main` inside the
            site-packages folder of your python installation in the current
            python installation (inside the active virtual environment, if
             you have such an environment)

    3.2. Testing that the installation worked:
        3.2.1. Running the tests for the application
            $ django-admin.py test dpl1_main.testing_app
                    --settings=dpl1_main.DPL1.settings

        3.2.2. You should see "Creating test database for alias 'default'..."
                in the output. If this isn't the case,
        3.2.3. Run the command
            $ django-admin.py runserver --settings=DPL1.settings

        3.2.4. If the output contains "Validating models..." skip to step 4.

4. Deployment on apache2 with mod_wsgi
    Notice that in all the examples at step 3 the option --settings=... was
        used. You will have to provide that settings file for yourself, or
        customize the one given in order to change settings like the database
        connection engine.

    Also, the interaction between the apache server and the other components
        (for instance a database connector) is out of scope for this document.
    You will have to take care that the chosen server has the proper
        authorizations to work with the other systems.

    4.1. Making the app work with mysql:
        In dpl1_main.DPL1.settings, you have the `DATABASES` entry
            DATABASES = {
                'default': {
                    'ENGINE': 'django.db.backends.mysql',
                    'NAME': 'vwh_db',
                    'PORT': '3306',
                    'USER': 'root',
                    'PASSWORD': 'qwer',
                    'HOST': 'localhost'
                }
            }

        Notice the elements, because each one of them is important:
        'ENGINE' - the value is standard, it's standard django engine for Mysql
        'NAME' - the name of a schema that is hosted by the 'HOST'
        'PORT' - the port the instance database server is listening on
        'USER' - a valid user for the database, with rights
        'PASSWORD' - the password
        'HOST' - the address an IP address (or domain name) for the server
            hosting the database.



-This file is a copy of the old README.md file that could itself be added to
MANIFEST.in file

#TODO: deploying static files (.css)
    #TODO: make the admin site use the template I choose
#TODO: some redirect bug? sometimes clicking on the test returns the 'home' page
#TODO: unit tests with selenium to test the session wrappers
#TODO: hook up the site with some CSS magic