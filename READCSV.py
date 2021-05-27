import csv
import webbrowser
def leercsv():
    with open('filecsv.csv', newline='') as File:
        print("ESTRUCTURA CSV", type(File))
        reader = csv.reader(File)
        for row in reader:
            print(row)

def reportarcsv():
    htmFile = open("reportecsv.html", "w")
    htmFile.write("""<!DOCTYPE HTML PUBLIC"
    <html>
    <head>
        <title>REPORTE CSV</title>
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

    with open('filecsv.csv', newline='') as File:
        reader = csv.reader(File)
        contenido = ""
        contador = 0
        for row in reader:
            if contador == 0:
                contador = 1
            elif contador == 1:
                contenido += (" <tbody>" "<td>" + row[0] + "</td>"
                                         "<td>" + row[1] + "</td>"
                                         "<td>" + row[2] + "</td>"
                                         "<td>" + row[3] + "</td>"
                                "</tbody>")

    htmFile.write(contenido)

    htmFile.write("""
  </table>
</div>
    </body>
    </html>""")

    htmFile.close
    webbrowser.open_new_tab('reportecsv.html')