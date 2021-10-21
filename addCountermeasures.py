# -*- coding: utf-8 -*-
"""
Created on Tue May 25 18:36:24 2021
This script is imported by CVSS_env_score and updates the asset and vulnerability CVSS metrics 
in response to the countermeasures defined in the ontology. THis occurs prior to evaluation of the 
environmental metrics.

@author: ballanr
"""

from owlready2 import *
import sys
#import the ontology
onto_path.append("C:\\Users\\ballanr\\Desktop\\Data_Science\\Edinburgh_University\\DATA SCIENCE MSc\\Dissertation_Ideas\\Baysian_Networks_information_assurance\\Ontologies\\security-ontology-ontologies-owl-REVISION-HEAD\\NewOntologies")
onto = get_ontology("SecOntology_RDFXML_Policy8.owl").load()

namespace = onto.get_namespace("http://www.w3.org/2002/07/owl#")
#namespace = onto.get_namespace("http://www.w3.org/XML/1998/namespace")
#namespace = onto.get_namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")                               
                               
#Function to render ontology using labels
def render_using_label(entity):
    return entity.label.first() or entity.name
                               
set_render_func(render_using_label)

# Prnt the classes,instances and subclasses
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


print("Data Properties")
print("================")
CVE_properties = list(onto.data_properties())
print(CVE_properties)
print("                  ")
print("Object Properties")
print("================")
output3 = list(onto.object_properties())
print(output3)

print("                                                                  ")
print("Countermeasures applied in this ontology")
print("========================================") 
AppliedCountermeasures = onto.hasCountermeasure.get_relations() #Get a list of where the countermeasures are applied in the ontology
Countermeasures = list(AppliedCountermeasures)
print(Countermeasures)

#Modify the ontology with results of the countermeasures
for c in Countermeasures:
    #if str(c) == "LDAPauthentication":
    #if str(c[0]).__class__ == "Countermeasures":
    if "LDAPauthentication" in str(c):
        #print(onto.LDAPauthentication.CostMetric)
        c[0].Authentication = onto.LDAPauthentication.Authentication
    elif "BehindHostFirewall" in str(c):
        #print(onto.BehindHostFirewall.CostMetric)
        c[0].AccessVector = onto.BehindHostFirewall.AccessVector
    elif "CERTauthentication" in str(c):
        #print(onto.CERTauthentication.CostMetric)
        c[0].Authentication = onto.CERTauthentication.Authentication
    elif "End2EndPipeLineEncryption" in str(c):
        #print(onto.End2EndPipeLineEncryption.CostMetric)
        c[0].ConfImpact = onto.End2EndPipeLineEncryption.ConfImpact
    elif "PartialPipelineEncryption" in str(c):
        #print(onto.PartialPipelineEncryption.CostMetric)
        c[0].ConfImpact = onto.PartialPipelineEncryption.ConfImpact
    elif "IntrusionDetectionDeployed" in str(c):
        #print(onto.IntrusionDetectionDeployed.CostMetric)
        c[0].IntegImpact = onto.IntrusionDetectionDeployed.IntegImpact
    elif "BehindNetworkFirewall" in str(c):
        #print(onto.BehindNetworkFirewall.CostMetric)
        c[0].AccessVector = onto.BehindNetworkFirewall.AccessVector
    elif "DisasterRecoveryStrategy" in str(c):
        #print(onto.DisasterRecoveryStrategy.CostMetric)
        c[0].AvailImpact = onto.DisasterRecoveryStrategy.AvailImpact
    elif "DisasterRecoveryStrategyPartial" in str(c):
        #print(onto.DisasterRecoveryStrategyPartial.CostMetric)
        c[0].AvailImpact = onto.DisasterRecoveryStrategyPartial.AvailImpact
    elif "IPSandDoSMitigation" in str(c):
        #print(onto.IPSandDoSMitigation.CostMetric)
        c[0].IntegImpact = onto.IPSandDoSMitigation.IntegImpact
    elif "ApplicationSandboxApplies" in str(c):
        #print(onto.ApplicationSandboxApplies.CostMetric)
        c[0].CollateralDamagePotential = onto.ApplicationSandboxApplies.CollateralDamagePotential
    elif "ApplicationWhitelistingApplies" in str(c):
        #print(onto.ApplicationWhitelistingApplies.CostMetric)
        c[0].CollateralDamagePotential = onto.ApplicationWhitelistingApplies.CollateralDamagePotential
    elif "DeviceHardeningPolicyApplies" in str(c):
        #print(onto.DeviceHardeningPolicyApplies.CostMetric)
        c[0].AccessComplexity = onto.DeviceHardeningPolicyApplies.AccessComplexity
    elif "MultiFactorAuthentication" in str(c):
        #print(onto.MultiFactorAuthentication.CostMetric)
        c[0].Authentication = onto.MultiFactorAuthentication.Authentication
    elif "NoAuthentication" in str(c):
        #print(onto.NoAuthentication.CostMetric)
        c[0].Authentication = onto.NoAuthentication.Authentication
    elif "NoFirewall" in str(c):
        #print(onto.NoFirewall.CostMetric)
        c[0].AccessVector = onto.NoFirewall.AccessVector
    elif "NoHardeningPolicyApplies" in str(c):
        #print(onto.NoHardeningPolicyApplies.CostMetric)
        c[0].AccessComplexity = onto.NoHardeningPolicyApplies.AccessComplexity
    elif "PartialHardeningPolicyApplies" in str(c):
        #print(onto.PartialHardeningPolicyApplies.CostMetric)
        c[0].AccessComplexity = onto.PartialHardeningPolicyApplies.AccessComplexity
    elif "PasswordPolicyAutoEnforced" in str(c):
        #print(onto.PasswordPolicyAutoEnforced.CostMetric)
        c[0].Authentication = onto.PasswordPolicyAutoEnforced.Authentication
    elif "TempFixAvailable" in str(c):
        #print(onto.TempFixAvailable.CostMetric)
        c[0].RemediationLevel = onto.TempFixAvailable.RemediationLevel

