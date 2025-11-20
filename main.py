from dataset import load_dataset
from model import train_tree, print_rules, evaluate, train_multiple_depths
from progress_bar import section, info
from colors import *

def main():
    section("Inicializando Árbol de Decisión")

    # Cargar dataset
    wine, X_train, X_test, y_train, y_test = load_dataset()

    # Entrenamiento principal
    tree = train_tree(X_train, y_train, depth=2)

    # Reglas del modelo
    print_rules(tree, wine)

    # Evaluación
    evaluate(tree, X_test, y_test)

    # Comparación con múltiples profundidades
    train_multiple_depths(
        wine,
        X_train, X_test,
        y_train, y_test,
        depths=[1, 2, 3, None]
    )

    section("PROCESO COMPLETADO")
    info("Arbol(es) terminado(ss)")

if __name__ == "__main__":
    main()
