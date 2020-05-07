from  django.http import HttpResponse

def saludo(request): 

    titulo="""<html>  
    <body>
    <h1>
    Hola esta es la prueba para PythonAnywhere
    </h1>
    </body>
    </html>"""
    
    return HttpResponse(titulo)
    