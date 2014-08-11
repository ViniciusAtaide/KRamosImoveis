# -*- coding: utf-8 -*-
from __future__ import with_statement
from fabric.api import *
from fabric.context_managers import shell_env
import os

env.warn_only = True
pwd = '/opt/myenv/KRamosImoveis'
venv_bin = '/opt/myenv/bin/'
python_bin = venv_bin + 'python'
pip_bin = venv_bin + 'pip'


@hosts('root@107.170.80.129')
def deploy():
    with cd(pwd):
	run('git pull')

    with cd(os.path.join(pwd, 'static/')):
	run('npm install')
	run('bower install')
	run('grunt install')

    with cd(pwd):
	with shell_env(DJANGO_SETTINGS_MODULE='KRamosImoveis.settings_production'):
	    run('{0} install -r requirements.txt'.format(pip_bin))
	    run('{0} manage.py syncdb'.format(python_bin))
	    run('{0} manage.py migrate'.format(python_bin))
	    run('{0} manage.py collectstatis --noinput'.format(python_bin))
	    run('supervisorctl restart kramosimoveis')
