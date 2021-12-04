#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author:Nolan
# datetime:2021/12/4 17:10
# software: PyCharm
# Version: v0.1.1


import logging
import random
import gym

logger = logging.getLogger(__name__)

class EnvSubmarine:
    def __init__(self):
        # ---------init state and action--------- #
        self.Target = 35
        self.state = 0
        # self.static_obstacle = 12
        self.actions = [0, 1, 2, 3]  # define action space
        self.gamma = 0.8
        self.viewer = None
        # ---------state transition--------- #
        # The graph is 6*6, the agent must get the target.
        self.size = 6
        self.T = dict()
        for i in range(self.size, self.size * self.size):
            self.T[str(i) + '_0'] = i - 6  # States 向上

        for i in range(self.size * (self.size - 1)):
            self.T[str(i) + '_1'] = i + 6  # States 向下

        for i in range(1, self.size * self.size):
            if i % self.size == 0:
                continue
            self.T[str(i) + '_2'] = i - 1  # States 向左

        for i in range(self.size * self.size):
            if (i + 1) % self.size == 0:
                continue
            self.T[str(i) + '_3'] = i + 1  # States向右
        # ---------Coordinates for plotting---------#
        self.x = [150, 250, 350, 450, 550, 650] * 6
        self.y = [650] * 6 + [550] * 6 + [450] * 6 + [350] * 6 + [250] * 6 + [150] * 6

    def reset(self):
        pass

    def step(self, action):
        pass

    def reward(self):
        pass


    def render(self):
        pass