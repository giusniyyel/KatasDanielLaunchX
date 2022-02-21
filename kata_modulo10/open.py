def main():
    try:
        open("/path/to/mars.jpg")
    except FileNotFoundError as err:    
        if err.errno == 2:
            print('No se pudo encontrar el archivo config.txt')
        elif err.errno == 13:
            print("Se encontró config.txt pero no se puede leer")

if __name__ == '__main__':
    main()