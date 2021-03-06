from fabric.api import run
from fabric.api import task
import bower
import bunyan
import dtrace
import grunt
import less
import nodemon
import yeoman


@task
def full():
    """
    Install all the tools available
    """
    bower.install()
    bunyan.install()
    dtrace.install()
    grunt.install()
    less.install()
    nodemon.install()
    yeoman.install()
