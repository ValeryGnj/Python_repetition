import os

spis = []

for dirs, folders, files in os.walk('C:\\Users\HUAWEI\OneDrive\Рабочий стол\ДОГОВОРА'):
    for file in files:
        full = os.path.join(dirs, file)
        spis.append(full)

print("\n".join(spis))
