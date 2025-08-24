import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import requests
from matplotlib import colors as mcolors

# ---------- utilidades ----------
def closest_css_color_name(rgb):
    """Retorna o nome da cor CSS4 mais próxima (distância euclidiana em RGB, usando float para evitar overflow)."""
    rgb = np.array(rgb, dtype=float)
    min_dist = float('inf')
    closest = None
    for name, hex_val in mcolors.CSS4_COLORS.items():
        rc, gc, bc = np.array(mcolors.to_rgb(hex_val)) * 255.0
        dist = np.sum((rgb - np.array([rc, gc, bc]))**2)
        if dist < min_dist:
            min_dist = dist
            closest = name
    return closest

def luminancia_rgb(rgb):
    r, g, b = [c/255.0 for c in rgb]
    return 0.2126*r + 0.7152*g + 0.0722*b

# ---------- baixar imagem com user-agent ----------
url = "https://upload.wikimedia.org/wikipedia/commons/f/f4/The_Scream.jpg"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
resp = requests.get(url, headers=headers, timeout=20)
resp.raise_for_status()
img_array = np.asarray(bytearray(resp.content), dtype=np.uint8)

# OpenCV: BGR -> RGB
img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# ---------- K-Means ----------
img_resized = cv2.resize(img, (200, 200))
pixels = img_resized.reshape((-1, 3)).astype(np.float32)

k = 5
kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
kmeans.fit(pixels)

centers = kmeans.cluster_centers_          # float64
labels, counts = np.unique(kmeans.labels_, return_counts=True)
proportions = counts / counts.sum()

# ordenar por maior proporção
order = np.argsort(-proportions)
colors = centers[order]                    # ainda float
proportions = proportions[order]

# nomes e conversões finais p/ exibição
names = [closest_css_color_name(c) for c in colors]
colors_u8 = np.array(colors, dtype=np.uint8)   # p/ exibir/plotar
hexes = [f"#{c[0]:02X}{c[1]:02X}{c[2]:02X}" for c in colors_u8]

# ---------- saída textual ----------
print("Paleta extraída (ordenada por porcentagem):")
for i, (name, rgb, hx, p) in enumerate(zip(names, colors_u8, hexes, proportions), 1):
    rgb_tuple = tuple(int(x) for x in rgb)
    print(f"{i}. {name:<15} RGB={rgb_tuple}  HEX={hx}  -> {p*100:.2f}%")

# ---------- gráfico de pizza (NOMES + %) ----------
plt.figure(figsize=(8, 4))
plt.pie(
    proportions,
    labels=names,
    autopct="%1.1f%%",
    startangle=90,
    colors=colors_u8 / 255.0,
    wedgeprops=dict(edgecolor='white')
)
plt.title('Paleta de Cores - O Grito (nomes + %)')
plt.tight_layout()
plt.show()

# ---------- imagem original + paleta com rótulos ----------
plt.figure(figsize=(10, 5))

# imagem
plt.subplot(1, 2, 1)
plt.imshow(img)
plt.axis('off')
plt.title('Imagem Original')

# paleta
plt.subplot(1, 2, 2)
W, H = 360, 120
palette = np.zeros((H, W, 3), dtype='uint8')
steps = W // k
for i, (color, name, p) in enumerate(zip(colors_u8, names, proportions)):
    x0, x1 = i*steps, (i+1)*steps if i < k-1 else W
    palette[:, x0:x1, :] = color
    txt = f"{name}\n{p*100:.1f}%"
    y, x = H//2, x0 + (x1-x0)//2
    text_color = 'white' if luminancia_rgb(color) < 0.5 else 'black'
    plt.text(x, y, txt, ha='center', va='center', fontsize=10, weight='bold', color=text_color)

plt.imshow(palette)
plt.axis('off')
plt.title('Paleta Extraída (nomes + %)')
plt.tight_layout()
plt.show()
