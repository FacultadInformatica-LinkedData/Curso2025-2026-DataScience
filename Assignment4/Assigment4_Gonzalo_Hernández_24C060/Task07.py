{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/gonzahv24/Curso2025-2026-DataScience/blob/master/Assignment4/Assigment4_Gonzalo_Hern%C3%A1ndez_24C060/Task07.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "nOOPLCHF7hLB"
      },
      "source": [
        "**Task 07: Querying RDF(s)**"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 35,
      "metadata": {
        "id": "Yl9npCt8n6m-",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "6048b058-a425-482b-e893-d08cabde2dba"
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
      "cell_type": "code",
      "source": [
        "from validation import Report"
      ],
      "metadata": {
        "id": "FmnGjffDT92V"
      },
      "execution_count": 36,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "XY7aPc86Bqoo"
      },
      "source": [
        "First let's read the RDF file"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 37,
      "metadata": {
        "id": "9ERh415on7kF"
      },
      "outputs": [],
      "source": [
        "from rdflib import Graph, Namespace, Literal\n",
        "from rdflib.namespace import RDF, RDFS\n",
        "# Do not change the name of the variables\n",
        "g = Graph()\n",
        "g.namespace_manager.bind('ns', Namespace(\"http://somewhere#\"), override=False)\n",
        "g.parse(github_storage+\"/rdf/data06.ttl\", format=\"TTL\")\n",
        "report = Report()"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "qp1oe2Eddsvo"
      },
      "source": [
        "**TASK 7.1a: For all classes, list each classURI. If the class belogs to another class, then list its superclass.**\n",
        "**Do the exercise in RDFLib returning a list of Tuples: (class, superclass) called \"result\". If a class does not have a super class, then return None as the superclass**"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 38,
      "metadata": {
        "id": "tRcSWuMHOXBl",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "5a78292b-bf5c-4e7a-c205-fa060666a05c"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "(rdflib.term.URIRef('http://oeg.fi.upm.es/def/people#Person'), None)\n",
            "(rdflib.term.URIRef('http://oeg.fi.upm.es/def/people#Animal'), None)\n",
            "(rdflib.term.URIRef('http://oeg.fi.upm.es/def/people#Professor'), rdflib.term.URIRef('http://oeg.fi.upm.es/def/people#Person'))\n",
            "(rdflib.term.URIRef('http://oeg.fi.upm.es/def/people#Student'), rdflib.term.URIRef('http://oeg.fi.upm.es/def/people#Person'))\n",
            "(rdflib.term.URIRef('http://oeg.fi.upm.es/def/people#FullProfessor'), rdflib.term.URIRef('http://oeg.fi.upm.es/def/people#Professor'))\n",
            "(rdflib.term.URIRef('http://oeg.fi.upm.es/def/people#AssociateProfessor'), rdflib.term.URIRef('http://oeg.fi.upm.es/def/people#Professor'))\n",
            "(rdflib.term.URIRef('http://oeg.fi.upm.es/def/people#InterimAssociateProfessor'), rdflib.term.URIRef('http://oeg.fi.upm.es/def/people#AssociateProfessor'))\n"
          ]
        }
      ],
      "source": [
        "# TO DO\n",
        "#Lista classUri\n",
        "result=[]\n",
        "for sb in g.subjects(RDF.type, RDFS.Class):\n",
        "  sc=None\n",
        "  for Sc in g.objects(sb,RDFS.subClassOf):\n",
        "    sc=Sc\n",
        "  result.append((sb,sc))\n",
        "for cl, sc in result:\n",
        "   short_c = g.namespace_manager.normalizeUri(cl)\n",
        "   short_sc = g.namespace_manager.normalizeUri(sc) if sc else None\n",
        "for r in result:\n",
        "  print(r)"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "## Validation: Do not remove\n",
        "report.validate_07_1a(result)"
      ],
      "metadata": {
        "id": "uvEpQQrTlMPH",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "a3263309-6ed8-4115-a52c-a4fc5f313e7d"
      },
      "execution_count": 39,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "TASK 7.1a OK\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**TASK 7.1b: Repeat the same exercise in SPARQL, returning the variables ?c (class) and ?sc (superclass)**"
      ],
      "metadata": {
        "id": "kbY-jqw6klr9"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "query =  \"Select ?c ?sc WHERE {?c rdf:type rdfs:Class. OPTIONAL {?c rdfs:subClassOf ?sc.}}\"\n",
        "\n",
        "for r in g.query(query):\n",
        "  print(r.c, r.sc)\n"
      ],
      "metadata": {
        "id": "NGAG7l9UklMC",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "911fc9bf-649b-4e26-b505-e570aaaf6f3d"
      },
      "execution_count": 40,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "http://oeg.fi.upm.es/def/people#Person None\n",
            "http://oeg.fi.upm.es/def/people#Animal None\n",
            "http://oeg.fi.upm.es/def/people#Professor http://oeg.fi.upm.es/def/people#Person\n",
            "http://oeg.fi.upm.es/def/people#Student http://oeg.fi.upm.es/def/people#Person\n",
            "http://oeg.fi.upm.es/def/people#FullProfessor http://oeg.fi.upm.es/def/people#Professor\n",
            "http://oeg.fi.upm.es/def/people#AssociateProfessor http://oeg.fi.upm.es/def/people#Professor\n",
            "http://oeg.fi.upm.es/def/people#InterimAssociateProfessor http://oeg.fi.upm.es/def/people#AssociateProfessor\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "## Validation: Do not remove\n",
        "report.validate_07_1b(query,g)"
      ],
      "metadata": {
        "id": "9zf4vgVHlKR3",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "fe8922de-8c50-4c09-a02c-878d8331817c"
      },
      "execution_count": 41,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "TASK 7.1b OK\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "gM3DASkTQQ5Y"
      },
      "source": [
        "**TASK 7.2a: List all individuals of \"Person\" with RDFLib (remember the subClasses). Return the individual URIs in a list called \"individuals\"**\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 42,
      "metadata": {
        "id": "LiKSPHRzS-XJ",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "ca690103-c288-4cd5-e1e5-915db0971675"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "http://oeg.fi.upm.es/def/people#Asun\n",
            "http://oeg.fi.upm.es/def/people#Oscar\n",
            "http://oeg.fi.upm.es/def/people#Raul\n"
          ]
        }
      ],
      "source": [
        "ns = Namespace(\"http://oeg.fi.upm.es/def/people#\")\n",
        "\n",
        "# variable to return\n",
        "individuals = []\n",
        "def subclases(cl):\n",
        "  sb=[]\n",
        "  for s,p,o in g.triples((None,RDFS.subClassOf,cl)):\n",
        "    sb.append(s)\n",
        "    sb += subclases(s)\n",
        "  return sb\n",
        "clases= subclases(ns.Person)\n",
        "clases.append(ns.Person)\n",
        "for cl in clases:\n",
        "  for s,p,o in g.triples((None,RDF.type,cl)):\n",
        "    individuals.append(s)\n",
        "# visualize results\n",
        "for i in individuals:\n",
        "  print(i)"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# validation. Do not remove\n",
        "report.validate_07_02a(individuals)"
      ],
      "metadata": {
        "id": "ONrAls5uiX1G",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "6de60947-5fec-4cd1-f11e-184cbb99538a"
      },
      "execution_count": 43,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "TASK 7.2a OK\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**TASK 7.2b: Repeat the same exercise in SPARQL, returning the individual URIs in a variable ?ind**"
      ],
      "metadata": {
        "id": "up-952A-za7A"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "query =  \"SELECT ?ind WHERE{?c rdfs:subClassOf* <http://oeg.fi.upm.es/def/people#Person>. ?ind a ?c}\"\n",
        "\n",
        "for r in g.query(query):\n",
        "  print(r.ind)\n",
        "# Visualize the results"
      ],
      "metadata": {
        "id": "ipYiEVbTzbR0",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "5bd40168-4205-4e6e-95b1-1a40c701f64d"
      },
      "execution_count": 44,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "http://oeg.fi.upm.es/def/people#Asun\n",
            "http://oeg.fi.upm.es/def/people#Oscar\n",
            "http://oeg.fi.upm.es/def/people#Raul\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "## Validation: Do not remove\n",
        "report.validate_07_02b(g, query)"
      ],
      "metadata": {
        "id": "s-Hu2LxRjUQt",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "40f2fb8d-714b-4c9d-da6d-6aa256068f6b"
      },
      "execution_count": 45,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "TASK 7.2b OK\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**TASK 7.3:  List the name and type of those who know Rocky (in SPARQL only). Use name and type as variables in the query**"
      ],
      "metadata": {
        "id": "3NyI7M2VNr9R"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "query =  \"\"\"SELECT ?name ?type WHERE{\n",
        "  ?name <http://oeg.fi.upm.es/def/people#knows> <http://oeg.fi.upm.es/def/people#Rocky>.\n",
        "  ?name rdf:type ?type.}\"\"\"\n",
        "# TO DO\n",
        "# Visualize the results\n",
        "for r in g.query(query):\n",
        "  print(r.name, r.type)\n"
      ],
      "metadata": {
        "id": "I_CNoIKdNpbx",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "b8b6082d-6242-49b0-f167-62c2b8303205"
      },
      "execution_count": 46,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "http://oeg.fi.upm.es/def/people#Asun http://oeg.fi.upm.es/def/people#FullProfessor\n",
            "http://oeg.fi.upm.es/def/people#Raul http://oeg.fi.upm.es/def/people#InterimAssociateProfessor\n",
            "http://oeg.fi.upm.es/def/people#Fantasma http://oeg.fi.upm.es/def/people#Animal\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "## Validation: Do not remove\n",
        "report.validate_07_03(g, query)"
      ],
      "metadata": {
        "id": "Zf3JS7tEhS2t",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "48c53bb4-bde3-45ef-e1a5-bafa4eb06b0f"
      },
      "execution_count": 47,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "TASK 7.3 OK\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Task 7.4: List the name of those entities who have a colleague with a dog, or that have a collegue who has a colleague who has a dog (in SPARQL). Return the results in a variable called name**"
      ],
      "metadata": {
        "id": "kyjGsyxDPa2C"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "query =  \"\"\"\n",
        "PREFIX people: <http://oeg.fi.upm.es/def/people#>\n",
        "Select ?name WHERE{\n",
        "  { ?name people:hasColleague ?c1.\n",
        "    ?c1 people:ownsPet ?dog.}\n",
        "    UNION{\n",
        "    ?name people:hasColleague ?c2.\n",
        "    ?c2 people:hasColleague ?c3.\n",
        "    ?c3 people:ownsPet ?dog.}\n",
        "  }\n",
        "\"\"\"\n",
        "\n",
        "for r in g.query(query):\n",
        "  print(r.name)\n",
        "\n",
        "# TO DO\n",
        "# Visualize the results"
      ],
      "metadata": {
        "id": "yoVwVZUAPaLm",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "835ead6c-de3c-4c52-f709-eebbf4888938"
      },
      "execution_count": 48,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "http://oeg.fi.upm.es/def/people#Asun\n",
            "http://oeg.fi.upm.es/def/people#Oscar\n",
            "http://oeg.fi.upm.es/def/people#Raul\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "## Validation: Do not remove\n",
        "report.validate_07_04(g,query)\n",
        "report.save_report(\"_Task_07\")"
      ],
      "metadata": {
        "id": "zcTZE7ngj2fc",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "f750091a-c97f-4f31-fd96-e2827aac782e"
      },
      "execution_count": 51,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "TASK 7.4 OK\n"
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