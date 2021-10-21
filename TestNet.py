# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 14:47:27 2020
This program reads in the .csv files output from MulVAL for arcs and vertices and creates the Bayesian Network. It uses the StructureNet() function to work out the 
dimensions of the cpt tables. To do this it first needs to know the structure of the net.
@author: ballanr
"""

import pysmile
import csv
#from itertools import zip_longest
import numpy as np
#import pandas as pd
from StructureNet import StructureNet
import re
from io import StringIO
import sys
#import pysmile_license
 

# TestNet creates the Bayesian Network structure from the Mulval
#Vertex and Arc CSV files. 

# then writes its content as XDSL file to disk.

 

class TestNet:

    def __init__(self):
        
       
        
        net = pysmile.Network()
        
        #Read in the Vartices of the BN
        
        with open('VERTICES4.CSV') as csvDataFile:
            #csvReader = csv.reader(csvDataFile)
            data = [row for row in csv.reader(csvDataFile,delimiter=',')]
            nodes = []
            vertices = []
            description = []
            probability = []
            for row in data:
                name1="node"
                name2="VRTX"
                nodes.append(name1+row[0])
                vertices.append(name2+row[0])
                description.append(row[1])
                probability.append(row[3])
                     
        #Check the vertices        
        print(nodes)
        print(vertices)
        print(description)
        print(probability)
        print(len(nodes))
        print(len(vertices))
        print(len(description))
        print(len(probability))
                       
        #Create the node structure
#        
        for i in range(len(nodes)):
            if i != 0:
                
                nodes[i] = self.create_cpt_node(net,

                vertices[i], description[i],

                ["Success","Failure"], 

                (100*i), (40*i))
                
#
#           
        #Read the ARCS file
        with open('ARCS4.CSV') as csvDataFile:
            #csvReader = csv.reader(csvDataFile)
            data = [row for row in csv.reader(csvDataFile,delimiter=',')]
            dest = []
            source = []
            direction = []
            for row in data:
                name="VRTX"
                dest.append(name+row[0])
                source.append(name+row[1])
                direction.append(row[2])
        
        #Draw the ARCS
        for i in range(len(dest)):
            if i != 0:
                net.add_arc(source[i],dest[i])
        
        #Check the arcs        
        print(dest)
        print(source)
        print(direction)
##################################################################################################################################################################        
#++++++++++++++++++++++++++++++++++Disable this section on first run to get net structure+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++     
        # Add the initial probability values.
        #Use StructureNet() to find the dimensions of the CPT tables
        #Gather output to standard out
        
        old_stdout = sys.stdout
        sys.stdout = mystdout = StringIO()
        output = StructureNet();            #StructureNet() to standard out
        sys.stdout = old_stdout
        dimensions = mystdout.getvalue()
        result = re.findall('^Node name:.*$',dimensions, re.MULTILINE)
        #print(result[5].split(':'))
        
#        #Create dictionary of CPT dimensions
        node_dimension = []
        dimension_dict = {}
        for i in range(len(vertices)-1):
            node_dimension.append(result[i].split(':'))
        print(node_dimension[0][1])  #Node value
        print(node_dimension[0][2])  #Dimension value
        print(len(node_dimension))
        
        for i in range(len(vertices)-1):
            dimension_dict[node_dimension[i][1]] = int(node_dimension[i][2])
        print(dimension_dict)
        
        
        #Use dictionary and initialise the CPT tables
        for i in range(len(vertices)-1):
            if i != 0:
                b = [0,1]
                VRTX_Def = [0.5 for _ in range(2**dimension_dict[vertices[i]])]
                VRTX_Def[0] = np.array([

                float(probability[i]),
##
                ])
                VRTX_Def[1] = np.array([

                1-float(probability[i]),
##
                ])
                VRTX = vertices[i]
                net.set_node_definition(VRTX, VRTX_Def)
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++      
#####################################################################################################################################################
#        VRTX2_Def = [
#
#            float(probability[2]), # P(VRTX2=S|VRTX1=U)
#
#            1-float(probability[2]), # P(VRTX2=F|VRTX1=U)
#
#            0.5, # P(VRTX2=S|VRTX1=F)
#
#            0.5, # P(VRTX2=F|VRTX1=F)
#            
#        ]
#        VRTX2 = vertices[2]
#        net.set_node_definition(VRTX2, VRTX2_Def)

        
#
#        
      

        net.write_file("NewNet.xdsl")
       

        print("TestNet complete: Network written to NewNet.xdsl")

 

    def create_cpt_node(self, net, id, name, outcomes, x_pos, y_pos):

        handle = net.add_node(pysmile.NodeType.CPT, id)

        

        net.set_node_name(handle, name)

        net.set_node_position(handle, x_pos, y_pos, 85, 55)
      

        initial_outcome_count = net.get_outcome_count(handle)
       

        for i in range(0, initial_outcome_count):

            net.set_outcome_id(handle, i, outcomes[i])
        

        for i in range(initial_outcome_count, len(outcomes)):

            net.add_outcome(handle, outcomes[i])
           

        return handle

