# 🚀 OOP dengan Python

## 📌 Ciforegia Romakoneri

---

## 📖 1. Konsep

🛠️ Dalam konsep ini, kita membangun sistem pencatatan kendaraan dengan paradigma **Object-Oriented Programming (OOP)**. 

🔹 **Vehicle** bertindak sebagai **superclass**, mewarisi atributnya ke beberapa **subclass** yaitu:
- 🚗 **Car**
- 🏍️ **Motorcycle**
- 🚛 **Truck**

✨ Setiap subclass memiliki tambahan atribut serta metode `display_info()` yang digunakan untuk menampilkan informasi kendaraan dengan cara yang berbeda.

![Konsep OOP](https://github.com/user-attachments/assets/4d2f997b-4f0d-4d43-bc27-a8d4176ee783)

---

## 📊 2. Class Diagram

Diagram berikut menunjukkan hubungan antara superclass dan subclass:

![Class Diagram](https://github.com/user-attachments/assets/77a76908-5ad5-4252-9169-bb20cfae9dac)

### ✨ Struktur Class `Vehicle`

#### 🔹 Atribut:
- `brand` : str → Merek kendaraan
- `manufacture_date` : date → Tanggal pembuatan
- `price` : float → Harga kendaraan
- `mileage` : int → Jarak tempuh kendaraan
- `features` : dict → Fitur tambahan kendaraan

#### 🔹 Metode:
- `display_info()` → Menampilkan informasi dasar kendaraan

### 🚗 Subclass `Car`
- **Atribut tambahan:** `num_seats`
- **Modifikasi metode:** `display_info()` menampilkan jumlah kursi

### 🏍️ Subclass `Motorcycle`
- **Atribut tambahan:** `engine_capacity`
- **Modifikasi metode:** `display_info()` menampilkan kapasitas mesin

### 🚛 Subclass `Truck`
- **Atribut tambahan:** `cargo_capacity`
- **Modifikasi metode:** `display_info()` menampilkan kapasitas kargo

---

## 📌 3. Use Case Diagram

Diagram berikut menjelaskan bagaimana admin dapat berinteraksi dengan sistem:

![Use Case Diagram](https://github.com/user-attachments/assets/e08b5d51-c335-44c0-8bcb-39cbed9eb89f)

### 🛠️ Fitur dalam sistem:
- **Add Vehicle** – Menambahkan kendaraan baru ke sistem
- **Remove Vehicle** – Menghapus kendaraan dari sistem
- **View Vehicle** – Melihat daftar kendaraan yang terdaftar

---

## 🔄 4. Sequence Diagram

Sequence diagram menggambarkan interaksi antara admin, sistem, dan kendaraan.

![Sequence Diagram](https://github.com/user-attachments/assets/690c513c-ea9f-4d35-ace6-726aff8249a1)

### 🔹 Langkah-langkah:
- **Choose Menu** – Admin memilih fitur (Add, Remove, View Vehicle, atau Selesai)
- **Add Vehicle** – Admin memilih jenis kendaraan, menginput data, lalu sistem menyimpannya
- **Remove Vehicle** – Admin memasukkan nama kendaraan untuk dihapus, sistem akan mengonfirmasi sebelum menghapus
- **View Vehicle** – Sistem mengambil dan menampilkan daftar kendaraan

---

## 🖥️ 5. CLI Apps OOP Python

![image](https://github.com/user-attachments/assets/b8ce0316-0e7a-48ef-bbb0-59ed9db93ed7)

![image](https://github.com/user-attachments/assets/82ddde77-5967-4de0-b844-8e06c89b2fc2)



---
