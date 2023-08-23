import random
import winsound
from colorama import init, Fore, Back, Style
init(autoreset=True)
ro = Fore.RED
ve = Fore.GREEN
am = Fore.YELLOW
az = Fore.BLUE
ma = Fore.MAGENTA
cy = Fore.CYAN

class Item:
    nombre="item"
    cantidad = 0
    tipo="comida"
    valor =0
    rareza ="z"

    def conseguir_item(self,n):
        i= Item()
        if(n== "moneda"):
            i.nombre = n
            i.tipo = "dinero"

        elif(n== "piel de lobo"):
            i.nombre = n
            i.tipo = "material"
            i.valor = 10
            i.rareza = "x"
        
        elif n =="pergamino alma de lobo":
            i.nombre = n
            i.tipo = "material"
            i.valor = 1000
            i.rareza = "c"

        elif n == "corazon de lobo":
            i.nombre = n
            i.tipo = "material"
            i.valor = 200
            i.rareza = "e"

        elif n == "garra de lobo":
            i.nombre = n
            i.tipo = "material"
            i.valor = 10
            i.rareza = "x"
        
        return i
            

class Evento_del_mundo:
    nombre= "evento llamado"
    tipo = "muerte"
    personaje ="P1"
    cantidad=0

class Movimiento:
    tipo ="Caminar hacia"
    tiempo_consumido= 10

class Deseos:
    deseo ="muerte del rey demoño"
    estado =False

class Profesion:
    nombre= "vagabundo"
    nivel =1

class Lugar:
    def __init__(self):
        self.lista_edificios = list()
        self.lista_items = list()
    nombre ="Ciudad"
    lista_edificios = list()

class Edificio:
    def __init__(self):
        self.lista_personajes = list()
    nombre="Edificio"
    tipo ="Tienda"
    lista_items = list()
    lista_personajes = list()

    def revisar_cofre(self):
        return self.lista_items

class Equipamento(Item):
    defensa_fisica=0
    defensa_magica=0

class Arma(Item):
    ataque_fisico=0
    ataque_magico=0
    critico=0

    def Obtener_arma(self, nombre):
        a = Arma()
        if(nombre == "Daga Oxidada"):
            a.nombre = nombre
            a.tipo ="Daga Arma Fisica"
            a.ataque_fisico = 5
            a.ataque_magico =1
            return a
        
    def print_arma(self):
        print(f"{self.tipo}: {self.nombre}, Poder fisico: {self.ataque_fisico},Poder magico: {self.ataque_magico}")

class Habilidad:
    nombre =""
    tipo =""
    costo_mana =0
    enfriamiento =0
    multiplicador =1

    #Usar una habilidad
    def Usar(self, usuario, objetivo):
        print(f"{usuario.nombre} usa: {self.nombre} sobre: {objetivo.nombre}")

        if self.tipo =="ataque_fisico":
            daño = (usuario.poder_fisico * self.multiplicador)*(objetivo.defensa_fisica)
            objetivo.vida -= daño

            print(f"causandole {daño} de daño fisico")
            
            print_1_espacio()

            objetivo.print_efecto_de_habilidad()
           
        elif self.tipo =="curacion":
            cura = usuario.poder_magico * self.multiplicador
            objetivo.vida += cura

            objetivo.print_efecto_de_habilidad()
        else:
            print("Error, tipo de habilidad no existe.")


    def ObtenerHabilidad(nombre):
        h = Habilidad()
        if nombre == "Puñetazo":
            h.nombre =nombre
            h.tipo ="ataque_fisico"
            h.costo_mana =1
            h.enfriamiento =1
            h.multiplicador =1
            return h
        elif nombre == "Embestida":
            h.nombre =nombre
            h.tipo ="ataque_fisico"
            h.costo_mana =1
            h.enfriamiento =1
            h.multiplicador =1
            return h
        elif nombre == "Garras":
            h.nombre =nombre
            h.tipo ="ataque_fisico"
            h.costo_mana =2
            h.enfriamiento =1
            h.multiplicador =1.1
            return h
        elif nombre == "Mordida":
            h.nombre =nombre
            h.tipo ="ataque_fisico"
            h.costo_mana =2
            h.enfriamiento =1
            h.multiplicador =1.2
            return h
        elif nombre == "curacion 1":
            h.nombre =nombre
            h.tipo ="curacion"
            h.costo_mana =2
            h.enfriamiento =1
            h.multiplicador =5
            return h
        elif nombre == "Garrotazo":
            h.nombre =nombre
            h.tipo ="ataque_fisico"
            h.costo_mana =4
            h.enfriamiento =2
            h.multiplicador =1.3
            return h
        elif nombre == "Patada":
            h.nombre =nombre
            h.tipo ="ataque_fisico"
            h.costo_mana =4
            h.enfriamiento =2
            h.multiplicador =1.3
            return h
        elif nombre == "Super Mordida":
            h.nombre =nombre
            h.tipo ="ataque_fisico"
            h.costo_mana =10
            h.enfriamiento =1
            h.multiplicador =1.4
            return h
        else:
            print("Error, Habilidad no encontrada.")

