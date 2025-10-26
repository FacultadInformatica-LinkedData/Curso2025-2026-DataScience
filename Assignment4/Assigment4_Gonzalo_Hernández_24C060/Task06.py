{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/gonzahv24/Curso2025-2026-DataScience/blob/master/Assignment4/Assigment4_Gonzalo_Hern%C3%A1ndez_24C060/Task06.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "nOOPLCHF7hLB"
      },
      "source": [
        "**Task 06: Modifying RDF(s)**"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 13,
      "metadata": {
        "id": "Yl9npCt8n6m-",
        "outputId": "576c3c73-0cf1-4cdb-c440-09a68c4da5ed",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: rdflib in /usr/local/lib/python3.12/dist-packages (7.3.0)\n",
            "Requirement already satisfied: pyparsing<4,>=2.1.0 in /usr/local/lib/python3.12/dist-packages (from rdflib) (3.2.5)\n"
          ]
        }
      ],
      "source": [
        "!pip install rdflib\n",
        "import urllib.request\n",
        "url = 'https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2025-2026/refs/heads/master/Assignment4/course_materials/python/validation.py'\n",
        "urllib.request.urlretrieve(url, 'validation.py')\n",
        "github_storage = \"https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2025-2026/master/Assignment4/course_materials\""
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "XY7aPc86Bqoo"
      },
      "source": [
        "Import RDFLib main methods"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 14,
      "metadata": {
        "id": "9ERh415on7kF"
      },
      "outputs": [],
      "source": [
        "from rdflib import Graph, Namespace, Literal, XSD\n",
        "from rdflib.namespace import RDF, RDFS\n",
        "from validation import Report\n",
        "g = Graph()\n",
        "g.namespace_manager.bind('ns', Namespace(\"http://somewhere#\"), override=False)\n",
        "r = Report()"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "gM3DASkTQQ5Y"
      },
      "source": [
        "Create a new class named Researcher"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 15,
      "metadata": {
        "id": "6vtudax8Xb7b",
        "outputId": "78da9a2c-a7c6-4d23-eb2b-0b6a3865d421",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "http://mydomain.org#Researcher http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Class\n"
          ]
        }
      ],
      "source": [
        "ns = Namespace(\"http://mydomain.org#\")\n",
        "g.add((ns.Researcher, RDF.type, RDFS.Class))\n",
        "for s, p, o in g:\n",
        "  print(s,p,o)"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Task 6.0: Create new prefixes for \"ontology\" and \"person\" as shown in slide 14 of the Slidedeck 01a.RDF(s)-SPARQL shown in class.**"
      ],
      "metadata": {
        "id": "ZX8w9jnV5Xhp"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# this task is validated in the next step\n",
        "ont = Namespace(\"http://oeg.fi.upm.es/def/ontology#\")\n",
        "per = Namespace(\"http://oeg.fi.upm.es/def/people#\")"
      ],
      "metadata": {
        "id": "b1ZQgYgB5vi7"
      },
      "execution_count": 16,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "qp1oe2Eddsvo"
      },
      "source": [
        "**TASK 6.1: Reproduce the taxonomy of classes shown in slide 34 in class (all the classes under \"Vocabulario\", Slidedeck: 01a.RDF(s)-SPARQL). Add labels for each of them as they are in the diagram (exactly) with no language tags. Remember adding the correct datatype (xsd:String) when appropriate**\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 17,
      "metadata": {
        "id": "pnsrsgRUWF3A",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "0991abe3-0b11-464c-fb96-2a5c7bb481ba"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "http://oeg.fi.upm.es/def/people#AssociateProfessor http://www.w3.org/2000/01/rdf-schema#subClassOf http://oeg.fi.upm.es/def/people#Professor\n",
            "http://oeg.fi.upm.es/def/people#InterimAssociateProfessor http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Class\n",
            "http://oeg.fi.upm.es/def/people#FullProfessor http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Class\n",
            "http://oeg.fi.upm.es/def/people#Professor http://www.w3.org/2000/01/rdf-schema#label Professor\n",
            "http://oeg.fi.upm.es/def/people#FullProfessor http://www.w3.org/2000/01/rdf-schema#label FullProfessor\n",
            "http://oeg.fi.upm.es/def/people#InterimAssociateProfessor http://www.w3.org/2000/01/rdf-schema#label InterimAssociateProfessor\n",
            "http://oeg.fi.upm.es/def/people#Professor http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Class\n",
            "http://oeg.fi.upm.es/def/people#AssociateProfessor http://www.w3.org/2000/01/rdf-schema#label AssociateProfessor\n",
            "http://oeg.fi.upm.es/def/people#FullProfessor http://www.w3.org/2000/01/rdf-schema#subClassOf http://oeg.fi.upm.es/def/people#Professor\n",
            "http://mydomain.org#Researcher http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Class\n",
            "http://oeg.fi.upm.es/def/people#InterimAssociateProfessor http://www.w3.org/2000/01/rdf-schema#subClassOf http://oeg.fi.upm.es/def/people#AssociateProfessor\n",
            "http://oeg.fi.upm.es/def/people#Professor http://www.w3.org/2000/01/rdf-schema#subClassOf http://oeg.fi.upm.es/def/people#Person\n",
            "http://oeg.fi.upm.es/def/people#Person http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Class\n",
            "http://oeg.fi.upm.es/def/people#Person http://www.w3.org/2000/01/rdf-schema#label Person\n",
            "http://oeg.fi.upm.es/def/people#AssociateProfessor http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Class\n"
          ]
        }
      ],
      "source": [
        "# TO DO\n",
        "#Persona\n",
        "g.add((per.Person, RDF.type, RDFS.Class))\n",
        "g.add((per.Person, RDFS.label, Literal(\"Person\", datatype=XSD.string)))\n",
        "#Profesor\n",
        "g.add((per.Professor, RDF.type, RDFS.Class))\n",
        "g.add((per.Professor, RDFS.subClassOf, per.Person))\n",
        "g.add((per.Professor, RDFS.label, Literal(\"Professor\", datatype=XSD.string)))\n",
        "#Professor COmpleto\n",
        "g.add((per.FullProfessor, RDF.type, RDFS.Class))\n",
        "g.add((per.FullProfessor, RDFS.subClassOf, per.Professor))\n",
        "g.add((per.FullProfessor, RDFS.label, Literal(\"FullProfessor\", datatype=XSD.string)))\n",
        "#Profesor Asociado\n",
        "g.add((per.AssociateProfessor, RDF.type, RDFS.Class))\n",
        "g.add((per.AssociateProfessor, RDFS.subClassOf, per.Professor))\n",
        "g.add((per.AssociateProfessor, RDFS.label, Literal(\"AssociateProfessor\", datatype=XSD.string)))\n",
        "#Profesor INterino\n",
        "g.add((per.InterimAssociateProfessor, RDF.type, RDFS.Class))\n",
        "g.add((per.InterimAssociateProfessor, RDFS.subClassOf, per.AssociateProfessor))\n",
        "g.add((per.InterimAssociateProfessor, RDFS.label, Literal(\"InterimAssociateProfessor\", datatype=XSD.string)))\n",
        "# Visualize the results\n",
        "for s, p, o in g:\n",
        "  print(s,p,o)"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Validation. Do not remove\n",
        "r.validate_task_06_01(g)"
      ],
      "metadata": {
        "id": "HdRPyusrjIuB",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "903e2013-11a1-4f1f-a818-be673e3ef670"
      },
      "execution_count": 18,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "The namespace is correct for http://oeg.fi.upm.es/def/people#Professor\n",
            "The namespace is correct for http://oeg.fi.upm.es/def/people#Person\n",
            "The namespace is correct for http://oeg.fi.upm.es/def/people#AssociateProfessor\n",
            "The namespace is correct for http://oeg.fi.upm.es/def/people#InterimAssociateProfessor\n",
            "The namespace is correct for http://oeg.fi.upm.es/def/people#FullProfessor\n",
            "Hierarchy OK\n",
            "TASK 6.1 OK\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "MXBqtBkJd22I"
      },
      "source": [
        "**TASK 6.2: Add the 3 properties shown in slide 36. Add labels for each of them (exactly as they are in the slide, with no language tags), and their corresponding domains and ranges using RDFS. Remember adding the correct datatype (xsd:String) when appropriate. If a property has no range, make it a literal (string)**"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 19,
      "metadata": {
        "id": "53hZNtXsXCNq",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "8d4dec5f-7ad2-4109-8729-4c9329e40cbd"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "http://oeg.fi.upm.es/def/people#hasColleague http://www.w3.org/2000/01/rdf-schema#label hasColleague\n",
            "http://oeg.fi.upm.es/def/people#hasName http://www.w3.org/2000/01/rdf-schema#label hasName\n",
            "http://oeg.fi.upm.es/def/people#Professor http://www.w3.org/2000/01/rdf-schema#subClassOf http://oeg.fi.upm.es/def/people#Person\n",
            "http://oeg.fi.upm.es/def/people#hasName http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/1999/02/22-rdf-syntax-ns#Property\n",
            "http://oeg.fi.upm.es/def/people#FullProfessor http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Class\n",
            "http://oeg.fi.upm.es/def/people#Professor http://www.w3.org/2000/01/rdf-schema#label Professor\n",
            "http://oeg.fi.upm.es/def/people#FullProfessor http://www.w3.org/2000/01/rdf-schema#label FullProfessor\n",
            "http://oeg.fi.upm.es/def/people#hasHomePage http://www.w3.org/2000/01/rdf-schema#label hasHomePage\n",
            "http://oeg.fi.upm.es/def/people#hasColleague http://www.w3.org/2000/01/rdf-schema#domain http://oeg.fi.upm.es/def/people#Person\n",
            "http://oeg.fi.upm.es/def/people#InterimAssociateProfessor http://www.w3.org/2000/01/rdf-schema#label InterimAssociateProfessor\n",
            "http://oeg.fi.upm.es/def/people#hasHomePage http://www.w3.org/2000/01/rdf-schema#range http://www.w3.org/2000/01/rdf-schema#Literal\n",
            "http://oeg.fi.upm.es/def/people#Professor http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Class\n",
            "http://oeg.fi.upm.es/def/people#AssociateProfessor http://www.w3.org/2000/01/rdf-schema#label AssociateProfessor\n",
            "http://oeg.fi.upm.es/def/people#hasHomePage http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/1999/02/22-rdf-syntax-ns#Property\n",
            "http://oeg.fi.upm.es/def/people#hasColleague http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/1999/02/22-rdf-syntax-ns#Property\n",
            "http://mydomain.org#Researcher http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Class\n",
            "http://oeg.fi.upm.es/def/people#hasName http://www.w3.org/2000/01/rdf-schema#range http://www.w3.org/2000/01/rdf-schema#Literal\n",
            "http://oeg.fi.upm.es/def/people#hasName http://www.w3.org/2000/01/rdf-schema#domain http://oeg.fi.upm.es/def/people#Person\n",
            "http://oeg.fi.upm.es/def/people#hasHomePage http://www.w3.org/2000/01/rdf-schema#domain http://oeg.fi.upm.es/def/people#FullProfessor\n",
            "http://oeg.fi.upm.es/def/people#InterimAssociateProfessor http://www.w3.org/2000/01/rdf-schema#subClassOf http://oeg.fi.upm.es/def/people#AssociateProfessor\n",
            "http://oeg.fi.upm.es/def/people#AssociateProfessor http://www.w3.org/2000/01/rdf-schema#subClassOf http://oeg.fi.upm.es/def/people#Professor\n",
            "http://oeg.fi.upm.es/def/people#InterimAssociateProfessor http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Class\n",
            "http://oeg.fi.upm.es/def/people#FullProfessor http://www.w3.org/2000/01/rdf-schema#subClassOf http://oeg.fi.upm.es/def/people#Professor\n",
            "http://oeg.fi.upm.es/def/people#hasColleague http://www.w3.org/2000/01/rdf-schema#range http://oeg.fi.upm.es/def/people#Person\n",
            "http://oeg.fi.upm.es/def/people#Person http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Class\n",
            "http://oeg.fi.upm.es/def/people#Person http://www.w3.org/2000/01/rdf-schema#label Person\n",
            "http://oeg.fi.upm.es/def/people#AssociateProfessor http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Class\n"
          ]
        }
      ],
      "source": [
        "# TO DO\n",
        "#Propiedad hasName\n",
        "g.add((per.hasName, RDF.type, RDF.Property))\n",
        "g.add((per.hasName, RDFS.domain, per.Person))\n",
        "g.add((per.hasName, RDFS.range, RDFS.Literal))\n",
        "g.add((per.hasName, RDFS.label, Literal(\"hasName\", datatype=XSD.string)))\n",
        "#Propiedad hasColleague\n",
        "g.add((per.hasColleague, RDF.type, RDF.Property))\n",
        "g.add((per.hasColleague, RDFS.domain, per.Person))\n",
        "g.add((per.hasColleague, RDFS.range, per.Person))\n",
        "g.add((per.hasColleague, RDFS.label, Literal(\"hasColleague\", datatype=XSD.string)))\n",
        "#Propiedad hasHomePage\n",
        "g.add((per.hasHomePage, RDF.type, RDF.Property))\n",
        "g.add((per.hasHomePage, RDFS.domain, per.FullProfessor))\n",
        "g.add((per.hasHomePage, RDFS.range, RDFS.Literal))\n",
        "g.add((per.hasHomePage, RDFS.label, Literal(\"hasHomePage\", datatype=XSD.string)))\n",
        "# Visualize the results\n",
        "for s, p, o in g:\n",
        "  print(s,p,o)"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Validation. Do not remove\n",
        "r.validate_task_06_02(g)"
      ],
      "metadata": {
        "id": "pd2mE-vGaxbu",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "bd69c351-22f1-435b-c054-f7a9e12682f5"
      },
      "execution_count": 20,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "TASK 6.2 OK\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "OGct6k7Ld9O0"
      },
      "source": [
        "**TASK 6.3: Create the individuals shown in slide 36 under \"Datos\". Link them with the same relationships shown in the diagram.\"**"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 21,
      "metadata": {
        "id": "jbMMSHSZcFcf",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "c7acbcb1-2bf2-493a-b441-248382db1c60"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "http://oeg.fi.upm.es/resource/person/Oscar http://www.w3.org/2000/01/rdf-schema#label Oscar\n",
            "http://oeg.fi.upm.es/def/people#hasColleague http://www.w3.org/2000/01/rdf-schema#label hasColleague\n",
            "http://oeg.fi.upm.es/def/people#Professor http://www.w3.org/2000/01/rdf-schema#label Professor\n",
            "http://oeg.fi.upm.es/def/people#FullProfessor http://www.w3.org/2000/01/rdf-schema#label FullProfessor\n",
            "http://oeg.fi.upm.es/def/people#hasHomePage http://www.w3.org/2000/01/rdf-schema#label hasHomePage\n",
            "http://oeg.fi.upm.es/def/people#hasColleague http://www.w3.org/2000/01/rdf-schema#domain http://oeg.fi.upm.es/def/people#Person\n",
            "http://mydomain.org#Researcher http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Class\n",
            "http://oeg.fi.upm.es/def/people#hasName http://www.w3.org/2000/01/rdf-schema#range http://www.w3.org/2000/01/rdf-schema#Literal\n",
            "http://oeg.fi.upm.es/resource/person/Asun http://oeg.fi.upm.es/def/people#hasHomePage http://www.oeg-upm.net/\n",
            "http://oeg.fi.upm.es/def/people#AssociateProfessor http://www.w3.org/2000/01/rdf-schema#subClassOf http://oeg.fi.upm.es/def/people#Professor\n",
            "http://oeg.fi.upm.es/resource/person/Asun http://oeg.fi.upm.es/def/people#hasColleague http://oeg.fi.upm.es/resource/person/Raul\n",
            "http://oeg.fi.upm.es/resource/person/Oscar http://oeg.fi.upm.es/def/people#hasColleague http://oeg.fi.upm.es/resource/person/Asun\n",
            "http://oeg.fi.upm.es/resource/person/Oscar http://oeg.fi.upm.es/def/people#hasName Oscar Corcho García\n",
            "http://oeg.fi.upm.es/def/people#FullProfessor http://www.w3.org/2000/01/rdf-schema#subClassOf http://oeg.fi.upm.es/def/people#Professor\n",
            "http://oeg.fi.upm.es/def/people#hasColleague http://www.w3.org/2000/01/rdf-schema#range http://oeg.fi.upm.es/def/people#Person\n",
            "http://oeg.fi.upm.es/resource/person/Oscar http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://oeg.fi.upm.es/def/people#AssociateProfessor\n",
            "http://oeg.fi.upm.es/def/people#Person http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Class\n",
            "http://oeg.fi.upm.es/def/people#AssociateProfessor http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Class\n",
            "http://oeg.fi.upm.es/def/people#hasName http://www.w3.org/2000/01/rdf-schema#label hasName\n",
            "http://oeg.fi.upm.es/def/people#hasName http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/1999/02/22-rdf-syntax-ns#Property\n",
            "http://oeg.fi.upm.es/def/people#FullProfessor http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Class\n",
            "http://oeg.fi.upm.es/def/people#InterimAssociateProfessor http://www.w3.org/2000/01/rdf-schema#label InterimAssociateProfessor\n",
            "http://oeg.fi.upm.es/resource/person/Asun http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://oeg.fi.upm.es/def/people#FullProfessor\n",
            "http://oeg.fi.upm.es/def/people#hasHomePage http://www.w3.org/2000/01/rdf-schema#range http://www.w3.org/2000/01/rdf-schema#Literal\n",
            "http://oeg.fi.upm.es/def/people#Professor http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Class\n",
            "http://oeg.fi.upm.es/def/people#AssociateProfessor http://www.w3.org/2000/01/rdf-schema#label AssociateProfessor\n",
            "http://oeg.fi.upm.es/def/people#hasHomePage http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/1999/02/22-rdf-syntax-ns#Property\n",
            "http://oeg.fi.upm.es/def/people#hasColleague http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/1999/02/22-rdf-syntax-ns#Property\n",
            "http://oeg.fi.upm.es/def/people#hasName http://www.w3.org/2000/01/rdf-schema#domain http://oeg.fi.upm.es/def/people#Person\n",
            "http://oeg.fi.upm.es/def/people#hasHomePage http://www.w3.org/2000/01/rdf-schema#domain http://oeg.fi.upm.es/def/people#FullProfessor\n",
            "http://oeg.fi.upm.es/def/people#InterimAssociateProfessor http://www.w3.org/2000/01/rdf-schema#subClassOf http://oeg.fi.upm.es/def/people#AssociateProfessor\n",
            "http://oeg.fi.upm.es/resource/person/Raul http://www.w3.org/2000/01/rdf-schema#label Raul\n",
            "http://oeg.fi.upm.es/def/people#InterimAssociateProfessor http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Class\n",
            "http://oeg.fi.upm.es/resource/person/Asun http://www.w3.org/2000/01/rdf-schema#label Asun\n",
            "http://oeg.fi.upm.es/def/people#Professor http://www.w3.org/2000/01/rdf-schema#subClassOf http://oeg.fi.upm.es/def/people#Person\n",
            "http://oeg.fi.upm.es/resource/person/Raul http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://oeg.fi.upm.es/def/people#InterimAssociateProfessor\n",
            "http://oeg.fi.upm.es/def/people#Person http://www.w3.org/2000/01/rdf-schema#label Person\n"
          ]
        }
      ],
      "source": [
        "# TO DO\n",
        "#Namespace\n",
        "data = Namespace(\"http://oeg.fi.upm.es/resource/person/\")\n",
        "#Oscar\n",
        "g.add((data.Oscar, RDF.type, per.AssociateProfessor))\n",
        "g.add((data.Oscar, per.hasColleague, data.Asun))\n",
        "g.add((data.Oscar, per.hasName, Literal(\"Oscar Corcho García\", datatype=XSD.string)))\n",
        "g.add((data.Oscar, RDFS.label, Literal(\"Oscar\", datatype=XSD.string)))\n",
        "#Asun\n",
        "g.add((data.Asun, RDF.type, per.FullProfessor))\n",
        "g.add((data.Asun, per.hasColleague, data.Raul))\n",
        "g.add((data.Asun, per.hasHomePage, Literal(\"http://www.oeg-upm.net/\", datatype=XSD.string)))\n",
        "g.add((data.Asun, RDFS.label, Literal(\"Asun\", datatype=XSD.string)))\n",
        "#Raul\n",
        "g.add((data.Raul, RDF.type, per.InterimAssociateProfessor))\n",
        "g.add((data.Raul, RDFS.label, Literal(\"Raul\", datatype=XSD.string)))\n",
        "# Visualize the results\n",
        "for s, p, o in g:\n",
        "  print(s,p,o)"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "r.validate_task_06_03(g)"
      ],
      "metadata": {
        "id": "-3q4Wv2EfYew",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "bf5b5a41-93d8-469d-aea1-d3416600ed3c"
      },
      "execution_count": 22,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "TASK 6.3 OK\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "tD383J__eHfV"
      },
      "source": [
        "**TASK 6.4: Add to the individual person:Oscar the email address, given and family names. Use the properties already included in example 4 to describe Jane and John (https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2025-2026/master/Assignment4/course_materials/rdf/example4.rdf). Do not import the namespaces, add them manually**\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 23,
      "metadata": {
        "id": "hWmwlAfBcgN-",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "a5f53eaa-4d3c-421d-cdf7-d2246714a5ec"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "http://oeg.fi.upm.es/resource/person/Oscar http://www.w3.org/2000/01/rdf-schema#label Oscar\n",
            "http://oeg.fi.upm.es/def/people#hasColleague http://www.w3.org/2000/01/rdf-schema#label hasColleague\n",
            "http://oeg.fi.upm.es/def/people#Professor http://www.w3.org/2000/01/rdf-schema#label Professor\n",
            "http://oeg.fi.upm.es/def/people#FullProfessor http://www.w3.org/2000/01/rdf-schema#label FullProfessor\n",
            "http://oeg.fi.upm.es/def/people#hasHomePage http://www.w3.org/2000/01/rdf-schema#label hasHomePage\n",
            "http://oeg.fi.upm.es/def/people#hasColleague http://www.w3.org/2000/01/rdf-schema#domain http://oeg.fi.upm.es/def/people#Person\n",
            "http://mydomain.org#Researcher http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Class\n",
            "http://oeg.fi.upm.es/def/people#hasName http://www.w3.org/2000/01/rdf-schema#range http://www.w3.org/2000/01/rdf-schema#Literal\n",
            "http://oeg.fi.upm.es/resource/person/Asun http://oeg.fi.upm.es/def/people#hasHomePage http://www.oeg-upm.net/\n",
            "http://xmlns.com/foaf/0.1/eamil http://www.w3.org/2000/01/rdf-schema#range http://www.w3.org/2001/XMLSchema#string\n",
            "http://oeg.fi.upm.es/def/people#AssociateProfessor http://www.w3.org/2000/01/rdf-schema#subClassOf http://oeg.fi.upm.es/def/people#Professor\n",
            "http://oeg.fi.upm.es/resource/person/Asun http://oeg.fi.upm.es/def/people#hasColleague http://oeg.fi.upm.es/resource/person/Raul\n",
            "http://oeg.fi.upm.es/resource/person/Oscar http://oeg.fi.upm.es/def/people#hasColleague http://oeg.fi.upm.es/resource/person/Asun\n",
            "http://oeg.fi.upm.es/resource/person/Oscar http://oeg.fi.upm.es/def/people#hasName Oscar Corcho García\n",
            "http://www.w3.org/2001/vcard-rdf/3.0/Given http://www.w3.org/2000/01/rdf-schema#range http://www.w3.org/2001/XMLSchema#string\n",
            "http://oeg.fi.upm.es/def/people#FullProfessor http://www.w3.org/2000/01/rdf-schema#subClassOf http://oeg.fi.upm.es/def/people#Professor\n",
            "http://oeg.fi.upm.es/resource/person/Oscar http://xmlns.com/foaf/0.1/email ocorcho@fi.upm.es\n",
            "http://oeg.fi.upm.es/def/people#hasColleague http://www.w3.org/2000/01/rdf-schema#range http://oeg.fi.upm.es/def/people#Person\n",
            "http://oeg.fi.upm.es/resource/person/Oscar http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://oeg.fi.upm.es/def/people#AssociateProfessor\n",
            "http://oeg.fi.upm.es/def/people#Person http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Class\n",
            "http://oeg.fi.upm.es/resource/person/Oscar http://www.w3.org/2001/vcard-rdf/3.0/Given Oscar\n",
            "http://oeg.fi.upm.es/def/people#AssociateProfessor http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Class\n",
            "http://www.w3.org/2001/vcard-rdf/3.0/Given http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/1999/02/22-rdf-syntax-ns#Property\n",
            "http://www.w3.org/2001/vcard-rdf/3.0/Family http://www.w3.org/2000/01/rdf-schema#range http://www.w3.org/2001/XMLSchema#string\n",
            "http://oeg.fi.upm.es/def/people#hasName http://www.w3.org/2000/01/rdf-schema#label hasName\n",
            "http://xmlns.com/foaf/0.1/email http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Datatype\n",
            "http://oeg.fi.upm.es/def/people#hasName http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/1999/02/22-rdf-syntax-ns#Property\n",
            "http://oeg.fi.upm.es/def/people#FullProfessor http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Class\n",
            "http://oeg.fi.upm.es/def/people#InterimAssociateProfessor http://www.w3.org/2000/01/rdf-schema#label InterimAssociateProfessor\n",
            "http://oeg.fi.upm.es/resource/person/Asun http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://oeg.fi.upm.es/def/people#FullProfessor\n",
            "http://oeg.fi.upm.es/def/people#hasHomePage http://www.w3.org/2000/01/rdf-schema#range http://www.w3.org/2000/01/rdf-schema#Literal\n",
            "http://oeg.fi.upm.es/def/people#Professor http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Class\n",
            "http://oeg.fi.upm.es/def/people#AssociateProfessor http://www.w3.org/2000/01/rdf-schema#label AssociateProfessor\n",
            "http://oeg.fi.upm.es/def/people#hasHomePage http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/1999/02/22-rdf-syntax-ns#Property\n",
            "http://oeg.fi.upm.es/def/people#hasColleague http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/1999/02/22-rdf-syntax-ns#Property\n",
            "http://oeg.fi.upm.es/def/people#hasName http://www.w3.org/2000/01/rdf-schema#domain http://oeg.fi.upm.es/def/people#Person\n",
            "http://oeg.fi.upm.es/def/people#hasHomePage http://www.w3.org/2000/01/rdf-schema#domain http://oeg.fi.upm.es/def/people#FullProfessor\n",
            "http://oeg.fi.upm.es/def/people#InterimAssociateProfessor http://www.w3.org/2000/01/rdf-schema#subClassOf http://oeg.fi.upm.es/def/people#AssociateProfessor\n",
            "http://www.w3.org/2001/vcard-rdf/3.0/Family http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/1999/02/22-rdf-syntax-ns#Property\n",
            "http://oeg.fi.upm.es/resource/person/Oscar http://www.w3.org/2001/vcard-rdf/3.0/Family Corcho García\n",
            "http://oeg.fi.upm.es/resource/person/Raul http://www.w3.org/2000/01/rdf-schema#label Raul\n",
            "http://oeg.fi.upm.es/def/people#InterimAssociateProfessor http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://www.w3.org/2000/01/rdf-schema#Class\n",
            "http://oeg.fi.upm.es/resource/person/Asun http://www.w3.org/2000/01/rdf-schema#label Asun\n",
            "http://oeg.fi.upm.es/def/people#Professor http://www.w3.org/2000/01/rdf-schema#subClassOf http://oeg.fi.upm.es/def/people#Person\n",
            "http://oeg.fi.upm.es/resource/person/Raul http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://oeg.fi.upm.es/def/people#InterimAssociateProfessor\n",
            "http://oeg.fi.upm.es/def/people#Person http://www.w3.org/2000/01/rdf-schema#label Person\n"
          ]
        }
      ],
      "source": [
        "# TO DO\n",
        "#Namespace\n",
        "foaf = Namespace(\"http://xmlns.com/foaf/0.1/\")\n",
        "vcard = Namespace(\"http://www.w3.org/2001/vcard-rdf/3.0/\")\n",
        "#Nuevas relaciones\n",
        "g.add((vcard.Family, RDF.type, RDF.Property))\n",
        "g.add((vcard.Family, RDFS.range, XSD.string))\n",
        "g.add((vcard.Given, RDF.type, RDF.Property))\n",
        "g.add((vcard.Given, RDFS.range, XSD.string))\n",
        "g.add((foaf.email, RDF.type, RDFS.Datatype))\n",
        "g.add((foaf.eamil, RDFS.range, XSD.string))\n",
        "#Más info de Oscar\n",
        "g.add((data.Oscar, vcard.Given, Literal(\"Oscar\", datatype=XSD.string)))\n",
        "g.add((data.Oscar, vcard.Family, Literal(\"Corcho García\", datatype=XSD.string)))\n",
        "g.add((data.Oscar, foaf.email, Literal(\"ocorcho@fi.upm.es\", datatype=XSD.string)))\n",
        "# Visualize the results\n",
        "for s, p, o in g:\n",
        "  print(s,p,o)"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Validation. Do not remove\n",
        "r.validate_task_06_04(g)\n",
        "r.save_report(\"_Task_06\")"
      ],
      "metadata": {
        "id": "Y1NiIQMyfgyF",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "39343cb6-9199-47f8-ceef-f93e3579465c"
      },
      "execution_count": 25,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "TASK 6.4 OK\n"
          ]
        }
      ]
    }
  ],
  "metadata": {
    "colab": {
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3 (ipykernel)",
      "language": "python",
      "name": "python3"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.9.5"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}