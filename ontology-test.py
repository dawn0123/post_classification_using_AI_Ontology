from rdflib import Graph, Namespace, URIRef
from rdflib.namespace import OWL

# Load the ontology file
g = Graph()
g.parse("Ontology-Sep2023.owl", format="xml")  # Replace "your_ontology.owl" with your ontology file path

# # Define the OWL and RDFS namespaces
# OWL = Namespace("http://www.w3.org/2002/07/owl#")
# RDFS = Namespace("http://www.w3.org/2000/01/rdf-schema#")

# # Query for all classes and labels
# query = """
#     SELECT ?class ?label
#     WHERE {
#         ?class a owl:Class .
#         ?class rdfs:label ?label .
#     }
# """

# # Execute the query
# results = g.query(query, initNs={"owl": OWL, "rdfs": RDFS})

# print('num =', len(results))

# with open('ontology_classes.txt', 'w', encoding='utf-8') as f:
    
#     # Print the classes and labels
#     for i, row in enumerate(results):
#         f.write(row['class'])
#         f.write(',')
#         f.write(row['label'])
#         f.write('\n')

# from rdflib import Graph

# # Load the ontology file
# g = Graph()
# g.parse("Ontology-Sep2023.owl", format="xml")  # Replace with the path to your ontology file and its format

# # Define the URI or name of the class you want to find equal classes for
# class_uri = "http://www.semanticweb.org/OntoOCD#Intrusive_Thoughts"  # Replace with the URI or name of your class

# # Find equal classes
# query = f"""
#     SELECT ?equalClass
#     WHERE {{
#         ?equalClass owl:equivalentClass <{class_uri}> .
#     }}
# """

# initNs = dict(
#     base="http://www.semanticweb.org/OntoOCD",
#     dc="http://purl.org/dc/elements/1.1/",
#     obo="http://purl.obolibrary.org/obo/",
#     owl="http://www.w3.org/2002/07/owl#",
#     rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#",
#     xml="http://www.w3.org/XML/1998/namespace",
#     xsd="http://www.w3.org/2001/XMLSchema#",
#     cito="http://purl.org/spar/cito/",
#     core="http://purl.obolibrary.org/obo/uberon/core#",
#     doap="http://usefulinc.com/ns/doap#",
#     foaf="http://xmlns.com/foaf/0.1/",
#     gold="http://purl.org/linguistics/gold/",
#     rdfs="http://www.w3.org/2000/01/rdf-schema#",
#     skos="http://www.w3.org/2004/02/skos/core#",
#     wiki="https://www.wikidata.org/wiki/",
#     gold1="http://linguistics-ontology.org/gold/2010/",
#     swrla="http://swrl.stanford.edu/ontologies/3.3/swrla.owl#",
#     terms="http://purl.org/dc/terms/",
#     schema="https://schema.org/",
#     protege="http://protege.stanford.edu/plugins/owl/protege#",
#     subsets="http://purl.obolibrary.org/obo/ro/subsets#",
#     Property="https://www.wikidata.org/wiki/Property:",
#     oboInOwl="http://www.geneontology.org/formats/oboInOwl#",
#     ace_lexicon="http://attempto.ifi.uzh.ch/ace_lexicon#",
#     owlready_ontology="http://www.lesfleursdunormal.fr/static/_downloads/owlready_ontology.owl#"
# )

# results = g.query(query, initNs=initNs)

# print('nums = ', len(results))
# # Print the equal classes
# for row in results:
#     print(f"Equal Class: {row['equalClass']}")

# a = eval(
# "['depression', 'weight gain', 'Medication', 'anxiety', 'anxiety', 'hope', 'obsession', 'bathroom', 'Thought', 'OCD']")

# for label in a:
#     # Query for the class with the label "weight gain"
#     query = ''.join([
#         "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>\n",
#         "SELECT ?class WHERE {\n",
#         "    ?class rdfs:label ?label .\n",
#         '    FILTER (str(?label) = "{}")\n'.format(label),
#         "}"
#     ])

#     # Execute the SPARQL query
#     results = g.query(query)
#     print('nums = ', len(results))

#     # Process the results
#     for row in results:
#         class_uri = row["class"]
#         print('label', label, 'class', class_uri)

# from rdflib import Graph, URIRef
from rdflib.plugins.sparql import prepareQuery