class Personaje:
    def __init__(self):
        self.lista_cosas_que_me_gustan = list()
        self.lisa_profesiones = list()
        self.lista_cosas_que_odio = list()
        self.lista_deseos = list()
        self.lista_eventos_que_odio = list()
        self.lista_habilidades = list()
        self.lista_subditos = list()

    nombre=""
    tipo =""
    vida_maxima =100
    vida=0
    mana_maximo =100
    mana =0
    dinero =0
    nivel =1
    experiencia =10
    poder_fisico =0
    poder_magico =0
    defensa_fisica =0
    defensa_magica =0
    velocidad =0
    suerte = 0
    lista_habilidades= list()
    lisa_profesiones = list()
    #Equipamento
    casco = Equipamento()
    pecho = Equipamento()
    pantalones = Equipamento()
    botas = Equipamento()
    habilidad_set = ""
    arma = Arma()
    #list<Item>()
    inventario = list()
    tipo_especial = "esclavo"
    #0 es cuando su hambre está al maximo
    hambre = 100
    #MODIFICAR ESTO, PARA CADA PERSONAJE EXISTE UNA RELACION
    #0 representa tristeza maxima
    felicidad =0
    amor =0
    odio =0
    confianza=0
    #Recuerdo que han sucedido x cosas // list<Evento_del_mundo>()
    recuerdos = list()
    #Deseo que se cumpla x evento ej: La muerte de x personaje //list<Deseos>()
    lista_deseos = list()
    lista_cosas_que_me_gustan = list()
    lista_eventos_que_odio =list()
    lista_cosas_que_odio=list()
    lista_subditos= list()

    def print_jugador_estadisticas(self):
        print(f"Poder fisico:{self.poder_fisico}")
        print(f"Poder magico:{self.poder_magico}")
        print(f"Vida:{self.vida}/{self.vida_maxima}")
        print(f"Mana:{self.mana}/{self.mana_maximo}")
        print(f"Defensa fisica:{self.defensa_fisica}")
        print(f"Defensa magica:{self.defensa_magica}")

    def print_efecto_de_habilidad(self):
        print(f"Vida:{self.vida}/{self.vida_maxima}")
        print(f"Mana:{self.mana}/{self.mana_maximo}")

    def print_inventario(self):
        print("Inventario:")
        for i in self.inventario:
            print(ma+f"{i.nombre}: {i.cantidad}")
        self.arma.print_arma()  

    def decidir_habilidad_random(self):
        h = Habilidad()
        r= random.randint(0, len(self.lista_habilidades)-1)
        return self.lista_habilidades[r]

    def GenerarEnemigo(self):
        num = random.randint(1,100)
        p = Personaje()
        lp = list()
        if num >0 and num <=2:
            p.nombre="Araña"
            p.tipo ="Araña"
            p.vida=0
            p.mana =0
            p.poder_fisico =0
            p.poder_magico =0
            p.defensa_fisica =0
            p.defensa_magica =0
            p.velocidad =0
            p.lista_habilidades.append(Habilidad.ObtenerHabilidad("Mordida"))
            p.lista_habilidades.append(Habilidad.ObtenerHabilidad("Super Mordida"))
            lp.append(p)
            return lp
        elif num >2 and num <=5:
            p.nombre="Humano"
            p.tipo ="Humano"
            p.vida=0
            p.mana =0
            p.poder_fisico =0
            p.poder_magico =0
            p.defensa_fisica =0
            p.defensa_magica =0
            p.velocidad =0
            p.lista_habilidades.append(Habilidad.ObtenerHabilidad("Patada"))
            p.lista_habilidades.append(Habilidad.ObtenerHabilidad("Puñetazo"))
            lp.append(p)
            return lp
        elif num >5 and num <=9:
            p.nombre="Orco"
            p.tipo ="Orco"
            p.vida=0
            p.mana =0
            p.poder_fisico =0
            p.poder_magico =0
            p.defensa_fisica =0
            p.defensa_magica =0
            p.velocidad =0
            p.lista_habilidades.append(Habilidad.ObtenerHabilidad("Mordida"))
            p.lista_habilidades.append(Habilidad.ObtenerHabilidad("Puñetazo"))
            p.lista_habilidades.append(Habilidad.ObtenerHabilidad("Garrotazo"))
            lp.append(p)
            return lp

        elif num >9 and num <=14:
            p.nombre="Goblin"
            p.tipo ="Goblin"
            p.vida=20
            p.mana =20
            p.poder_fisico =2
            p.poder_magico =1
            p.defensa_fisica =1
            p.defensa_magica =1
            p.velocidad =1
            p.lista_habilidades.append(Habilidad.ObtenerHabilidad("Puñetazo"))
            p.lista_habilidades.append(Habilidad.ObtenerHabilidad("Mordida"))
            lp.append(p)
            return lp
        elif num >14 and num <=100:
            p.nombre="Slime"
            p.tipo ="Slime"
            p.vida =10
            p.mana =10
            p.poder_fisico =1
            p.poder_magico =1
            p.defensa_fisica =1
            p.defensa_magica =1
            p.velocidad =1
            p.lista_habilidades.append(Habilidad.ObtenerHabilidad("Embestida"))
            lp.append(p)
            return lp
        else:
            print("Error, al generar enemigo")
            return lp
    
    @classmethod
    def decidir_dropeo(self, personaje_matador, personaje_matado):
        
        numero = random.randint(1,100)
        i = Item()
        if personaje_matado.nombre == "lobo":
            #puede dropear
            if numero > 99:
                return i.conseguir_item("pergamino alma de lobo")
            if numero > 89 and numero < 100:
                return i.conseguir_item("corazon de lobo")
            else:
                return i.conseguir_item("garra de lobo")
            

