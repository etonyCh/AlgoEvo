Projet : Algorithmes d'Optimisation  Travaux

Ce dépôt contient des implémentations et des wrappers d'algorithmes d'optimisation (heuristiques et métaheuristiques) développés dans le cadre du cours. Le `README` cidessous est rédigé pour un usage académique : il décrit l'organisation du dépôt, les algorithmes fournis, comment exécuter des validations rapides et les éléments importants pour l'évaluation.

**Auteurs :** Étudiant

**Contexte :** Code produit dans le cadre d'un cours d'optimisation / métaheuristiques. Destiné à démontrer des versions simples de plusieurs algorithmes (Genetic Algorithm, Simulated Annealing, Tabu Search, PSO, ACO) appliqués à des problèmes classiques : Voyageur de commerce (TSP), Sac-à-dos (Knapsack), et stubs pour l'ordonnancement.

**Licence :** Usage académique uniquement (par défaut, contactez l'auteur pour réutilisation).

**Structure du dépôt**
- **`algorithme_*.py`** : implémentations originales (TSP et variantes) conservées au niveau racine.
- **`algo/`** : scripts ACO procéduraux originaux (`TSP_ACO.py`, `KP_ACO.py`).
- **`voyageur_commerce/`** : wrappers  humains  pour les algorithmes TSP (GA, Tabou, Recuit, PSO, ACO).
- **`sac_a_dos/`** : implémentations et wrappers pour le problème du sac-à-dos (GA binaire, Recuit simple, PSO binaire, wrapper ACO).
- **`ordonnancement/`** : stubs et points d'entrée pour futures implémentations d'ordonnancement.

**Algorithmes fournis (aperçu)**
- Voyageur de commerce (TSP) : `algorithme_genetique_rang.py`, `algorithme_genetique_roulette.py`, `algorithme_recuit_simulé.py`, `algorithme_tabou.py`, `TSP_PSO.py`, et le script ACO dans `algo/TSP_ACO.py`.
- Sac-à-dos (Knapsack) : version ACO (`algo/KP_ACO.py`) + nouvelles petites implémentations démonstratives dans `sac_a_dos/` : `sac_a_dos_genetique.py`, `sac_a_dos_recuit.py`, `sac_a_dos_pso.py`.
- Ordonnancement : dossiers prêts (`ordonnancement/`)  implémentations à venir (stubs commentés).

**Remarques de conception importantes**
- Les wrappers dans les sous-dossiers ajoutent temporairement le chemin racine au `sys.path` pour permettre l'import des modules placés à la racine. Pour un projet reproductible et partageable, il est recommandé de convertir le dépôt en package Python (ajouter des `__init__.py` et/ou utiliser `pyproject.toml`) et de retirer ces hacks d'import.
- Certains scripts ACO sont écrits de façon procédurale et sont exécutés via subprocess dans les wrappers afin d'éviter des effets secondaires liés à l'importation.

**Prérequis**
- Python 3.10+ (les scripts utilisent des constructions simples compatibles avec Python 3.8+, mais 3.10+ recommandé).
- Créer un environnement virtuel :

```powershell
python -m venv .venv
.\\.venv\\Scripts\\Activate.ps1
pip install -r requirements.txt  # (s'il existe  voir notes cidessous)
```

Remarque : le dépôt n'a pas de `requirements.txt` exhaustif par défaut ; dépendances externes ne sont pas nécessaires pour les scripts fournis (utilisent uniquement la stdlib), sauf si vous ajoutez des bibliothèques externes.

**Exemples d'exécution (validation rapide)**
Les commandes suivantes sont des exemples courts pour lancer les wrappers et observer des sorties reproductibles (utiliser PowerShell sous Windows) :

```powershell
# TSP - Exemples rapides
python .\\voyageur_commerce\\voyageur_commerce_genetique.py --seed 1 --nombre_generations 50 --taille_population 50
python .\\voyageur_commerce\\voyageur_commerce_tabou.py --seed 1 --nombre_iterations 200 --taille_tabu 50
python .\\voyageur_commerce\\voyageur_commerce_recuit.py --seed 1 --iterations_max 1000 --temperature_initiale 1000
python .\\voyageur_commerce\\voyageur_commerce_pso.py --seed 1 --num_particles 30 --max_iters 200
python .\\voyageur_commerce\\voyageur_commerce_aco.py

# Knapsack - Exemples rapides
python .\\sac_a_dos\\sac_a_dos_genetique.py --seed 1 --generations 100 --pop_size 50
python .\\sac_a_dos\\sac_a_dos_recuit.py --seed 1 --iterations 1000
python .\\sac_a_dos\\sac_a_dos_pso.py --seed 1 --n_particles 50 --iters 500
python .\\sac_a_dos\\sac_a_dos_aco.py
```

Ces commandes affichent une sortie textuelle indiquant la meilleure solution trouvée et les métriques associées (distance, valeur, etc.). Pour des runs reproductibles, réutilisez l'option `--seed` fournie par les wrappers.

**Format des entrées / instances**
- Les scripts TSP présents utilisent des jeux de données internes ou générés aléatoirement pour des démonstrations. Si vous souhaitez évaluer sur des fichiers (TSPLIB par exemple), il faudra adapter les wrappers pour charger ces instances.
- Le knapsack demo utilise des listes d'objets définies dans les scripts. Pour charger des instances externes, ajouter une option `--instance` et un parseur CSV simple.

**Validation courte que j'ai exécutée**
- J'ai lancé un jeu de commandes de validation courte (script wrappers) : tous les wrappers TSP et Knapsack ont démarré et ont produit des résultats attendus. Quelques corrections mineures ont été appliquées pendant la validation (import path, suppression d'un import invalide et nettoyage de marqueurs de patch résiduels).

**Conseils pour l'évaluation / lecture par le professeur**
- Pour inspecter l'algorithme concret d'un TSP, ouvrir `algorithme_genetique_roulette.py` ou `algorithme_recuit_simulé.py`.
- Pour voir une implémentation simple et pédagogique du sac-à-dos, consulter `sac_a_dos/sac_a_dos_genetique.py`, `sac_a_dos/sac_a_dos_recuit.py`, et `sac_a_dos/sac_a_dos_pso.py`.
- Si vous préférez une structure de package propre (recommandé pour la maintenance), je peux :
  - ajouter des `__init__.py`,
  - créer un `pyproject.toml` minimal,
  - générer un `requirements.txt` si des dépendances apparaissent.

**Limitations connues**
- Certains algorithmes (notamment ACO dans `algo/`) sont des scripts procéduraux et ne sont pas empaquetés comme modules importables.
- Les implémentations fournies pour le sac-à-dos et la PSO sont des versions pédagogiques, pas optimisées pour la performance ou pour des instances de grande taille.

**Prochaines étapes suggérées**
1. Transformer le dépôt en package Python propre pour éviter les manipulations de `sys.path`.
2. Ajouter des tests unitaires minimaux et un workflow CI (GitHub Actions) pour les validations rapides.
3. Implémenter les algorithmes d'ordonnancement si nécessaire (précisez le problème : Jobshop, Flowshop, ou Singlemachine).

---
Si vous souhaitez, je peux maintenant :
- convertir le dépôt en package Python propre (ajouter `__init__.py` et / ou `pyproject.toml`) ; ou
- implémenter un algorithme d'ordonnancement précis (indiquez lequel) ; ou
- générer des tests unitaires et un workflow CI.

Indiquez la suite que vous préférez et je m'en occupe.
