from sklearn.tree import DecisionTreeClassifier, export_text
from colors import *
from progress_bar import progress_bar, section, info

def train_tree(X_train, y_train, depth):
    label = "Sin límite" if depth is None else depth

    progress_bar(f"Entrenando modelo con max_depth={label}...")
    tree = DecisionTreeClassifier(max_depth=depth, random_state=7)
    tree.fit(X_train, y_train)
    info("Entrenamiento completado.")
    return tree

def print_rules(tree, wine):
    section("REGLAS DEL MODELO")
    rules = export_text(tree, feature_names=wine.feature_names)
    print(f"{MAGENTA}{rules}{RESET}")

def evaluate(tree, X_test, y_test):
    section("EVALUANDO MODELO")
    progress_bar("Calculando precisión...")
    acc = tree.score(X_test, y_test)
    info(f"Precisión: {BOLD}{acc:.4f}{RESET}")
    return acc

def train_multiple_depths(wine, X_train, X_test, y_train, y_test, depths):
    section("COMPARANDO PROFUNDIDADES")

    for depth in depths:
        tree = train_tree(X_train, y_train, depth)
        acc = tree.score(X_test, y_test)

        label = "Sin límite" if depth is None else depth
        print(f"\n{CYAN}{BOLD}--- max_depth={label} ---{RESET}")
        print(f"Precisión: {GREEN}{acc:.4f}{RESET}")
        print(f"{MAGENTA}{export_text(tree, feature_names=wine.feature_names)}{RESET}")