class Mundo:
    def __init__(self):
        self.lista_eventos = list()
        self.lista_mapa = list()
        self.lista_personajes = list()
        self.lista_posibles_decisiones = list()
        self.equipo_aliado = list()

    #lista tipo Evento_del_mundo
    lista_eventos =list()
    lista_personajes = list()
    lista_posibles_decisiones = list()
    lista_mapa = list()
    equipo_aliado = list()
    dias_desde_protagonista=0
    reloj =24

    def CargarDatos(self):
        #P1
        p1= Personaje()
        p1.nombre="Satan"
        p1.tipo = "Humano"
        p1.vida=100
        p1.mana = 100
        p1.poder_fisico =1
        p1.poder_magico =1
        p1.defensa_fisica =1
        p1.defensa_magica =1
        p1.velocidad =1
        p1.lista_habilidades.append(Habilidad.ObtenerHabilidad("Puñetazo"))
        #print(f"nombre: {p1.lista_habilidades[0].nombre} tipo: {p1.lista_habilidades[0].tipo}")
        p1.arma = p1.arma.Obtener_arma("Daga Oxidada")
        mundo.equipo_aliado.append(p1)
        mundo.lista_personajes.append(p1)

        #Kana
        p1 = Personaje()
        p1.nombre ="Kana"
        p1.tipo = "hombre gato"
        p1.tipo_especial ="esclavo"
        p1.vida=100
        p1.mana = 100
        p1.poder_fisico =1
        p1.poder_magico =1
        p1.defensa_fisica =1
        p1.defensa_magica =1
        p1.velocidad =1
        p1.lista_habilidades.append(Habilidad.ObtenerHabilidad("curacion 1"))
        mundo.equipo_aliado.append(p1)
        mundo.lista_personajes.append(p1)

        #Sr Alfonso
        p3 = Personaje()
        p3.nombre ="Sr. Alfonso"
        p3.tipo = "Vampiro"
        p3.tipo_especial ="?"
        pr = Profesion()
        pr.nombre="Mercader"
        pr.nivel =8
        p3.lisa_profesiones.append(pr)
        pr.nombre = "Esclavsta"
        pr.nivel = 8
        p3.lisa_profesiones.append(pr)
        p3.vida=100
        p3.mana = 100
        p3.poder_fisico =1
        p3.poder_magico =1
        p3.defensa_fisica =1
        p3.defensa_magica =1
        p3.velocidad =1
        mundo.lista_personajes.append(p3)

        mundo.lista_posibles_decisiones.append("Ir a otro lugar")
        mundo.lista_posibles_decisiones.append("Abrir inventario")
        mundo.lista_posibles_decisiones.append("Ver estadisticas")

        self._cargar_mapa()

    def _cargar_mapa(self):
        l= Lugar()
        l.nombre = "Pueblo"
        e= Edificio()
        e.nombre="Tienda del Sr Alfonso"
        e.tipo= "Tienda"
        l.lista_edificios.append(e)
        self.lista_mapa.append(l)
        
        l= Lugar()
        l.nombre= "Bosque"
        e = Edificio()
        e.nombre = "Entrar bosque nivel 1"
        e.tipo = "Batalla"
        l.lista_edificios.append(e)
        self.lista_mapa.append(l)
        
        l2= Lugar()
        l2.nombre= "Casa"
        e = Edificio()
        e.nombre = "Baño"
        e.tipo="Baño"
        l2.lista_edificios.append(e)
        e = Edificio()
        e.nombre= "Cofre"
        e.tipo= "Cofre"
        l2.lista_edificios.append(e)
        e = Edificio()
        e.nombre= "Cama"
        e.tipo= "Cama"
        l2.lista_edificios.append(e)
        e = Edificio()
        e.nombre= "Cama de Paja"
        e.tipo= "Cofre"
        l2.lista_edificios.append(e)
        self.lista_mapa.append(l2)

    def Avanzar_tiempo(self, tiempo):
         self.reloj -= tiempo
         if(self.reloj==0):
             self.dias_desde_protagonista+=1
             self.reloj = 24

    def Realizar_accion(self, movimiento, personaje):

        self.Avanzar_tiempo(movimiento.tiempo_consumido)
        if(movimiento.tipo == "Entrenar fisico"):
            personaje.ataque_fisico += personaje.ataque_fisico*0.01
        if(movimiento.tipo == "Entrenar magia"):
            personaje.ataque_magico += personaje.ataque_magico*0.01
        if(movimiento.tipo == "Entrenar vida"):
            personaje.vida += personaje.vida*0.01
  
    def Verificar_equipo_aliado_con_vida(self):
        for i in self.equipo_aliado:
            if(i.vida>0):
                return True
        return False

    def Ingreso_decision_correcta(self, lista):
        #retorna objeto
        proceso_correcto = False
        desicion=0
        while(not proceso_correcto):
            desicion = input("Ingresa tu desicion: ")
            try:
                desicion = int(desicion)
                proceso_correcto = True
            except:
                proceso_correcto =False
                
            if(proceso_correcto and  desicion >=0 and desicion < len(lista)):
                proceso_correcto =True
            else:
                proceso_correcto = False

            if(proceso_correcto):
                return lista[desicion]
                    
    def print_decidir_menus(self, lista_extra):
        #Imprime menu principal + desicones posibles
        for i in range (len(self.lista_posibles_decisiones)):
            print(f"{self.lista_posibles_decisiones[i]}: {i}")

        #en caso de lista_extra no ser tipo List()
        if isinstance(lista_extra, str):
            lista_aux = list()
            lista_aux.append(lista_extra)
            lista_extra = lista_aux.copy()

        cantidad_elementos = self.lista_posibles_decisiones + lista_extra
        restar_indice= len(self.lista_posibles_decisiones)

        for i in range(len(self.lista_posibles_decisiones), len(cantidad_elementos)):
            print(f"{lista_extra[i - restar_indice].nombre}: {i}")

        #verifica decision correcta  y retorna objeto seleccionado
        return self.Ingreso_decision_correcta(cantidad_elementos)
        

    def Jugar(self, lista_decision):
        while(self.Verificar_equipo_aliado_con_vida()):
           
            decision = self.print_decidir_menus(lista_decision)
            print_linea()

            #print(type(decision))
            #print(isinstance(decision, Lugar))
            if isinstance(decision, str):
                if(decision =="Ir a otro lugar"):
                    #self.print_decidir_menus(self.lista_mapa)
                    self.Jugar(self.lista_mapa)
                elif(decision =="Abrir inventario"):
                    #invenrtario del primer integrante del equipo aliado
                    print(self.equipo_aliado[0].print_inventario())
                    self
                elif(decision =="Ver estadisticas"):
                    #estadidsticas del perimer integrante del equipo aliado
                    self.equipo_aliado[0].print_jugador_estadisticas()
                else:
                    print("error de decision")
            elif isinstance(decision, Lugar):
                self.Jugar(decision.lista_edificios)
            elif isinstance(decision, Edificio):
                if(decision.nombre== "Entrar bosque nivel 1"):
                    b = Batalla()
                    b.Comenzar(self, 1)
                elif(decision.nombre == "Baño"):
                    print("Has regado el arbolito.")
                elif(decision.nombre == "Cofre"):
                    self.Jugar(decision.lista_items)
                else:
                    print("Error de edificio")
 
        print_linea()

