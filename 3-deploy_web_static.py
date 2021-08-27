#!/usr/bin/python3
""""""
import os
from fabric.api import put, run, env
from fabric.contrib import files
from datetime import datetime


def do_deploy(archive_path):
    '''
    distributes an archive to your web servers, using the function do_deploy
    '''
