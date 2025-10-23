# -*- coding: utf-8 -*-

#!pip install rdflib
import urllib.request
url = 'https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2025-2026/refs/heads/master/Assignment4/course_materials/python/validation.py'
urllib.request.urlretrieve(url, 'validation.py')
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2025-2026/master/Assignment4/course_materials"

"""Import RDFLib main methods"""

from rdflib import Graph, Namespace, Literal, XSD
from rdflib.namespace import RDF, RDFS
from validation import Report
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
r = Report()

"""Create a new class named Researcher"""

ns = Namespace("http://mydomain.org#")
g.add((ns.Researcher, RDF.type, RDFS.Class))
for s, p, o in g:
  print(s,p,o)

"""**Task 6.0: Create new prefixes for "ontology" and "person" as shown in slide 14 of the Slidedeck 01a.RDF(s)-SPARQL shown in class.**"""

# this task is validated in the next step
person = Namespace("http://oeg.fi.upm.es/def/people#")
ontology = Namespace("http://oeg.fi.upm.es/def/ontology#")

g.namespace_manager.bind("person", person, override=True)
g.namespace_manager.bind("ontology", ontology, override=True)
g.namespace_manager.bind("rdf", RDF, override=True)
g.namespace_manager.bind("rdfs", RDFS, override=True)
g.namespace_manager.bind("xsd", XSD, override=True)

"""**TASK 6.1: Reproduce the taxonomy of classes shown in slide 34 in class (all the classes under "Vocabulario", Slidedeck: 01a.RDF(s)-SPARQL). Add labels for each of them as they are in the diagram (exactly) with no language tags. Remember adding the correct datatype (xsd:String) when appropriate**

"""

# TO DO
clases_y_padres = [("Person", None),("Professor", "Person"),("FullProfessor", "Professor"),("AssociateProfessor", "Professor"),("InterimAssociateProfessor", "AssociateProfessor")]

for nombre, padre in clases_y_padres:
    clase = person[nombre]
    g.add((clase, RDF.type, RDFS.Class))
    g.add((clase, RDFS.label, Literal(nombre, datatype=XSD.string)))
    if padre:
        g.add((clase, RDFS.subClassOf, person[padre]))

# Visualize the results
for s, p, o in g:
  print(s,p,o)

# Validation. Do not remove
r.validate_task_06_01(g)

"""**TASK 6.2: Add the 3 properties shown in slide 36. Add labels for each of them (exactly as they are in the slide, with no language tags), and their corresponding domains and ranges using RDFS. Remember adding the correct datatype (xsd:String) when appropriate. If a property has no range, make it a literal (string)**"""

# TO DO
def agregar_propiedad(nombre, dominio=None, rango=None):
    prop = person[nombre]
    g.add((prop, RDF.type, RDF.Property))
    g.add((prop, RDFS.label, Literal(nombre, datatype=XSD.string)))
    if dominio:
        g.add((prop, RDFS.domain, dominio))
    if rango:
        g.add((prop, RDFS.range, rango))
    return prop

agregar_propiedad("hasColleague", dominio=person.Person,        rango=person.Person)
agregar_propiedad("hasName",      dominio=person.Person,        rango=RDFS.Literal)
agregar_propiedad("hasHomePage",  dominio=person.FullProfessor, rango=RDFS.Literal)

# Visualize the results
for s, p, o in g:
  print(s,p,o)

# Validation. Do not remove
r.validate_task_06_02(g)

"""**TASK 6.3: Create the individuals shown in slide 36 under "Datos". Link them with the same relationships shown in the diagram."**"""

# TO DO
datos = Namespace("http://oeg.fi.upm.es/resource/person/")
g.namespace_manager.bind("data", datos, True)

def agregar_individuo(nombre, tipo_rdf, etiqueta, propiedades=None):
    sujeto = datos[nombre]
    g.remove((sujeto, None, None))
    g.add((sujeto, RDF.type, tipo_rdf))
    g.add((sujeto, RDFS.label, Literal(etiqueta, datatype=XSD.string)))
    if propiedades:
        for predicado, objeto in propiedades:
            g.add((sujeto, predicado, objeto))
    return sujeto

oscar = agregar_individuo("Oscar", person.FullProfessor, "Oscar")
asun  = agregar_individuo("Asun",  person.AssociateProfessor, "Asun")
raul  = agregar_individuo("Raul",  person.InterimAssociateProfessor, "Raul")

g.add((oscar, person.hasColleague, asun))
g.add((oscar, person.hasName, Literal("Oscar Corcho García", datatype=XSD.string)))
g.add((asun, person.hasHomePage, Literal("http://www.oeg-upm.net/", datatype=XSD.string)))
g.add((asun, person.hasColleague, raul))


# Visualize the results
for s, p, o in g:
  print(s,p,o)

r.validate_task_06_03(g)

"""**TASK 6.4: Add to the individual person:Oscar the email address, given and family names. Use the properties already included in example 4 to describe Jane and John (https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2025-2026/master/Assignment4/course_materials/rdf/example4.rdf). Do not import the namespaces, add them manually**

"""

# TO DO
VCARD = Namespace("http://www.w3.org/2001/vcard-rdf/3.0/")
FOAF  = Namespace("http://xmlns.com/foaf/0.1/")

# el namespace de individuos que usaste en 6.3
data  = Namespace("http://oeg.fi.upm.es/resource/person/")
oscar = data.Oscar

# Añadir tres propiedades a Oscar (todas como xsd:string)
g.add((oscar, VCARD.Given,  Literal("Oscar",  datatype=XSD.string)))
g.add((oscar, VCARD.Family, Literal("Corcho", datatype=XSD.string)))
g.add((oscar, FOAF.email,   Literal("oscar@oeg-upm.net", datatype=XSD.string)))
# Visualize the results
for s, p, o in g:
  print(s,p,o)

# Validation. Do not remove
r.validate_task_06_04(g)
r.save_report("_Task_06")
