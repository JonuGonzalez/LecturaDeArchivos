from xml.dom import minidom
import webbrowser
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
def reportarxml():
    htmFile = open("reportexml.html", "w")
    htmFile.write("""<!DOCTYPE HTML PUBLIC"
    <html>
    <head>
        <title>REPORTE XML</title>
     <meta charset="utf-5">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    
    <style type="text/css">
            body{
                background-color: #474D5A;
            }
            div#reporte {
                width: 60%;
                height: 98%;
                border:solid black;	
                background-color: #B1B7C4;
                margin: 20%;
                margin-top: 0;
                border-radius: 50px;
            }
            div#titulo{
                background-color: black;
                border:solid black;
                border-radius: 50px;
                height:10%;
            }
            h1{
                font-family: arial,helvetica;
                color: white;
            }
            h4{
                font-family: arial,helvetica;
                color: black;
            }
            h5{
                font-family: arial,helvetica;
                color: black;
            }
        </style>
    </head>
    <body>
        <div id="reporte">
            <div id="titulo">
                <center>
                    <h1>Reporte  Jonathan González</h1>
                </center>
            </div>
            <center>
                <h4>
                    Registros Seleccionados	
                </h4>            
  <table class="table">
    <thead>
      <tr>
       <th>Nombre</th>
        <th>Edad</th>
        <th>Genero</th>
        <th>Profesion</th>
      </tr>
    </thead>
    """)
    contenido = ""
    for i in range(4):
        for PERSONA in PERSONAS:
            NOMBRE = PERSONA.getElementsByTagName("NOMBRE")[i]
            EDAD = PERSONA.getElementsByTagName("EDAD")[i]
            GENERO = PERSONA.getElementsByTagName("GENERO")[i]
            PROFESION = PERSONA.getElementsByTagName("PROFESION")[i]
            contenido += (" <tbody>" "<td>" + NOMBRE.firstChild.data + 
                            "</td>"  "<td>" + EDAD.firstChild.data + 
                            "</td>"  "<td>" + GENERO.firstChild.data + 
                            "</td>"  "<td>" + PROFESION.firstChild.data + 
                            "</td>"  "</tbody>")
    htmFile.write(contenido)
    htmFile.write("""
  </table>
</div>
    </body>
    </html>""")

    htmFile.close
    webbrowser.open_new_tab('reportexml.html')
