# -*- coding: utf-8 -*-
from __future__ import with_statement
from fabric.api import *
from fabric.context_managers import shell_env
import os
 
env.warn_only = True
pwd = '/deploy/treloso/treloso'
venv_bin = '/deploy/treloso/bin/'
python_bin = venv_bin + 'python'
pip_bin = venv_bin + 'pip'
 
 
@hosts('root@107.170.80.129')
def deploy():
    with cd(pwd):
        run('git pull')
 
    with cd(os.path.join(pwd, 'apps/core/static/core')):
        run('npm install')
        run('bower install')
        run('grunt deploy')
 
    with cd(pwd):
        with shell_env(DJANGO_SETTINGS_MODULE='treloso.settings_production'):
            run('{0} install -r requirements.txt'.format(pip_bin))
            run('{0} manage.py syncdb'.format(python_bin))
            run('{0} manage.py migrate'.format(python_bin))
            run('{0} manage.py collectstatic --noinput'.format(python_bin))
            run('supervisorctl restart treloso')