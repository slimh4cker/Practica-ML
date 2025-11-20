from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from progress_bar import progress_bar, info, section

def load_dataset():
    section("CARGANDO DATASET")

    progress_bar("Cargando dataset 'Wine'...")
    wine = load_wine()
    X, y = wine.data, wine.target

    info(f"Características detectadas: {len(wine.feature_names)}")
    info(f"Clases encontradas: {set(y)}")

    progress_bar("Dividiendo dataset 80% / 20%...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=7
    )

    info(f"Entrenamiento: {len(X_train)} registros")
    info(f"Pruebas      : {len(X_test)} registros")

    return wine, X_train, X_test, y_train, y_test
