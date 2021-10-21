# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 21:20:09 2021

@author: ballanr
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 18:27:22 2021

@author: ballanr
"""

from owlready2 import *

#import the ontology
onto_path.append("C:\\Users\\ballanr\\Desktop\\Data_Science\\Edinburgh_University\\DATA SCIENCE MSc\\Dissertation_Ideas\\Baysian_Networks_information_assurance\\Ontologies\\security-ontology-ontologies-owl-REVISION-HEAD\\NewOntologies")
onto = get_ontology("SecOntology_RDFXML.owl")
#clear
onto.load()

namespace = onto.get_namespace("http://www.w3.org/2002/07/owl#")
#namespace = onto.get_namespace("http://www.w3.org/XML/1998/namespace")
#namespace = onto.get_namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")                               
                               
#Function to render ontology using labels
def render_using_label(entity):
    return entity.label.first() or entity.name
#                               
#set_render_func(render_using_label)
print(namespace)

