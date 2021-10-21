# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 18:27:22 2021

@author: ballanr
"""

from owlready2 import *
import sys
import addCountermeasures as addCountermeasures
#import the ontology
addCountermeasures
onto_path.append("C:\\Users\\ballanr\\Desktop\\Data_Science\\Edinburgh_University\\DATA SCIENCE MSc\\Dissertation_Ideas\\Baysian_Networks_information_assurance\\Ontologies\\security-ontology-ontologies-owl-REVISION-HEAD\\NewOntologies")
onto = get_ontology("SecOntology_RDFXML_Policy8.owl").load()

namespace = onto.get_namespace("http://www.w3.org/2002/07/owl#")
#namespace = onto.get_namespace("http://www.w3.org/XML/1998/namespace")
#namespace = onto.get_namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")                               
                               
#Function to render ontology using labels
def render_using_label(entity):
    return entity.label.first() or entity.name
                               
set_render_func(render_using_label)



###################################################  EXPLORATION OF THE ONTOLOGY  #####################################################

# Prnt the classes,instances and subclasses
#classes = list(onto.classes())
#print(classes)
#for i in classes: 
#    print(i)
#    print(i.instances())0
#    print(list(i.subclasses()))


##Get the BaseScores of a CVE vulnerability
#indvs = onto.individuals()
#indvs = list(onto.individuals())
#print(indvs)
#print(indvs[1].BaseScoreValue)

###Get list of data property assertion values 
#CVE_properties = list(onto.data_properties())
#print(CVE_properties)

#Get a value for a data property

#for i in CVE_properties: 
#    print(i,i.type)
    #print(i.instances())
    #print(list(i.subclasses()))

#print(output2)
#output3 = list(onto.object_properties())
#print(output3[13].type)
#    
#output4 = list(onto.properties())
#print(output4)


#output5 = list(onto.annotation_properties())
#print(output5)
#output6 = list(onto.data_properties())
#print(output6)
#output7= onto.search(iri = "*")
#output7
#print(output6[13].type) #Returns the value
#print(output6[1].type)

#onto.metadata.comment.append("comment:experimenting with Owlready2.0")
#print(onto.metadata.comment)

#Save the ontology 
#onto.save()
    
##############################################################################################################################################
###################################################  END OF EXPLORATION OF THE ONTOLOGY  #####################################################
##############################################################################################################################################
#
#
#
##############################################################################################################################################
################################################## CALCULATE THE ENVIRONMENTAL SCORE #########################################################
#
# 1/Calculate the Ajusted Impact Score, AdjustedImpact = min(10,10.41 * (1-(1-ConfImpact*ConfReq) * (1-IntegImpact*IntegReq) * (1-AvailImpact*AvailReq)))
# 2/Recalculate the new Base Score using the Adjusted Impact Score
# 3/Calculate the Adjusted Temporal Score: TemporalScore = round_to_1_decimal(BaseScore * Exploitability * RemediationLevel * ReportConfidence)
# 4/Calculate the Environmental Score: EnvironmentalScore = round_to_1_decimal((AdjustedTemporal+(10-AdjustedTemporal)*CollateralDamagePotential)*TargetDistribution
##############################################################################################################################################
    
    
#Variables
    
classes = list(onto.classes())
print("Available classes are:")
print(classes)
print("                                                                  ")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("                                                                  ")


indvs = onto.individuals()
indvs = list(onto.individuals())
print("Available Individuals are:")
print(indvs)
print("                                                                  ")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("                                                                  ")


#Model the environment from user input
num = input("Enter Asset individual,100 to exit :")
num = int(num)
if num == 100:
    sys.exit("exiting program")
else:


#Calculate the adjusted Impact score for an individual vulnerability on an asset
#-------------------------------------------------------------------------------
# Equation is: "AdjustedImpact = min(10,10.41 * (1-(1-ConfImpact*ConfReq) * (1-IntegImpact*IntegReq) * (1-AvailImpact*AvailReq)))"
    AdjustedImpact = min(10,10.41 * (1-(1-(indvs[num].ConfImpact)*(indvs[num].ConfReq)) * (1-(indvs[num].IntegImpact)*(indvs[num].IntegReq)) * (1-(indvs[num].AvailImpact)*(indvs[num].AvailReq))))
    print("Adjusted Impact Score is: " + str(AdjustedImpact))



##Calculate the new Base Score
##-----------------------------
##BaseScore  =  round_to_1_decimal(((0.6*Impact)+(0.4*Exploitability)–1.5)*f(Impact))
##Impact  =  10.41*(1-(1-indvs[1].ConfImpact)*(1-indvs[1].IntegImpact)*(1-indvs[1].AvailImpact))
##Exploitability  =  20* AccessVector*AccessComplexity*Authentication
##f(impact) =  0 if Impact=0, 1.176 otherwise
##print(Impact)
    num = input("Enter vulnerability individual :") 
    num = int(num)
    Impact  =  AdjustedImpact
    #Exploitability  =  (20*(indvs[num].AccessVector))*(indvs[num].AccessComplexity)*(indvs[num].Authentication)
    Exploitability  =  20*(indvs[num].AccessVector)*(indvs[num].AccessComplexity)*(indvs[num].Authentication)
    if Impact == 0:
        fimpact = 0
    else:
        fimpact = 1.176
#    fimpact = 1.176
    NewBaseScore  =  round(((0.6*Impact)+(0.4*Exploitability)-1.5)*fimpact , 2)
    OriginalBaseScore = indvs[num].BaseScoreValue
    print("Original Base Score is: " + str(OriginalBaseScore))
    print("New Base score is: " + str(NewBaseScore))

#Calculate the Adjusted Temporal Score
##------------------------------------
#TemporalScore = round_to_1_decimal(NewBaseScore * Exploitability * RemediationLevel * ReportConfidence)
    AdjustedTemporalScore = round(NewBaseScore*(indvs[num].Exploitability)*(indvs[num].RemediationLevel)*(indvs[num].ReportConfidence),1)
    print("Modified Temporal Score is: " + str(AdjustedTemporalScore))

#Calculate the Environmental Score
##--------------------------------
#Equation is: EnvironmentalScore = round_to_1_decimal((AdjustedTemporal+(10-AdjustedTemporal)*CollateralDamagePotential)*TargetDistribution
    EnvironmentalScore = round((AdjustedTemporalScore+(10-AdjustedTemporalScore)*(indvs[num].CollateralDamagePotential)*(indvs[num].TargetDistribution)),1)

    print("Environmental Score is: " + str(EnvironmentalScore))


#Print and store DeltaValue which will be used as a relative %reduction to modify the probabilities of the nodes. 
    Reduction = OriginalBaseScore - EnvironmentalScore
    RelativeReduction = Reduction/10
    DeltaValue = round(1-RelativeReduction,2)
    print("DeltaValue is: " + str(DeltaValue))