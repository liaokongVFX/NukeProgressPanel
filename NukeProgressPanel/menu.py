# -*- coding:utf-8 -*-
__date__ = '2017/5/23 17:41'
__author__ = 'liaokong'

import nuke
import ProgressPanel

dirs = os.path.dirname((os.path.abspath(__file__)))
sys.path.insert(0, dirs)

nuke.menu("Nuke").addMenu("pipeline").addCommand("progressPanel", "ProgressPanel.start()")
