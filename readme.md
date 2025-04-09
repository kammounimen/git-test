# Amélioration d’images pour la vision nocturne

## Problématique

Les images prises en faible luminosité présentent des défis importants pour le traitement d'images, notamment un manque de contraste, une perte de détails dans les zones sombres et l'apparition de bruit. Ces problèmes compliquent l'analyse et l'interprétation des images, particulièrement dans des domaines comme la surveillance, la photographie, la médecine et la vision par ordinateur.

## Objectif

L'objectif de ce projet est d'améliorer la visibilité des images prises dans des conditions de faible luminosité en appliquant plusieurs techniques de traitement d'image, telles que:

- **Conversion en niveaux de gris** : Pour réduire la complexité des données d'image tout en préservant l'information essentielle.
- **Égalisation de l'histogramme** : Améliorer le contraste de l'image.Elle est particulièrement utile pour les images sombres et mal éclairées.
- **Seuillage d'Otsu** : Segmenter l'image en une image binaire en fonction d'un seuil optimal déterminé automatiquement.
- **Amélioration de la luminosité** : Modifier les paramètres de luminosité et de contraste pour rendre l'image plus claire.
- **Calcul et tracé de l'histogramme** : Visualiser la distribution des intensités des pixels dans l'image.

## Prérequis

- Python 3.x
- Bibliothèques Python : `opencv-python`, `numpy`, `matplotlib`

Vous pouvez installer les bibliothèques nécessaires avec la commande suivante :

```bash
pip install opencv-python numpy matplotlib


```

## Fonctions Utilisées

Le code utilise principalement des fonctions d'OpenCV et de matplotlib pour réaliser ces étapes :

- **cv2.imread()** : Cette fonction charge une image depuis le disque. Elle prend en paramètre le chemin de l'image et retourne un tableau contenant l'image.
- **cv2.cvtColor()** : Cette fonction est utilisée pour convertir l'image d'un espace de couleur à un autre. Ici, elle est utilisée pour convertir l'image en niveaux de gris (cv2.COLOR_BGR2GRAY).
- **cv2.equalizeHist()** : Cette fonction égalise l'histogramme de l'image. Elle redistribue les intensités des pixels de manière plus uniforme, améliorant ainsi le contraste de l'image.
- **cv2.threshold()** : Le seuillage d'Otsu est appliqué via cette fonction. cv2.THRESH_OTSU est un algorithme qui calcule automatiquement un seuil optimal pour convertir l'image en une image binaire.
- **cv2.convertScaleAbs()** : Cette fonction est utilisée pour ajuster le contraste et la luminosité de l'image. Les paramètres alpha et beta contrôlent respectivement le contraste et la luminosité de l'image.
- **cv2.calcHist()** : Cette fonction calcule l'histogramme d'une image. Dans ce cas, elle est utilisée pour calculer l'histogramme de l'image en niveaux de gris. L'histogramme montre la répartition des intensités des pixels dans l'image.
- **plt.plot() (de matplotlib)** : Cette fonction trace l'histogramme. Les données de l'histogramme sont affichées sous forme de graphiques pour visualiser la répartition des intensités des pixels.
- **cv2.imshow()** : Cette fonction permet d'afficher les différentes images traitées (image originale, image en niveaux de gris, image égalisée, image seuillée, image améliorée).
- **cv2.waitKey() et cv2.destroyAllWindows()** : Ces fonctions permettent de maintenir les fenêtres ouvertes et d'attendre que l'utilisateur appuie sur une touche avant de fermer les fenêtres d'affichage.

## Résultats attendus

- **Image originale** : L'image telle qu'elle a été chargée.
  ![Image originale](C:\Users\User\Desktop\git-test\originale.png)
- **Image en niveaux de gris** : L'image convertie en niveaux de gris, simplifiant ainsi les traitements.
  ![Image en niveaux de gris](C:\Users\User\Desktop\git-test\gray.png)
- **Image égalisée** : L'image après l'égalisation de l'histogramme, avec un meilleur contraste
  ![Image égalisée](C:\Users\User\Desktop\git-test\egalisee.png)
- **Image seuillée** : L'image après l'application du seuillage d'Otsu, transformée en binaire.
  ![Image seuillée](C:\Users\User\Desktop\git-test\seuillee.png)
- **Image améliorée** : L'image avec une luminosité et un contraste augmentés.
  ![Image améliorée](C:\Users\User\Desktop\git-test\amelioree.png)
- **Histogramme** : Un histogramme de l'image en niveaux de gris sera également affiché pour montrer comment la distribution des pixels a changé après les traitements.
  ![Histogramme](C:\Users\User\Desktop\git-test\histogramme.png)
