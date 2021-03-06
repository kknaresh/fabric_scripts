from fabric.api import task
from fabric.api import run
from fabric.api import sudo
import bower
import bunyan
import grunt
import less
import nodemon
import tools
import yeoman


@task
def install1():
    """
    NodeJS from external package
    """
    run('echo prefix = ~/.node >> ~/.npmrc')
    run('echo export PATH="$PATH:$HOME/.node/bin" >> ~/.bashrc')
    sudo('apt-get install -y python-software-properties')
    sudo('apt-get install -y software-properties-common')
    sudo('add-apt-repository -y ppa:chris-lea/node.js')
    sudo('apt-get update')
    sudo('apt-get install -y nodejs')
    run('mkdir -p .node')


@task
def install():
    """
    NodeJS from external package
    """
    run('echo prefix = ~/.node >> ~/.npmrc')
    run('echo export PATH="$PATH:$HOME/.node/bin" >> ~/.bashrc')
    sudo('apt-get install -y build-essential')
    sudo('curl -sL https://deb.nodesource.com/setup | bash -')
    sudo('apt-get update')
    sudo('apt-get install -y nodejs')
    run('mkdir -p .node')


@task
def full():
    """
    Install NodeJS and tools
    """
    install()
    tools.full()
