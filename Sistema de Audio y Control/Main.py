
###################### Librerias y dependencias
import ReconocedordeVoz
import sintetizador
import ventana
import subprocess as sp
import controlTecladoyMouse
import time
import threading
######################
###################### Variables globales
duracion = "3" 
modoPrueba = True
menuAyuda = True
tiempo = {'uno':1,'1':1,'dos':2,'2':2,'tres':3,'3':3,'cuatro':4,'4':4,'cinco':5,'5':5,'seis':6,'6':6,'siente':7,'7':7,'ocho':8,'8':8,'nueve':9,'9':9,'diez':10,'10':10}
######################
a = True
sintetizador.hablar("iniciando asistente de voz")

while True:
    try:
        vozUsuario = ""
        vozUsuario = ReconocedordeVoz.reconocer(duracion).lower()

        if ("modo" in vozUsuario and ("desactivar" in vozUsuario or "fin" in vozUsuario)  and "prueba" in vozUsuario):
            modoPrueba = True
        elif ("modo" in vozUsuario and ("activar" in vozUsuario or "iniciar" in vozUsuario) and "prueba" in vozUsuario):
            modoPrueba = False

        if (modoPrueba == False):
            sintetizador.hablar("modo de prueba activo, usted dijo: "+vozUsuario)


        if (("ajustar" in vozUsuario or "cambiar" in vozUsuario) and ("tiempo" in vozUsuario or "duracion" in vozUsuario)):
            if (duracion == "Mone"):
                actual = "es automatico por el sistema, a la espera que dejes de hablar,"
            else:
                actual = "es de "+duracion+" segundos,"
           
            sintetizador.hablar("el tiempo actual es de "+actual+" diga el nuevo valor, recuerde que el tiempo esta dado en segundos y debe ser entero, por favor diga un numero entre uno y diez")
            vozUsuario = ReconocedordeVoz.reconocer("2").lower()
            aux2 = str(tiempo[vozUsuario])
            if (int(aux2) > 0 and int(aux2) < 11):
                sintetizador.hablar("el nuevo tiempo de escucha cambio a "+aux2+ " segundos.")
                duracion = aux2
            else:
                sintetizador.hablar("el numero dicho no fue entendido correctamente, queda definido forma automatica.")
                duracion = "None"

        if ("modo" in vozUsuario  and "ayuda" in vozUsuario):
            tex = 'Este es el modo ayuda, en este usted podrá mirar los diferentes módulos y se le dirán como son los comandos, ¿por favor diga que ayuda necesita?  Puede elegir entre navegación, configuración o escritura.'
            sintetizador.hablar(tex)   
            while menuAyuda:
                vozUsuario = ReconocedordeVoz.reconocer("None").lower()
                sintetizador.hablar('muy bien, ')
                if ("navegación" in vozUsuario or "navegacion" in vozUsuario): 
                    tex = 'En el módulo de navegación puede realizar las siguientes acciones, como primer comando esta, abrir WhatsApp, que sirve para abrir la aplicación, de igual manera esta el comando, cerrar WhatsApp, que cierra el aplicativo, otra funcionalidad  es ,minimizar, con esta ocultas tus conversaciones, si quieres volverla a abrir esta el comando, maximizar, o tembien puedes decir , restaurar, y volverá a aparecer tu ventana de WhatsApp, también están los comandos de scroll los cuales deberá decir, bajar, en caso de querer hacer un scroll hacia abajo o deberá decir, subir, en caso de querer hacer un scroll hacia arriba. ¿Desea preguntar sobre otro modulo? Responde con sí o no.'
                    sintetizador.hablar(tex) 
                    vozUsuario = ReconocedordeVoz.reconocer("None").lower()
                    if ("si" in vozUsuario or "sí" in vozUsuario):
                        sintetizador.hablar('muy bien, Puede elegir entre navegación, configuración o escritura') 
                    else:
                        sintetizador.hablar('muy bien, Espero haber sido de ayuda, saliendo del modo')
                        menuAyuda = False
                elif ("configuración" in vozUsuario or "configuracion" in vozUsuario): 
                    tex = 'En el módulo de configuración puede realizar las siguientes acciones, como primer comando puedes tener un modo de prueba con el siguiente comando, activar modo de prueba, con este podrás probar el micrófono y dirá todo lo que tú le hables, también  está el comando para cambiar el tiempo de escucha y se activa diciendo, ajustar tiempo de escucha, donde  te pregunta el nuevo valor en segundos de 1 a 10 y lo parametriza. ¿Desea preguntar sobre otro modulo? Responde con sí o no'
                    sintetizador.hablar(tex) 
                    vozUsuario = ReconocedordeVoz.reconocer("None").lower()
                    if ("si" in vozUsuario or "sí" in vozUsuario):
                        sintetizador.hablar('muy bien, Puede elegir entre navegación, configuración o escritura') 
                    else:
                        sintetizador.hablar('muy bien, Espero haber sido de ayuda, saliendo del modo')
                        menuAyuda = False 
                elif ("escritura" in vozUsuario):
                    tex = 'En el módulo de escritura básicamente tiene los comandos necesarios para escribir o iniciar un chat nuevo,  como primer comando esta, nuevo, con este abre el panel de los contactos y posteriormente con el comando, escribir, puedes escribir el nombre del contacto, luego con el comando, enter o aceptar,  podrás enviar la petición para crear el chat nuevo, y con los mismo anteriores comandos podrás escribir una vez ya dentro del chat, si quieres enviar un mensaje a un contacto especifico de manera rápida podrás hacerlo con el siguiente comando, enviar mensaje a, y al final le añades el nombre el contacto, un ejemplo puede ser, enviar mensaje a Daniel, el aplicativo reconocerá el contacto y luego te pedirá que digas tu mensaje y luego lo enviara. ¿Desea preguntar sobre otro modulo? Responde con sí o no'  
                    sintetizador.hablar(tex) 
                    vozUsuario = ReconocedordeVoz.reconocer("None").lower()
                    if ("si" in vozUsuario or "sí" in vozUsuario):
                        sintetizador.hablar('muy bien, Puede elegir entre navegación, configuración o escritura') 
                    else:
                        sintetizador.hablar('muy bien, Espero haber sido de ayuda, saliendo del modo')
                        menuAyuda = False


        if ("abrir" in vozUsuario and modoPrueba):
            aux = "abriendo whatsapp"
            sintetizador.hablar(aux)
            controlTecladoyMouse.abrir()
        elif ("cerrar" in vozUsuario and modoPrueba):
            sintetizador.hablar("cerrando whatsapp")
            controlTecladoyMouse.cerrarVentana()                
        elif (("bajar" in vozUsuario or "scroll down" in vozUsuario or "scrolldown" in vozUsuario) and modoPrueba) :
            sintetizador.hablar('bajando')
            controlTecladoyMouse.scrollDown()
        elif (("abajo" in vozUsuario  or "siguiente" in vozUsuario) and modoPrueba):
            sintetizador.hablar('bajando siguiente chat') 
            controlTecladoyMouse.siguienteChat()   
        elif ("arriba" in vozUsuario and modoPrueba):
            sintetizador.hablar('subiendo al siguiente chat') 
            controlTecladoyMouse.anteriorChat()   
        elif (("subir" in vozUsuario or "scroll up" in vozUsuario or "scrollup" in vozUsuario) and modoPrueba) :
            sintetizador.hablar('subiendo') 
            controlTecladoyMouse.scrollUp()     
        elif ("minimi" in vozUsuario and modoPrueba):
            sintetizador.hablar('minimizando whatsapp')
            controlTecladoyMouse.minimizar()
        elif ((("restaurar" in vozUsuario) or ("maximi" in vozUsuario)) and modoPrueba):
            sintetizador.hablar('abriendo whatsapp')
            controlTecladoyMouse.abrir1()
        elif ((("aumentar" in vozUsuario and  "letra" in vozUsuario) or  "acercar" in vozUsuario) and modoPrueba):
            sintetizador.hablar('aumentando letra')
            controlTecladoyMouse.acercar()
        elif ((("reducir" in vozUsuario and  "letra" in vozUsuario) or  "alejar" in vozUsuario) and modoPrueba):
            sintetizador.hablar('reduciendo letra')
            controlTecladoyMouse.alejar()
        elif ("nuevo" in vozUsuario and modoPrueba):
            sintetizador.hablar('creando nuevo chat')
            controlTecladoyMouse.nuevo()
        elif ("perfil" in vozUsuario and modoPrueba):
            sintetizador.hablar('mostrando perfil')
            controlTecladoyMouse.foto()
        elif ("escribir" in vozUsuario and modoPrueba):
            sintetizador.hablar('claro')
            vozUsuario = vozUsuario[vozUsuario.find("escribir")+9:]
            sintetizador.hablar('escribiendo '+vozUsuario)
            controlTecladoyMouse.escribir(vozUsuario)
        elif ("buscar" in vozUsuario and modoPrueba):
            sintetizador.hablar("buscando")
            vozUsuario = vozUsuario[vozUsuario.find("buscar")+7:]
            sintetizador.hablar('buscando '+vozUsuario)
        elif (("atras" in vozUsuario or "atrás" in vozUsuario or "escape" in vozUsuario) and modoPrueba):
            sintetizador.hablar('atrás')
            controlTecladoyMouse.escape()
        elif (("eliminar" in vozUsuario and "conver" in vozUsuario) and modoPrueba):
            sintetizador.hablar('eliminando conversacion')
            controlTecladoyMouse.borrar()
        elif ("finalizar" in vozUsuario and modoPrueba):
            sintetizador.hablar("finalizando prueba")
            controlTecladoyMouse.cerrarVentana()    
        elif (("aceptar" in vozUsuario or "enter" in vozUsuario) and modoPrueba):
            sintetizador.hablar("aceptar")
            controlTecladoyMouse.enter() 
        elif (("enviar" in vozUsuario and  "mensaje a" in vozUsuario) and modoPrueba): 
            aux = vozUsuario[vozUsuario.find("mensaje a")+10:]
            tex = 'que mensaje desea darle a ',aux,'?'
            sintetizador.hablar(tex)   
            vozUsuario = ReconocedordeVoz.reconocer("None").lower()
            sintetizador.hablar('muy bien, enviando mensaje')
            controlTecladoyMouse.nuevo()
            controlTecladoyMouse.escribir(aux)
            time.sleep(1)
            controlTecladoyMouse.enter() 
            time.sleep(1)
            controlTecladoyMouse.escribir(vozUsuario)
            controlTecladoyMouse.enter() 
        elif (( "chat de" in vozUsuario) and modoPrueba): 
            aux = vozUsuario[vozUsuario.find("chat de")+7:]
            sintetizador.hablar('muy bien')
            controlTecladoyMouse.buscarChat()
            controlTecladoyMouse.escribir(aux)
            time.sleep(1)
            controlTecladoyMouse.enter()   
        elif (("ver foto" in vozUsuario and  "de" in vozUsuario) and modoPrueba):
            aux = vozUsuario[vozUsuario.find("foto de")+7:]
            sintetizador.hablar('mostrando foto')
            controlTecladoyMouse.foto(aux)
            time.sleep(1)
            controlTecladoyMouse.enter() 
        elif (( "borrar" in vozUsuario and "todo" in vozUsuario) and modoPrueba): 
            controlTecladoyMouse.borrarTodo()
        elif (( "borrar" in vozUsuario) and modoPrueba): 
            controlTecladoyMouse.borrarvozUsuario()

    except Exception as e:
        print('Ocurrio un error', e)