OCD_classes = [
    'http://www.semanticweb.org/OntoOCD#Aggressive_Obsession',
    'http://www.semanticweb.org/OntoOCD#Aggressive_Thought',
    'http://www.semanticweb.org/OntoOCD#Avoidance_Behavior',
    'http://www.semanticweb.org/OntoOCD#Checking',
    'http://www.semanticweb.org/OntoOCD#Compulsion',
    'http://www.semanticweb.org/OntoOCD#Contamination_Obsession',
    'http://www.semanticweb.org/OntoOCD#Contamination_Thought',
    'http://www.semanticweb.org/OntoOCD#Counting',
    'http://www.semanticweb.org/OntoOCD#Doubt_Obsession',
    'http://www.semanticweb.org/OntoOCD#Doubt_Thought',
    'http://www.semanticweb.org/OntoOCD#Impairment',
    'http://www.semanticweb.org/OntoOCD#Hoarding_Obsession',
    'http://www.semanticweb.org/OntoOCD#Hoarding_Thought',
    'http://www.semanticweb.org/OntoOCD#Hypervigilance_Behavior',
    'http://www.semanticweb.org/OntoOCD#Intrusive_Thoughts',
    'http://www.semanticweb.org/OntoOCD#Mental_Image',
    'http://www.semanticweb.org/OntoOCD#Obsession',
    'http://www.semanticweb.org/OntoOCD#Reassurance_Behavior',
    'http://www.semanticweb.org/OntoOCD#Religious_Obsession',
    'http://www.semanticweb.org/OntoOCD#Religious_Thought',
    'http://www.semanticweb.org/OntoOCD#Repeating_Rituals',
    'http://www.semanticweb.org/OntoOCD#Sexual_Obsession',
    'http://www.semanticweb.org/OntoOCD#Somatic_Obsession',
    'http://www.semanticweb.org/OntoOCD#Somatic_Thought',
    'http://www.semanticweb.org/OntoOCD#Symmetry_Obsession',
    'http://www.semanticweb.org/OntoOCD#Symmetry_Thought',
    'http://www.semanticweb.org/OntoOCD#Thought',
    'http://www.semanticweb.org/OntoOCD#Urge',
]

OCD_labels = [c.split('#')[-1].replace('_', ' ').lower() for c in OCD_classes]

def find_classes_with_label(label):

    query = prepareQuery('''
        SELECT ?class ?label
        WHERE {
            ?class rdfs:label ?label .
            FILTER (str(?label) = "%s")
        }
    ''' % label, initNs={"rdfs": "http://www.w3.org/2000/01/rdf-schema#"})

    classes = []
    for row in g.query(query):
        classes.append((row['class'], row['label']))

    if label in OCD_labels:
        classes.append((f'<{OCD_classes[OCD_labels.index(label)]}>', label))

    return classes

def find_equivalent_and_subclasses(class_uri):

    try:
        cu = class_uri.n3()
    except:
        cu = class_uri

    query = prepareQuery('''
        SELECT ?subclass ?label
        WHERE {
            { ?subclass owl:equivalentClass* %s }
            UNION
            { %s owl:equivalentClass* ?subclass }
            UNION
            { ?subclass rdfs:subClassOf* %s }
            ?subclass rdfs:label ?label
        }
    ''' % (cu, cu, cu), 
        initNs={
            "owl": "http://www.w3.org/2002/07/owl#", 
            "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
            "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
            })

    subclasses = []
    for row in g.query(query):
        cl = str(row['subclass'])
        if cl in OCD_classes:
            label = OCD_labels[OCD_classes.index(cl)]
        else:
            label = row['label']
        subclasses.append((cl, label))

    return subclasses

def get_equivalent_classes(class_uri):
    try:
        cu = class_uri.n3()
    except:
        cu = class_uri

    query = """
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

    SELECT ?class ?label
    WHERE {
        %s owl:equivalentClass ?equivalentClass .
        {
            ?equivalentClass owl:unionOf/rdf:rest*/rdf:first ?class .
        }
        UNION
        {
            ?equivalentClass owl:unionOf ?collection .
            ?collection rdf:parseType "Collection" .
            ?collection rdf:rest*/rdf:first ?class .
        }
        ?class rdfs:label ?label
    }
    """ % (cu,)

    equiclasses = []
    results = g.query(query)
    for row in results:
        cl = row['class']
        if cl in OCD_classes:
            label = OCD_labels[OCD_classes.index(cl)]
        else:
            label = row['label']
        equiclasses.append((cl, label))

    return equiclasses


label = "intrusive thoughts"
classes = find_classes_with_label(label)
if len(classes) == 0:
    print("No class found with label '%s'" % label)
else:
    for class_uri, class_label in classes:
        # subclasses = get_equivalent_classes(class_uri)
        subclasses = find_equivalent_and_subclasses(class_uri)
        print("Class '%s' (%s) has the following equivalent and sub-classes:" % (class_uri, class_label))
        for subclass_uri, subclass_label in subclasses:
            print("- Class '%s' (%s)" % (subclass_uri, subclass_label))