import os
import re

from bottle import Bottle, request, response
from bottle import static_file

import jinja2

# set useful definitions
root_dir = os.path.dirname(__file__)
templates_dir = os.path.join(root_dir, 'templates')

# initialise jinja2 environment
JINJA_ENVIRONMENT = jinja2.Environment(loader=jinja2.FileSystemLoader(templates_dir),
                                       extensions=['jinja2.ext.autoescape'],
                                       autoescape=True)

bottle = Bottle()

def is64bits(user_agent=''):
    """Check whether the platform is 64-bits.

    :param user_agent: user_agent from HTTP header

    :returns:  return true if user_agent matchs regex
    """
    platform = ['x86_64', 'x86-64', 'Win64', 'x64;', 'amd64', 'AMD64',
                'WOW64', 'x64_64']

    if re.search('|'.join(platform), user_agent):
        return True
    return False

@bottle.route('/')
def get():

    template_values = {'filename' : 'VMware-Horizon-View-Client-x86-3.0.0-1887158.exe'}

    if is64bits(request.get_header('User-Agent')):
        template_values['filename'] = 'VMware-Horizon-View-Client-x86_64-3.0.0-1887158.exe'

    template = JINJA_ENVIRONMENT.get_template('download.html')

    return template.render(template_values)
