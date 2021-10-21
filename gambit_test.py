# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 12:13:26 2021

THis will be used to manipulate the games using python once they are created in the application
(I think)

@author: ballanr
"""

import numpy as np
import nashpy as nash

#GAME1 (pure strategy game)
#A = np.array([[2,0],[4,2]]) # A is the row player
#B = np.array([[4,2],[2,0]]) # B is the column player
#game1 = nash.Game(A,B)
#game1
#
#
## Find the Nash Equilibrium with Support Enumeration
#equilibria = game1.support_enumeration()
#for eq in equilibria:
#    print(eq)
#############################################################################################
##GAME2
## Create the payoff matrix(mixed strategy game)
#A = np.array([[-4,8,1],[0,4,1],[0,1,0]]) # A is the row player
#B = np.array([[-4,8,1],[0,4,1],[1,0,1]]) # B is the column player
#game2 = nash.Game(A,B)
#game2
## Find the Nash Equilibrium with Support Enumeration
#equilibria = game2.support_enumeration()
#for eq in equilibria:
#    print(eq)
#      
## Calculate Utilities
##
#sigma_r = np.array([0,1,0])
#sigma_c = np.array([1,0,0])
#pd = nash.Game(A, B)
#print(pd[sigma_r, sigma_c])
#
##run game many times to watch convegence to equilibria if any.
#iterations = 100
#np.random.seed(0)
#play_counts = pd.fictitious_play(iterations=iterations)
#for row_play_count, column_play_count in play_counts:
#    print(row_play_count, column_play_count)
#############################################################################################
#Game3
A = np.array([[2.46-0.9,-2.46+0.5], [2.485-0.1,-2.485+0.5]])
B = np.array([[2.485-0.1,-2.485+0.5], [2.485-0.5,-2.485+0.5]])
prisoners_dilemma = nash.Game(A, B)

#Find utility when both players play their first strategy
#sigma_r = np.array([1, 0])
#sigma_c = np.array([1, 0])
#print(prisoners_dilemma[sigma_r, sigma_c])
#Find utility when both players play randomly across their strategies.
sigma_r = np.array([1 / 2, 1 / 2])
sigma_c = np.array([1 / 2, 1 / 2])
print(prisoners_dilemma[sigma_r, sigma_c])
##############################################################################################
#Game4
#Use of replicator dynamics algorithm.Returns strategies of row player over time. 
#Can also control the starting strategy. Useful for investigations.
#A = np.array([[3, 2], [4, 2]])
#game = nash.Game(A)
#y0 = np.array([0.9, 0.1]) #starting strategy
#timepoints = np.linspace(0, 10, 1000) #timepoints over the strategies.
#output = game.replicator_dynamics(y0=y0, timepoints=timepoints)
#print(output)
