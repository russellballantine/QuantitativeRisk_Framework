# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 20:45:35 2021

@author: ballanr
"""

from owlready2 import *

#import the ontology
onto_path.append("C:\\Users\\ballanr\\Desktop\\Data_Science\\Edinburgh_University\\DATA SCIENCE MSc\\Dissertation_Ideas\\Baysian_Networks_information_assurance\\Ontologies\\security-ontology-ontologies-owl-REVISION-HEAD")
onto = get_ontology("http://www.lesfleursdunormal.fr/static/_downloads/pizza_onto.owl").load()

#namespace = onto.get_namespace("http://www.w3.org/2002/07/owl#")
#namespace.Asset

with onto:
    class Drug(Thing):
        namespace = onto

    class Ingredient(Thing):
        pass
    
    class has_for_ingredient(ObjectProperty):
        domain = [Drug]
        range = [Ingredient]
        
class DrugAssociation(Drug): # a new class inheriting from Drug
        pass
    
#list the classes
output = list(onto.classes())
print(output)
print(Drug.iri)
print(DrugAssociation.is_a)

