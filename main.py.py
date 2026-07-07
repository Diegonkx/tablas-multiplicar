import pygame
import random
import sys
import os

# Inicialización general de Pygame
pygame.init()

# Configuración del directorio de trabajo y dimensiones de la pantalla
os.chdir(os.path.dirname(os.path.abspath(__file__)))
ANCHO, ALTO = 1000, 750
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Plataforma de Tablas de Multiplicar")

# Colores globales
AZUL_CLARO = (135, 206, 235)
AZUL_OSCURO = (0, 120, 255)
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
GRIS = (200, 200, 200)

# Fuentes globales
fuente_titulo = pygame.font.SysFont("Arial", 40, True)
fuente_texto = pygame.font.SysFont("Arial", 28)

# Carga de recursos comunes
nums = {}
for i in range(11):
    img = pygame.image.load(f"{i}.png")
    nums[i] = pygame.transform.scale(img, (70, 70))

por = pygame.image.load("x.png")
por = pygame.transform.scale(por, (70, 70))

igual = pygame.image.load("=.png")
igual = pygame.transform.scale(igual, (70, 70))

# Recursos específicos de la actividad 1 (escalados a su tamaño original)
nums_act1 = {}
for i in range(11):
    img = pygame.image.load(f"{i}.png")
    nums_act1[i] = pygame.transform.scale(img, (100, 100))

x_act1 = pygame.transform.scale(pygame.image.load("x.png"), (100, 100))
igual_act1 = pygame.transform.scale(pygame.image.load("=.png"), (100, 100))
feliz = pygame.transform.scale(pygame.image.load("feliz.png"), (200, 200))
triste = pygame.transform.scale(pygame.image.load("triste.png"), (200, 200))


