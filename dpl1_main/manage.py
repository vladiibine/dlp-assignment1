#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dpl1_main.DPL1.settings")

    #Vlad was here: manage.py should see the PYTHONPATH as django-admin.py
    #sees it, meaning it should see dpl1_main as the main package
    sys.path.remove(os.getcwd())
    sys.path.append(os.path.join('.', '..'))

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
