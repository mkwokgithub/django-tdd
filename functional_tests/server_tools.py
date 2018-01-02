from fabric.api import run
from fabric.context_managers import settings

def _get_manage_dot_py(host):
    mystr = '~/sites/{}/virtualenv/bin/python3 ~/sites/{}/source/manage.py'
    return mystr.format(host,host)

def reset_database(host):
    manage_dot_py = _get_manage_dot_py(host)
    svr_string = 'ubuntu-mkwok@{}'
    flush_string = '{} flush --noinput'
    with settings(host_string=svr_string.format(host)):
        run(flush_string.format(manage_dot_py))
    
def create_session_on_server(host,email):
    manage_dot_py = _get_manage_dot_py(host)
    svr_string = 'ubuntu-mkwok@{}'
    create_sess_string = '{} create_session {}'
    with settings(host_string=svr_string.format(host)):
        session_key = run(create_sess_string.format(manage_dot_py, email))
        return session_key.strip()
            
    
            
