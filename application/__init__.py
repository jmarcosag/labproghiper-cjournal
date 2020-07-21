from flask import Flask
import os
from application.model.entity.estado import Estado
from application.model.entity.noticia import Noticia


app = Flask(__name__, static_folder=os.path.abspath("application/view/static"), template_folder=os.path.abspath("application/view/templates"))

exnot1 = Noticia(1, "exemplotitulo", "exemplotexto", "img/", "video/", "Rio de Janeiro", "17/20")
listaNot = [exnot1]

exest1 = Estado(1,"Rio de Janeiro", "RJ", 'img/', [exnot1])
listaEst = [exest1]