class Batalla:
    def __init__(self):
        self.equipo_enemigo = list()

    equipo_aliado=list()
    equipo_enemigo=list()
    turno =0

    def VerificarSobrevivientes(self):
        aliados = False
        enemigos = False
        for i in self.equipo_aliado:
            if i.vida>0:
               aliados = True
        for i in self.equipo_enemigo:
            if i.vida>0:
               enemigos = True
        
        if aliados and enemigos:
            return True
        else:
            if enemigos == False:

                for e in self.equipo_enemigo:

                    item = Personaje.decidir_dropeo(self.equipo_aliado[0], e)
                    print(f"{e.nombre} ha dropeado: {item}")

                    item_encontrado = False

                    for i in self.equipo_aliado[0].inventario:
                        if i == item.nombre:
                            i += item.cantidad
                            item_encontrado = True
                     
                    if(not item_encontrado):
                        self.equipo_aliado[0].inventario.append(item)

            return False
        
    def Comenzar(self, mundo, dificultad):
        #cargar equipo aliado en la lista equipo_aliado
        self.equipo_aliado = mundo.equipo_aliado
        #generar personajes enemigos y cargalos en la lista equipo_enemigo
        p = Personaje()
        lista = p.GenerarEnemigo()
        for i in lista:
            self.equipo_enemigo.append(i)

        if(len(self.equipo_enemigo)>1):
            print("Peligro han aparecido multiples enemigos")
            for i in self.equipo_enemigo:
                print(f"    {i.nombre} nivel: {i.nivel}")
        elif(len(self.equipo_enemigo)==1):
            print("Peligro ha aparecido un enemigo")
            print(f"    {i.nombre} nivel: {i.nivel}")
        else:
            print("No hay enemigos ??")

        while(self.VerificarSobrevivientes()):
            for i in self.equipo_aliado:
                usuario = i
                print(i.nombre)
                for j in range (0, len(i.lista_habilidades)):
                    print(f"{i.lista_habilidades[j].nombre} :{j}")
                
                habilidad= mundo.Ingreso_decision_correcta(i.lista_habilidades)

                if(habilidad.tipo=="ataque_fisico"or habilidad.tipo=="ataque_magico"):
                    print("Atacar a:")
                    for e in range(0, len(self.equipo_enemigo)):
                        print(f"    {self.equipo_enemigo[e].nombre} nivel: {self.equipo_enemigo[e].nivel}: {e}")

                    objetivo= mundo.Ingreso_decision_correcta(self.equipo_enemigo)

                elif(habilidad.tipo=="curacion"):
                    print("Curar a:")
                    for a in range(0, len(self.equipo_aliado)):
                        print(f"{self.equipo_aliado[a].nombre} :{a}")
                    for e in range(0, len(self.equipo_enemigo)):
                        print(f"{self.equipo_enemigo[e].nombre} :{e+len(self.equipo_aliado)}")
                    
                    objetivo= mundo.Ingreso_decision_correcta(self.equipo_aliado + self.equipo_enemigo)
                    
                habilidad.Usar(usuario, objetivo)
                print_linea()

            for i in self.equipo_enemigo:
                p = Personaje()
                h = Habilidad()
                h= i.decidir_habilidad_random()
                r = random.randint(0, len(self.equipo_aliado)-1)
                p= self.equipo_aliado[r]
                h.Usar(i, p)
                print_linea()

