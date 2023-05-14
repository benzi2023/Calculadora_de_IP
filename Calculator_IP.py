class InvalidInputError(Exception):
    pass


def calcular_direccion_red(ip, mascara):
    ip_octetos = [int(octeto) for octeto in ip.split('.')]
    mascara_octetos = [int(octeto) for octeto in mascara.split('.')]
    
    direccion_red = []
    for i in range(4):
        direccion_red.append(ip_octetos[i] & mascara_octetos[i])
    
    return '.'.join(map(str, direccion_red))


def calcular_direccion_broadcast(ip, mascara):
    ip_octetos = [int(octeto) for octeto in ip.split('.')]
    mascara_octetos = [int(octeto) for octeto in mascara.split('.')]
    
    direccion_broadcast = []
    for i in range(4):
        direccion_broadcast.append(ip_octetos[i] | (255 - mascara_octetos[i]))
    
    return '.'.join(map(str, direccion_broadcast))


def calcular_rango_direcciones(ip, mascara):
    direccion_red = calcular_direccion_red(ip, mascara)
    direccion_broadcast = calcular_direccion_broadcast(ip, mascara)
    
    rango_inicial = direccion_red
    rango_final = direccion_broadcast
    
    return rango_inicial, rango_final


def validar_entrada(entrada):
    octetos = entrada.split('.')
    
    if len(octetos) != 4:
        raise InvalidInputError('La entrada debe tener exactamente 4 octetos.')
    
    for octeto in octetos:
        try:
            valor = int(octeto)
            if valor < 0 or valor > 255:
                raise InvalidInputError('Cada octeto debe ser un número entero entre 0 y 255.')
        except ValueError:
            raise InvalidInputError('Cada octeto debe ser un número entero.')
    
    return True


ip = '192.168.0.100'
mascara = '255.255.255.0'

try:
    if validar_entrada(ip) and validar_entrada(mascara):
        direccion_red = calcular_direccion_red(ip, mascara)
        direccion_broadcast = calcular_direccion_broadcast(ip, mascara)
        rango_inicial, rango_final = calcular_rango_direcciones(ip, mascara)

        print(f'Dirección de red: {direccion_red}')
        print(f'Dirección de broadcast: {direccion_broadcast}')
        print(f'Rango de direcciones: {rango_inicial} - {rango_final}')
    else:
        print('Las entradas proporcionadas no son válidas.')
except InvalidInputError as e:
    print(f'Error: {str(e)}')
