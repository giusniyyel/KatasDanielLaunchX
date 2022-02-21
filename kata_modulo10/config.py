def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("No se pudo encontrar el archivo config.txt!")
    except IsADirectoryError:
        print("Se encontró config.txt pero es un directorio y no se puede leer")
    except (BlockingIOError, TimeoutError):
        print("El sistema de archivos está demasiado ocupado y no se pudieron leer los archivos de configuración")


if __name__ == '__main__':
    main()