def mostrar_menu():
    """Dibuja la interfaz del menú principal."""
    pantalla.fill(AZUL_CLARO)
    
    # Título principal
    txt_titulo = fuente_titulo.render("MENÚ PRINCIPAL DE ACTIVIDADES", True, NEGRO)
    pantalla.blit(txt_titulo, (ANCHO // 2 - txt_titulo.get_width() // 2, 50))
    
    # Opciones del menú
    opciones = [
        "1. Evaluador de Tablas",
        "2. Tabla del 9 Animada",
        "3. Ver Todas las Tablas Animadas",
        "Presiona ESC en cualquier actividad para regresar aquí."
    ]
    
    y_offset = 180
    for idx, opcion in enumerate(opciones):
        color = NEGRO if idx < 3 else AZUL_OSCURO
        txt_opcion = fuente_texto.render(opcion, True, color)
        pantalla.blit(txt_opcion, (150, y_offset))
        y_offset += 60

    pygame.display.flip()


def actividad_1():
    """PROGRAMA 1: FELIZ TRISTE (Evaluador de Tablas)"""
    # Ajustar ventana temporalmente al tamaño del programa original
    pygame.display.set_mode((900, 600))
    pygame.display.set_caption("Evaluador de Tablas")
    
    titulo_font = pygame.font.SysFont("Arial", 40)
    texto_font = pygame.font.SysFont("Arial", 30)
    
    ejecutando = True
    while ejecutando:
        n1 = random.randint(0, 10)
        n2 = random.randint(0, 10)
        respuesta = ""
        contestado = False
        correcto = False
        
        while not contestado:
            pantalla.fill(AZUL_CLARO)
            titulo1 = titulo_font.render("EVALUADOR DE TABLAS", True, NEGRO)
            pantalla.blit(titulo1, (250, 20))
            pantalla.blit(nums_act1[n1], (150, 150))
            pantalla.blit(x_act1, (280, 150))
            pantalla.blit(nums_act1[n2], (410, 150))
            pantalla.blit(igual_act1, (540, 150))
            
            caja = pygame.Rect(670, 170, 120, 60)
            pygame.draw.rect(pantalla, BLANCO, caja)
            txt = texto_font.render(respuesta, True, NEGRO)
            pantalla.blit(txt, (690, 180))
            pygame.display.update()
            
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:  # Volver al menú
                        pygame.display.set_mode((ANCHO, ALTO))  # Restaurar tamaño
                        return
                    if e.key == pygame.K_RETURN:
                        if respuesta != "":
                            resultado = n1 * n2
                            correcto = (int(respuesta) == resultado)
                            contestado = True
                    elif e.key == pygame.K_BACKSPACE:
                        respuesta = respuesta[:-1]
                    else:
                        if e.unicode.isdigit():
                            respuesta += e.unicode
                            
        pantalla.fill(AZUL_CLARO)
        if correcto:
            mensaje = titulo_font.render("¡CORRECTO!", True, NEGRO)
            pantalla.blit(mensaje, (320, 50))
            pantalla.blit(feliz, (350, 180))
        else:
            mensaje = titulo_font.render("INCORRECTO", True, NEGRO)
            pantalla.blit(mensaje, (320, 50))
            pantalla.blit(triste, (350, 180))
            resultado = n1 * n2
            txt = texto_font.render(f"La respuesta correcta es: {resultado}", True, NEGRO)
            pantalla.blit(txt, (220, 420))
            
        txt2 = texto_font.render("Presiona ESPACIO para continuar o ESC para menú", True, NEGRO)
        pantalla.blit(txt2, (80, 520))
        pygame.display.update()
        esperando = True
        while esperando:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_SPACE:
                        esperando = False
                    if e.key == pygame.K_ESCAPE:
                        pygame.display.set_mode((ANCHO, ALTO))
                        return


def actividad_2():
    """PROGRAMA 2: TABLA DEL 9 Animada (Fija en la tabla del 9)"""
    pygame.display.set_caption("Tablas Animadas")
    reloj = pygame.time.Clock()
    
    tabla = 9  # Forzado a la tabla del 9 directamente
    fila_actual = 0
    paso_actual = 0
    ultimo_tiempo = pygame.time.get_ticks()
    VELOCIDAD = 250
    
    while True:
        reloj.tick(60)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:  # Regresar al menú
                    return
                    
        pantalla.fill(BLANCO)
        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - ultimo_tiempo > VELOCIDAD:
            paso_actual += 1
            if paso_actual > 5:
                paso_actual = 0
                fila_actual += 1
            ultimo_tiempo = tiempo_actual
            
        titulo = fuente_titulo.render(f"TABLA DEL {tabla}", True, AZUL_OSCURO)
        pantalla.blit(titulo, (330, 20))
        
        if fila_actual > 10:
            fila_actual = 10
            paso_actual = 5
            
        y = 100
        for i in range(fila_actual + 1):
            resultado = tabla * i
            pasos_visibles = 5
            if i == fila_actual:
                pasos_visibles = paso_actual
                
            if pasos_visibles >= 1:
                pantalla.blit(nums[tabla], (100, y))
            if pasos_visibles >= 2:
                pantalla.blit(por, (220, y))
            if pasos_visibles >= 3:
                pantalla.blit(nums[i], (340, y))
            if pasos_visibles >= 4:
                pantalla.blit(igual, (460, y))
            if pasos_visibles >= 5:
                resultado_texto = str(resultado)
                x_resultado = 600
                for digito in resultado_texto:
                    pantalla.blit(nums[int(digito)], (x_resultado, y))
                    x_resultado += 80
            y += 55
        pygame.display.flip()



def actividad_3():
    """PROGRAMA 3: TODAS LAS TABLAS (Ejecución directa continua)"""
    pygame.display.set_caption("Todas las Tablas Secuenciales")
    reloj = pygame.time.Clock()
    
    tabla = 0
    fila_actual = 0
    paso_actual = 0
    ultimo_tiempo = pygame.time.get_ticks()
    VELOCIDAD = 150
    while True:
        reloj.tick(60)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    return
                    
        pantalla.fill(BLANCO)
        tiempo_actual = pygame.time.get_ticks()
        
        if tiempo_actual - ultimo_tiempo > VELOCIDAD:
            paso_actual += 1
            if paso_actual > 5:
                paso_actual = 0
                fila_actual += 1
            if fila_actual > 10:
                fila_actual = 0
                tabla += 1
                if tabla > 10:
                    tabla = 0  # Reinicia a la tabla del 0 al finalizar todas
            ultimo_tiempo = tiempo_actual
            
        titulo = fuente_titulo.render(f"TABLA DEL {tabla}", True, AZUL_OSCURO)
        pantalla.blit(titulo, (330, 20))
        
        y = 100
        for i in range(fila_actual + 1):
            resultado = tabla * i
            pasos_visibles = 5
            if i == fila_actual:
                pasos_visibles = paso_actual
                
            if pasos_visibles >= 1:
                pantalla.blit(nums[tabla], (100, y))
            if pasos_visibles >= 2:
                pantalla.blit(por, (220, y))
            if pasos_visibles >= 3:
                pantalla.blit(nums[i], (340, y))
            if pasos_visibles >= 4:
                pantalla.blit(igual, (460, y))
            if pasos_visibles >= 5:
                resultado_texto = str(resultado)
                x_resultado = 600
                for digito in resultado_texto:
                    pantalla.blit(nums[int(digito)], (x_resultado, y))
                    x_resultado += 80
            y += 55
            
        pygame.display.flip()


# Bucle Principal de Control (Menú del Sistema)
ejecutando_sistema = True
while ejecutando_sistema:
    mostrar_menu()
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando_sistema = False
            
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_1:
                actividad_1()
                # Asegurar restauración del tamaño original del contenedor al volver
                pygame.display.set_mode((ANCHO, ALTO))
                pygame.display.set_caption("Plataforma de Tablas de Multiplicar")
            elif evento.key == pygame.K_2:
                actividad_2()
                pygame.display.set_caption("Plataforma de Tablas de Multiplicar")
            elif evento.key == pygame.K_3:
                actividad_3()
                pygame.display.set_caption("Plataforma de Tablas de Multiplicar")
            elif evento.key == pygame.K_ESCAPE:
                ejecutando_sistema = False

pygame.quit()
sys.exit()

