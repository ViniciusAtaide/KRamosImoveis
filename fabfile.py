# -*- coding: utf-8 -*-
from __future__ import with_statement
from fabric.api import *
from fabric.context_managers import shell_env
import os

env.warn_only = True
pwd = '/opt/myenv/KRamosImoveis'
pwdfront = '/opt/kramosfront/'
venv_bin = '/opt/myenv/bin'
python_bin = venv_bin + 'python'
pip_bin = venv_bin + 'pip'

@hosts('yuri@107.170.80.129:8080')
def deploy():
	with cd(pwd):
		run('sudo git pull')

	with cd(pwdfront):
		run('sudo git pull')
		run('sudo npm install')
		run('bower install')
		run('grunt build')
		run('cp -avr ./dist/ ' + os.path.join(pwd,'/static/kramosfront'))
		run('cp ./dist/index.html ' + os.path.join(pwd,'/templates/front/'))

	with cd(pwd):
		with shell_env(DJANGO_SETTINGS_MODULE='treloso.settings_production'):
			run('{0} install -r requeriments.txt'.format(pip_bin))
			run('{0} manage.py syncdb'.format(python_bin))
			run('{0} manage.py migrate'.format(python_bin))
			run('{0} manage.py collectstatic --noinput'.format(python_bin))
			run('{0} supervisorctl restart kleberci')