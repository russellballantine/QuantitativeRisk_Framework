# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 11:16:00 2020

@author: ballanr
"""

import pysmile

def hello_smile():
    net = pysmile.Network()
    net.read_file("C:\\Users\\ballanr\\Desktop\\Data_Science\\Edinburgh_University\\DATA SCIENCE MSc\\Dissertation_Ideas\\Baysian_Networks_information_assurance\\Genie Models\\VentureBN");
    net.set_evidence("Forecast", "Moderate")
    net.update_beliefs()
    beliefs = net.get_node_value("Success")
    for i in range(0, len(beliefs)):
        print(net.get_outcome_id("Success", i)
        + "=" + str(beliefs[i]))
hello_smile()