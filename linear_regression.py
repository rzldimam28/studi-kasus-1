import numpy as np

def fit_model(x, y):

  # mengubah x dan y menjadi array
  x = np.array(x)
  y = np.array(y)

  # menghitung sigma x, sigma x^2, sigma y, sigma xy
  sigma_x = sum(x)
  sigma_x_sq = sum(x ** 2)
  sigma_y = sum(y)
  sigma_x_y = sum(x * y)
  n = len(x)

  # menghitung a dan b
  b = ((n * sigma_x_y) - (sigma_x * sigma_y)) / ((n * sigma_x_sq) - (sigma_x ** 2))
  a = (sigma_y - b * sigma_x) / n

  print("Model Regresi yg dihasilkan:")
  print(f"y = {a} + {b}x")
  return round(a, 2), round(b, 2)

def predict(x, a, b):
  # y = a + bx
  return a + b * x

x = [1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0]
y = [8.1, 7.8, 8.5, 9.8, 9.5, 8.9, 8.6, 10.2, 9.3, 9.2, 10.5]

a, b = fit_model(x, y)
print(f"Nilai a: {a}")
print(f"Nilai b: {b}")

pred = predict(3, a, b)
print(f"Hasil prediksi: {pred}")