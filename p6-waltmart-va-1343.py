import matplotlib.pyplot as plt
import numpy as np
# Daniel Nieves NC=1343
cant_productos=[100,150,200,300,500]
precio=[4000,7000,9000,12000,18000]

plt.plot(cant_productos)
plt.show()
# plt.plot(cant_productos,precio)
# plt.show()

# personalizar
plt.plot(cant_productos,precio,color="blue",marker="o",linestyle="dashed",linewidth=2,markersize=12)
plt.title("Ventas de Waltmart 1343")
plt.xlabel("cant_productos")
plt.ylabel("precios")

plt.show()