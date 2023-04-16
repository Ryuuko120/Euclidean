import numpy as np
import cv2

# Burung Beo
C1I1 = cv2.imread('Target/C1I1.png', 0)
C1I2 = cv2.imread('Target/C1I2.png', 0)
C1I3 = cv2.imread('Target/C1I3.png', 0)

# Burung Kicau
C2I1 = cv2.imread('Target/C2I1.png', 0)
C2I2 = cv2.imread('Target/C2I2.png', 0)
C2I3 = cv2.imread('Target/C2I3.png', 0)

# Burung Pemangsa
C3I1 = cv2.imread('Target/C3I1.png', 0)
C3I2 = cv2.imread('Target/C3I2.png', 0)
C3I3 = cv2.imread('Target/C3I3.png', 0)

# Burung Air
C4I1 = cv2.imread('Target/C4I1.png', 0)
C4I2 = cv2.imread('Target/C4I2.png', 0)
C4I3 = cv2.imread('Target/C4I3.png', 0)

# Burung Eksotik
C5I1 = cv2.imread('Target/C5I1.png', 0)
C5I2 = cv2.imread('Target/C5I2.png', 0)
C5I3 = cv2.imread('Target/C5I3.png', 0)

# Pembanding
Pembanding = cv2.imread('Target/Pivot.png', 0)

# ubah citra menjadi vektor
vC1I1 = np.ravel(C1I1)
vC1I2 = np.ravel(C1I2)
vC1I3 = np.ravel(C1I3)

vC2I1 = np.ravel(C2I1)
vC2I2 = np.ravel(C2I2)
vC2I3 = np.ravel(C2I3)

vC3I1 = np.ravel(C3I1)
vC3I2 = np.ravel(C3I2)
vC3I3 = np.ravel(C3I3)

vC4I1 = np.ravel(C4I1)
vC4I2 = np.ravel(C4I2)
vC4I3 = np.ravel(C4I3)

vC5I1 = np.ravel(C5I1)
vC5I2 = np.ravel(C5I2)
vC5I3 = np.ravel(C5I3)

vP = np.ravel(Pembanding)

# hitung jarak Euclidean
dC1I1 = np.sqrt(np.sum((vC1I1 - vP) ** 2))
dC1I2 = np.sqrt(np.sum((vC1I2 - vP) ** 2))
dC1I3 = np.sqrt(np.sum((vC1I3 - vP) ** 2))

dC2I1 = np.sqrt(np.sum((vC2I1 - vP) ** 2))
dC2I2 = np.sqrt(np.sum((vC2I2 - vP) ** 2))
dC2I3 = np.sqrt(np.sum((vC2I3 - vP) ** 2))

dC3I1 = np.sqrt(np.sum((vC3I1 - vP) ** 2))
dC3I2 = np.sqrt(np.sum((vC3I2 - vP) ** 2))
dC3I3 = np.sqrt(np.sum((vC3I3 - vP) ** 2))

dC4I1 = np.sqrt(np.sum((vC4I1 - vP) ** 2))
dC4I2 = np.sqrt(np.sum((vC4I2 - vP) ** 2))
dC4I3 = np.sqrt(np.sum((vC4I3 - vP) ** 2))

dC5I1 = np.sqrt(np.sum((vC5I1 - vP) ** 2))
dC5I2 = np.sqrt(np.sum((vC5I2 - vP) ** 2))
dC5I3 = np.sqrt(np.sum((vC5I3 - vP) ** 2))


# Tampilkan jarak
print(dC1I1)
print(dC1I2)
print(dC1I3)

print(dC2I1)
print(dC2I2)
print(dC2I3)

print(dC3I1)
print(dC3I2)
print(dC3I3)

print(dC4I1)
print(dC4I2)
print(dC4I3)

print(dC5I1)
print(dC5I2)
print(dC5I3)

print()

# Buat tempat untuk menyimpan nama variable beserta value variable
var_dict = {'C1I1': C1I1, 'C1I2': C1I2, 'C1I3': C1I3, 'C2I1': C2I1, 'C2I2': C2I2, 'C2I3': C2I3, 'C3I1': C3I1, 'C3I2': C3I2, 'C3I3': C3I3, 'C4I1': C4I1, 'C4I2': C4I2, 'C4I3': C4I3, 'C5I1': C5I1, 'C5I2': C5I2, 'C5I3': C5I3}

# Mencari Citra Terdekat
min_dict = {'C1I1': dC1I1, 'C1I2': dC1I2, 'C1I3': dC1I3, 'C2I1': dC2I1, 'C2I2': dC2I2, 'C2I3': dC2I3, 'C3I1': dC3I1, 'C3I2': dC3I2, 'C3I3': dC3I3, 'C4I1': dC4I1, 'C4I2': dC4I2, 'C4I3': dC4I3, 'C5I1': dC5I1, 'C5I2': dC5I2, 'C5I3': dC5I3}

min_var = min(min_dict, key=min_dict.get)  # Ambil variable beserta nilai terkecilnya
min_img = var_dict[min_var]  # Ambil gambar dari variable yang sudah diambil

print(f"Gambar yang jarak citranya paling dekat dengan pembanding berdasarkan rumus Eucledian adalah: {min_var}")
print(f"Jaraknya adalah: {min_dict[min_var]}")

#Tampilkan Gambarnya
p = cv2.resize(Pembanding, (800, 800))
min_image_resized = cv2.resize(min_img, (800, 800))

combined_img = cv2.hconcat([p, min_image_resized])

cv2.imshow('Result', combined_img)
cv2.waitKey(0)
cv2.destroyAllWindows()