class accion_realizada:
    tipo="entrenamiento"
    costo_en_tiempo=10


def print_linea():
    print(am + "=======================================================================")

def print_1_espacio():
    print("\n")

def print_2_espacios():
    print("\n\n")

def Inicio():
    print("Eres un joven que vive en una choza hecha de madera, en una aldea."\
        "\nEl lugar donde vives es basicamente una sola habitacion sucia y fria."\
        "\nTienes 18 años, eres delgado, feo y pobre"\
        "\ntu familia esta muerta y tu no pudiste hacer nada")
    print_1_espacio()

    #Asignar Nombre P1
    mundo.equipo_aliado[0].nombre=(input("cual es tu nombre? "))
    print_1_espacio()

    print("escucha que alguien golpeaa la puerta"\
        "\nnock!, nock!, nock!"\
        "\ncon una voluntad casi inexistente te levantas de tu cama y caminas hacia"\
        "\nla puerta"\
        "\nnock!, nock!, nock!"\
        "\nal abrir, logras ver a un hombre de traje, que trae a una chica"\
        "\ncon sus pies y manos amarradas para que no pueda escapar, es una esclava"\
        f"\n?: tu eres {mundo.equipo_aliado[0].nombre}, escuche que el esta muerto.. tu padre"\
        "\nSr Alfonso: yo soy el señor Alfonso. Esta chica era para el, la encargoa a ella especificamente"\
        "\nya que el no puede recibirla.. y tu eres su hijo.. esta chica ahora te pertenece"\
        "\nyo soy conocido por nunca incumplir mis negocios"\
        "\nsi un dia tienes dinero pasa por mi negocio, seguro encuentras algo que te"\
        "\ninterese")
    print_1_espacio()

    print("parece que simplemente aceptaras este futuro.."\
        "\nno tienes comida ni dinero para encargarte de esta chica"\
        f"\ntu inventario: {mundo.equipo_aliado[0].inventario}"\
        "\neso quiere decir que esta vacio")

    print_1_espacio()
    print("dejas que la chica entre a tu mugrosa choza"\
        "\nella te observa un momento.. al ver que tu la observas ella baja la mirada"\
        "\nesta claramente asustada sobre que tipo de amo seras"\
        "\nobserba a su alrededor.. se da cuenta de que como lo suponia"\
        "\neres un mugroso perdedor, probablemente me alimentara con hiervas del jardin"\
        "\n(eso piensa ella)")
        
    print_linea()

mundo = Mundo()
mundo.CargarDatos()
Inicio()
lista = list()
mundo.Jugar(lista)