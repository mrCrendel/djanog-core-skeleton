from fabric.context_managers import cd, prefix
from fabric.operations import sudo, run
from fabric.state import env

PROJECT_ROOT = ''
VENV_DIR = ''


def update():
    env.host_string = ''
    env.user = ''
    env.password = ''
    with cd(PROJECT_ROOT):
        sudo('git pull origin master')
        with prefix('source ' + VENV_DIR + '/bin/activate'):
            with prefix('source env/.env.source'):
                    run('pip install -r requirements/prod.txt')
                    run('./manage.py collectstatic --noinput')
                    run('./manage.py migrate')
                    sudo('systemctl daemon-reload')
                    sudo('systemctl restart nine')
                    sudo('service nginx restart')

if __name__ == '__main__':
    update()