#Check the Countermeasures have been adjusted correctly.
#indvs = onto.individuals()
#for i in indvs:
#    print(i.Authentication)

#Save the countermeasure metrics set on individuals to a file for later use in the Gaming Matrix. 
#CyberSecurityCost = []   
#=====================================================================================================
        
        
# Record the cost metrics for those individuals which have countermeasures set
#
        
indvs = onto.individuals()

LDAPauthentication = []
BehindHostFirewall = [] 
CERTauthentication = []
End2EndPipeLineEncryption = []
PartialPipelineEncryption = []
IntrusionDetectionDeployed = []
BehindNetworkFirewall = []
DisasterRecoveryStrategy = []
IPSandDoSMitigation = []
NoAuthentication = []
NoFirewall = []
DeviceHardeningPolicyApplies = []
PartialHardeningPolicyApplies = []
NoHardeningPolicyApplies = []
PasswordPolicyAutoEnforced = []
MultiFactorAuthentication = []
ApplicationWhitelistingApplies = []
ApplicationSandboxApplies = []

for i in indvs:
    #if i.hasCountermeasure:
        print(i.hasCountermeasure)
        if "LDAPauthentication" in str(i.hasCountermeasure):
            with open('Game_Matrix_cost.txt', 'a') as f:
                #f.write("\n")
                for item in str(i):
                    f.write("%s" % item)
                for item in str(onto.LDAPauthentication.CostMetric):
                    f.write("%s" % item)
                f.write("\n")
                LDAPauthentication = onto.LDAPauthentication.CostMetric
                #print(LDAPauthentication)
        if "BehindHostFirewall" in str(i.hasCountermeasure):
            with open('Game_Matrix_cost.txt', 'a') as f:
                #f.write("\n")
                for item in str(i):
                    f.write("%s" % item)
                for item in str(onto.BehindHostFirewall.CostMetric):
                    f.write("%s" % item)
                f.write("\n")
                BehindHostFirewall = onto.BehindHostFirewall.CostMetric
                #print(BehindHostFirewall)
        if "CERTauthentication" in str(i.hasCountermeasure):
            with open('Game_Matrix_cost.txt', 'a') as f:
                #f.write("\n")
                for item in str(i):
                    f.write("%s" % item)
                for item in str(onto.CERTauthentication.CostMetric):
                    f.write("%s" % item)
                f.write("\n")
                CERTauthentication = onto.CERTauthentication.CostMetric
                #print(CERTauthentication)
        if "End2EndPipeLineEncryption" in str(i.hasCountermeasure):
            with open('Game_Matrix_cost.txt', 'a') as f:
                #f.write("\n")
                for item in str(i):
                    f.write("%s" % item)
                for item in str(onto.End2EndPipeLineEncryption.CostMetric):
                    f.write("%s" % item)
                f.write("\n")
                End2EndPipeLineEncryption = onto.End2EndPipeLineEncryption.CostMetric
                #print(End2EndPipeLineEncryption)
        if "PartialPipelineEncryption" in str(i.hasCountermeasure):
            with open('Game_Matrix_cost.txt', 'a') as f:
                #f.write("\n")
                for item in str(i):
                    f.write("%s" % item)
                for item in str(onto.PartialPipelineEncryption.CostMetric):
                    f.write("%s" % item)
                f.write("\n")
                PartialPipelineEncryption = onto.PartialPipelineEncryption.CostMetric
                #print(PartialPipelineEncryption)
        if "IntrusionDetectionDeployed" in str(i.hasCountermeasure):
            with open('Game_Matrix_cost.txt', 'a') as f:
                #f.write("\n")
                for item in str(i):
                    f.write("%s" % item)
                for item in str(onto.IntrusionDetectionDeployed.CostMetric):
                    f.write("%s" % item)
                f.write("\n")
                IntrusionDetectionDeployed = onto.IntrusionDetectionDeployed.CostMetric
                #print(IntrusionDetectionDeployed)
        if "BehindNetworkFirewall" in str(i.hasCountermeasure):
            with open('Game_Matrix_cost.txt', 'a') as f:
                #f.write("\n")
                for item in str(i):
                    f.write("%s" % item)
                for item in str(onto.BehindNetworkFirewall.CostMetric):
                    f.write("%s" % item)
                f.write("\n")
                BehindNetworkFirewall = onto.BehindNetworkFirewall.CostMetric
                #print(BehindNetworkFirewall)
        if "DisasterRecoveryStrategy" in str(i.hasCountermeasure):
            with open('Game_Matrix_cost.txt', 'a') as f:
                #f.write("\n")
                for item in str(i):
                    f.write("%s" % item)
                for item in str(onto.DisasterRecoveryStrategy.CostMetric):
                    f.write("%s" % item)
                f.write("\n")
                DisasterRecoveryStrategy = onto.DisasterRecoveryStrategy.CostMetric
                #print(DisasterRecoveryStrategy)
        if "DisasterRecoveryStrategyPartial" in str(i.hasCountermeasure):
            with open('Game_Matrix_cost.txt', 'a') as f:
                #f.write("\n")
                for item in str(i):
                    f.write("%s" % item)
                for item in str(onto.DisasterRecoveryStrategyPartial.CostMetric):
                    f.write("%s" % item)
                f.write("\n")
                DisasterRecoveryStrategyPartial = onto.DisasterRecoveryStrategyPartial.CostMetric
                #print(DisasterRecoveryStrategyPartial)
        if "IPSandDoSMitigation" in str(i.hasCountermeasure):
            with open('Game_Matrix_cost.txt', 'a') as f:
                #f.write("\n")
                for item in str(i):
                    f.write("%s" % item)
                for item in str(onto.IPSandDoSMitigation.CostMetric):
                    f.write("%s" % item)
                f.write("\n")
                IPSandDoSMitigation = onto.IPSandDoSMitigation.CostMetric
                #print(IPSandDoSMitigation)
        if "NoAuthentication" in str(i.hasCountermeasure):
            with open('Game_Matrix_cost.txt', 'a') as f:
                #f.write("\n")
                for item in str(i):
                    f.write("%s" % item)
                for item in str(onto.NoAuthentication.CostMetric):
                    f.write("%s" % item)
                f.write("\n")
                NoAuthentication = onto.NoAuthentication.CostMetric
                #print(NoAuthentication)
        if "NoFirewall" in str(i.hasCountermeasure):
            with open('Game_Matrix_cost.txt', 'a') as f:
                #f.write("\n")
                for item in str(i):
                    f.write("%s" % item)
                for item in str(onto.NoFirewall.CostMetric):
                    f.write("%s" % item)
                f.write("\n")
                NoFirewall = onto.NoFirewall.CostMetric
                #print(NoFirewall)
        if "DeviceHardeningPolicyApplies" in str(i.hasCountermeasure):
            with open('Game_Matrix_cost.txt', 'a') as f:
                #f.write("\n")
                for item in str(i):
                    f.write("%s" % item)
                for item in str(onto.DeviceHardeningPolicyApplies.CostMetric):
                    f.write("%s" % item)
                f.write("\n")
                DeviceHardeningPolicyApplies = onto.DeviceHardeningPolicyApplies.CostMetric
                #print(DeviceHardeningPolicyApplies)
        if "PartialHardeningPolicyApplies" in str(i.hasCountermeasure):
            with open('Game_Matrix_cost.txt', 'a') as f:
                #f.write("\n")
                for item in str(i):
                    f.write("%s" % item)
                for item in str(onto.PartialHardeningPolicyApplies.CostMetric):
                    f.write("%s" % item)
                f.write("\n")
                PartialHardeningPolicyApplies = onto.PartialHardeningPolicyApplies.CostMetric
                #print(NoAuthentication)
        if "NoHardeningPolicyApplies" in str(i.hasCountermeasure):
            with open('Game_Matrix_cost.txt', 'a') as f:
                #f.write("\n")
                for item in str(i):
                    f.write("%s" % item)
                for item in str(onto.NoHardeningPolicyApplies.CostMetric):
                    f.write("%s" % item)
                f.write("\n")
                NoHardeningPolicyApplies = onto.NoHardeningPolicyApplies.CostMetric
                #print(NoHardeningPolicyApplies)
        if "PasswordPolicyAutoEnforced" in str(i.hasCountermeasure):
            with open('Game_Matrix_cost.txt', 'a') as f:
                #f.write("\n")
                for item in str(i):
                    f.write("%s" % item)
                for item in str(onto.PasswordPolicyAutoEnforced.CostMetric):
                    f.write("%s" % item)
                f.write("\n")
                PasswordPolicyAutoEnforced = onto.PasswordPolicyAutoEnforced.CostMetric
                #print(PasswordPolicyAutoEnforced)
        if "MultiFactorFactorAuthentication" in str(i.hasCountermeasure):
            with open('Game_Matrix_cost.txt', 'a') as f:
                #f.write("\n")
                for item in str(i):
                    f.write("%s" % item)
                for item in str(onto.MultiFactorAuthentication.CostMetric):
                    f.write("%s" % item)
                f.write("\n")
                MultiFactorAuthentication = onto.MultiFactorAuthentication.CostMetric
                #print(MultiFactorAuthentication)
        if "ApplicationWhitelistingApplies" in str(i.hasCountermeasure):
            with open('Game_Matrix_cost.txt', 'a') as f:
                #f.write("\n")
                for item in str(i):
                    f.write("%s" % item)
                for item in str(onto.ApplicationWhitelistingApplies.CostMetric):
                    f.write("%s" % item)
                f.write("\n")
                ApplicationWhitelistingApplies = onto.ApplicationWhitelistingApplies.CostMetric
                #print(ApplicationWhitelistingApplies)
        if "ApplicationSandboxApplies" in str(i.hasCountermeasure):
            with open('Game_Matrix_cost.txt', 'a') as f:
                #f.write("\n")
                for item in str(i):
                    f.write("%s" % item)
                for item in str(onto.ApplicationSandboxApplies.CostMetric):
                    f.write("%s" % item)
                f.write("\n")
                ApplicationSandboxApplies = onto.ApplicationSandboxApplies.CostMetric
                #print(ApplicationSandboxApplies)
        else:
            print("No countermeasures appear to be set")
            
        
#Save the ontology 
#onto.save()