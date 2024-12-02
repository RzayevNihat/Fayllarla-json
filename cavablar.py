import json
import math

# laptops.json faylını oxuyun
with open('laptops.json', 'r') as file:
    laptops = json.load(file)

# 1. Touch screen olan notbukların sayı
touch_screen_count = sum(1 for laptop in laptops if laptop.get("Touch Screen", False))

# 2. Notbukların ümumi sayı
total_laptops = len(laptops)

# 3. Touch screen faizi
touch_screen_percentage = (touch_screen_count / total_laptops) * 100 if total_laptops > 0 else 0

# 4. SSD = 512GB, RAM = 16GB, Sərt disk = 1TB olan notbuk
matching_laptops = [
    laptop for laptop in laptops
    if ("512GB SSD" in laptop.get("Product Name", "") or "512GB" in laptop.get("Product Name", "")) and 
    ("16GB" in laptop.get("Product Name", "")) and 
    ("1TB" in laptop.get("Product Name", ""))
]

# 5. Ən az texniki xüsusiyyətlərə malik notbuk
min_specs_laptop = min(laptops, key=lambda x: (int(x.get("Battery Life (up to hours)", 0)), x.get("Size", "0")))

# 6. Müxtəlif notbuk markalarının sayı
unique_brands = {laptop["Brand"] for laptop in laptops}

# 7. Hangi marka daha çox yayılıb
brand_counts = {}
for laptop in laptops:
    brand = laptop["Brand"]
    brand_counts[brand] = brand_counts.get(brand, 0) + 1
most_common_brand = max(brand_counts, key=brand_counts.get)

# 8. Ən məşhur marka faylda neçə dəfə görünür?
most_common_brand_count = brand_counts[most_common_brand]

# 9. Ekranın diametri 17 düymdən çox olan notbuklar
large_screen_laptops_count = sum(1 for laptop in laptops if float(laptop["Size"].replace("inch", "").strip()) > 17)

# 10. "iBall" notbukları üçün orta batareya ömrü
iball_battery_lives = [int(laptop["Battery Life (up to hours)"]) for laptop in laptops if laptop["Brand"] == "iBall"]
average_iball_battery_life = sum(iball_battery_lives) / len(iball_battery_lives) if iball_battery_lives else 0

# 11. Faylda Windows-un neçə müxtəlif versiyası
unique_windows_versions = {laptop["Operating system"] for laptop in laptops}

# Nəticələri çap edin
print(f"Touch screen olan notbukların faizi: {math.ceil(touch_screen_percentage)}%")
print("\nSSD = 512GB, RAM = 16GB, Sərt disk = 1TB olan notbuklar:")
for laptop in matching_laptops:
    print(f"- {laptop['Product Name']} | Link: {laptop.get('link', 'N/A')}")

print(f"\nƏn az texniki xüsusiyyətlərə malik notbuk: {min_specs_laptop['Product Name']}")

print(f"\nFaylda {len(unique_brands)} müxtəlif notbuk markası təmsil olunur.")
print(f"\nDaha çox yayılmış marka: {most_common_brand} | Görünmə sayı: {most_common_brand_count}")

print(f"\nEkranın diametri 17 düymdən çox olan {large_screen_laptops_count} notbuk var.")

print(f"\n'iBall' notbukları üçün orta batareya ömrü: {average_iball_battery_life:.2f} saat.")

print(f"\nFaylda Windows-un {len(unique_windows_versions)} müxtəlif versiyası təqdim olunub.")
