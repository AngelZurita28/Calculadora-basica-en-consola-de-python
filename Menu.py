# menu


if __name__ == '__main__':
    print('Hello, and welcome to "The los pollos Hermanos Family", my name is gustavo, but you can call me Gus...')
    total = None
    listaCompra = list()

    while True:
        print("Que desea ordenar? ")
        print("[1] Comidas [2] Bebidas [3] Postres ...")
        seccion = input()
        
        arregloParaLista = None
        match seccion:
            case '1':
                print('Que comida desea ordenar? ')
                print('[1] Pizza(100) [2] Hamburguesa(90) [3] Spaghetti(150) [4] Boneless(140) [5] Sushi(200) ...')
                comida = input()
                print('Cuantas Ordenes quiere? ')
                cantidad = input()
                try:
                    cantidad = int(cantidad)
                except:
                    print('error en la insercion de los datos')
                    continue
                match comida:
                    case '1':
                        arregloParaLista = ['Pizza', cantidad, cantidad * 100]
                    case '2':
                        arregloParaLista = ['Hamburguesa', cantidad, cantidad * 90]
                    case '3':
                        arregloParaLista = ['Spaghetti', cantidad, cantidad * 150]
                    case '4':
                        arregloParaLista = ['Boneless', cantidad, cantidad * 140]
                    case '5':
                        arregloParaLista = ['sushi', cantidad, cantidad * 200]
                    case _:
                        print('Dato incorrecto')

            case '2':
                print('Que Bebida desea ordenar? ')
                print('[1] Coca(20) [2] Pepsi(15) [3] Cafe(30) [4] Limonada(40) [5] Cerveza(30) ...')
                comida = input()
                print('Cuantas Ordenes quiere? ')
                cantidad = input ()
                try:
                    cantidad = int(cantidad)
                except:
                    print('error en la insercion de los datos')
                    continue
                match comida:
                    case '1':
                        arregloParaLista = ['Coca', cantidad, cantidad * 20]
                    case '2':
                        arregloParaLista = ['Pepsi', cantidad, cantidad * 15]
                    case '3':
                        arregloParaLista = ['Cafe', cantidad, cantidad * 30]
                    case '4':
                        arregloParaLista = ['Limonada', cantidad, cantidad * 40]
                    case '5':
                        arregloParaLista = ['Cerveza', cantidad, cantidad * 30]
                    case _:
                        print('Dato incorrecto')
            
            case '3':
                print('Que Postre desea ordenar? ')
                print('[1] Tiramisu(90) [2] Panna Cotta(100) [3] Bonet(120) [4] Torrone(60) [5] Cartocci(70) ...')
                comida = input()
                print('Cuantas Ordenes quiere? ')
                cantidad = input ()
                try:
                    cantidad = int(cantidad)
                except:
                    print('error en la insercion de los datos')
                    continue
                match comida:
                    case '1':
                        arregloParaLista = ['Tiramisu', cantidad, cantidad * 90]
                    case '2':
                        arregloParaLista = ['Panna Cotta', cantidad, cantidad * 100]
                    case '3':
                        arregloParaLista = ['Bonet', cantidad, cantidad * 120]
                    case '4':
                        arregloParaLista = ['Torrone', cantidad, cantidad * 60]
                    case '5':
                        arregloParaLista = ['Cartocci', cantidad, cantidad * 70]
                    case _:
                        print('Dato incorrecto')
            
            case _:
                print('error en los datos')
            
        listaCompra.append(arregloParaLista)
        print("Desea ordenar algo mas? [S/N]...")
        respuesta = input()
        if respuesta == 'n' or respuesta == 'N':
            break

    print('SU ORDEN!')
    subtotal = 0
    for i in listaCompra:
        print(i[0],  "   x", i[1], "   $", i[2])
        subtotal += float(i[2])
    iva = subtotal * 0.16
    total = subtotal + iva 
    print("subtotal : ", subtotal)
    print('IVA : ', iva)
    print('Total : ' , total)
        
