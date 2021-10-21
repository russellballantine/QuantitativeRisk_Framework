# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 23:52:51 2021
# LoadNet_new loads the XDSL file created by TestNet. It then prompts for a node from the modeller to update the marginal probabilities in terms of the environment 
# which will allow the BN to produce a static posterior risk output after COUNTERMEASURES ARE ADDED TO THE MODEL.
# The program reads in NewNet.xdsl or NewNet_withUtility.xdsl then prompts to allow indexing of relevant model objects to adjust marginal apriori probabilities.
# The cost of the security measures is calculated: S(l,t) = I(t)T(t)[1-E(l,t)] and saved.
# When the environmental adjustments have been made the modified Bayesian Network with adjusted CPT nodes is saved to NewNet_withUtility2.xdsl
@author: Russell Ballantine
"""
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 16:12:52 2020

@author: ballanr
"""

import pysmile
import numpy as np
#import addCountermeasures as addCountermeasures #Importing this applies the countermeasures defined in the OWL ontology
import CVSS_env_score as CVSS_env_score #NB this will run the CVSS_env_score script
from importlib import reload
#import pysmile_license
 
# LoadNet_new loads the XDSL file created by TestNet,
# It then prompts for a node from the modeller to update the marginal probabilities


 

class LoadNet_new:

    def __init__(self):

        print("Starting LoadNet_new...")

        net = pysmile.Network()

        

        # load the network created by Tutorial1

        net.read_file("NewNet.xdsl")

        

#        print("Posteriors with no evidence set:")

#        net.update_beliefs()
#
#        self.print_all_posteriors(net)
#        net.set_evidence("VRTX11", "Success")
#        net.update_beliefs()
#        beliefs = net.get_node_value("VRTX11")
#        print(beliefs)
#        beliefs2 = net.get_node_value("VRTX22") # This is the posterior probability
#        print(beliefs2)
#        outcomeID = net.get_outcome_id("VRTX10",0) # This is the outcome of the node, indexed on possible outcomes
#        print(outcomeID)
#        IDs = net.get_all_nodes() # produces an array of node IDs.
#        print(IDs)
        CyberSecurityLoss = []
#        addCountermeasures
        #print(addCountermeasures.LDAPauthentication[0])
        node = input("Enter node to be adjusted for environment score, if none type 'none' :")
        while node != "none":
            node = str(node)
            child = net.get_child_ids(node) # Gets all children of a node
            print("Child node is: " + str(child))
#           parent = net.get_parent_ids("VRTX11")
#           print(parent)
            definition_cpt = np.array(net.get_node_definition(child[0])) #Get the CPT table
            print("CPT table of of child node is: " + str(definition_cpt))
            definition_cpt[0] = round(CVSS_env_score.DeltaValue*definition_cpt[0],4) #Multiply original probability by the Delta value (CPT now representing Efficacy) 
            definition_cpt[1] = round(1-definition_cpt[0],4)
            print("Check modified CPT table: " + str(definition_cpt))
        
            #net.set_node_definition("VRTX11",[0.1, 0.9, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]) # update the cpt table 
            net.set_node_definition(child[0],definition_cpt)
            definition_cpt = net.get_node_definition(child[0])
            print("Updated CPT table: " + str(definition_cpt))
            #CyberSecurityLoss = CVSS_env_score.Impact*definition_cpt[0]*definition_cpt[1] #S(l,t) = I(t)T(t)[1 - E(l,t)]
            CyberSecurityLoss.append(child[0])
            CyberSecurityLoss.append(round(CVSS_env_score.Impact*definition_cpt[0]*definition_cpt[1],4))
            print("Cyber Security loss at this control level(CSL): " + str(CyberSecurityLoss))
            with open('Game_Matrix_loss.txt', 'a') as f:
                for item in CyberSecurityLoss:
                    f.write("%s\n" % item)                  
            net.write_file("NewNet_SecPolicy8.xdsl")  #Update and save to a new network. Original network remains unchanged.
            reload(CVSS_env_score)
            node = input("Enter node to be adjusted for environment score, if none type 'none' :")
            node = str(node)
            if node == "none":
                break;
                
            
#       
        

        print("LoadNet_new complete.")

        net.write_file("NewNet_SecPolicy8.xdsl")  #No need to do this unless we are updating the structure of the net. 
        print("Modified Network written to NewNet_SecPolicy8.xdsl")

 

    def print_posteriors(self, net, node_handle):

        node_id = net.get_node_id(node_handle)

        if net.is_evidence(node_handle):

            print(node_id + " has evidence set (" +

                  net.get_outcome_id(node_handle, 

                                     net.get_evidence(node_handle)) + ")")

        else :

            posteriors = net.get_node_value(node_handle)

            for i in range(0, len(posteriors)):

                print("P(" + node_id + "=" + 

                      net.get_outcome_id(node_handle, i) +

                      ")=" + str(posteriors[i]))

 

    def print_all_posteriors(self, net):

        for handle in net.get_all_nodes():

            self.print_posteriors(net, handle)

 

    

    def change_evidence_and_update(self, net, node_id, outcome_id):

        if outcome_id is not None:

            net.set_evidence(node_id, outcome_id)        

        else:

            net.clear_evidence(node_id)

        

        net.update_beliefs()

        self.print_all_posteriors(net)

        print("")

    