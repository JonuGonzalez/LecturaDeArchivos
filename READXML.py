from xml.dom import minidom
doc = minidom.parse("filexml.xml")
print("ESTRUCTURA XML", type(doc))
PERSONAS = doc.getElementsByTagName("PERSONAS")
def leerxml():
    for i in range(4):
        for PERSONA in PERSONAS:
            NOMBRE = PERSONA.getElementsByTagName("NOMBRE")[i]
            EDAD = PERSONA.getElementsByTagName("EDAD")[i]
            GENERO = PERSONA.getElementsByTagName("GENERO")[i]
            PROFESION = PERSONA.getElementsByTagName("PROFESION")[i]
            print("NOMBRE:%s" % NOMBRE.firstChild.data)
            print("EDAD:%s" % EDAD.firstChild.data)
            print("GENERO:%s" % GENERO.firstChild.data)
            print("PROFESION:%s" % PROFESION.firstChild.data)
