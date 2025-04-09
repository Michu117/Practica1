def resultados(palindromos):
    if palindromos:
        print("Palíndromos encontrados:")
        print(", ".join(palindromos))
    else:
        print("No hay números palíndromos.")
    print(f"Contador: {len(palindromos)}")
