#!/usr/bin/env python2
import sys
sys.path.append('/home/randy/Projects/distPND')

from distutils.core import setup
from glob import glob

setup(
    name = 'BubbMan2',
    version = '1.0',
    description = 'A solo entry by pymike for PyWeek #8',
    author = 'pymike',
    maintainer = 'Tempel',
    maintainer_email = 'randy.heydon@clockworklab.net',
    url = 'http://www.pygame.org/project-BubbMan+2-1114-.html',
    packages = ['lib','retrogamelib'],
    package_data = {'retrogamelib': ['*.png']},
    data_files = [('data', glob('data/*'))],
    scripts = ['run_game.py'],
    license = 'GPL',
)