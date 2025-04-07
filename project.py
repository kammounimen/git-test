import cv2
import numpy as np
import matplotlib.pyplot as plt

# Charger l'image
image = cv2.imread("C:\\Users\\User\\Desktop\\computervision\\image1.jpg")  
if image is None:
    print("Erreur lors du chargement de l'image.")
    exit()

# Conversion en niveaux de gris
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Égalisation de l'histogramme
equalized = cv2.equalizeHist(gray)

# Seuillage d'Otsu
_, thresh = cv2.threshold(equalized, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Amélioration de la luminosité
alpha = 2 
beta = 50   
brightened = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

# Calculer l'histogramme
hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

hist = hist / hist.max()   

# Tracer l'histogramme
plt.figure()
plt.title("Histogramme de l'image en niveaux de gris")
plt.xlabel("Intensité des pixels")
plt.ylabel("Fréquence")
plt.plot(hist, color='black')
plt.xlim([0, 256])
plt.show()

# Affichage des résultats
cv2.imshow('Image originale', image)
cv2.imshow('Image en niveaux de gris', gray)
cv2.imshow('Image egalisée', equalized)
cv2.imshow('Image seuillée', thresh)
cv2.imshow('Image améliorée', brightened)

# Attendre une touche pour fermer les fenêtres
cv2.waitKey(0)
cv2.destroyAllWindows()
