# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 20:59:43 2020

@author: ballanr
"""

import pysmile

 

# pysmile_license is your license key

import pysmile_license

 

def hello_smile():

    net = pysmile.Network()  #Create a network

    net.read_file("VentureBN.xdsl"); 
   # net.read_file("AttackGraph.xml");

        

    net.set_evidence("Forecast", "Moderate")

    net.update_beliefs()

 

    beliefs = net.get_node_value("Success")

    for i in range(0, len(beliefs)):

        print(net.get_outcome_id("Success", i) + "=" + str(beliefs[i]))

 

hello_smile()