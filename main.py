from datetime import datetime

# Parent class
class Vehicle:
    def __init__(self, brand: str, manufacture_date: str, price: float, mileage: int, features: dict):
        self.brand = brand  # String
        self.manufacture_date = datetime.strptime(manufacture_date, "%Y-%m-%d")  # Date
        self.price = price  # Float
        self.mileage = mileage  # Integer
        self.features = features  # Dictionary

    def display_info(self):
        """Menampilkan informasi kendaraan dan mengembalikannya sebagai string"""
        vehicle_info = (
            f"Merek: {self.brand}\n"
            f"Tanggal Produksi: {self.manufacture_date.strftime('%d-%m-%Y')}\n"
            f"Harga: Rp{self.price:,.2f}\n"
            f"Kilometer: {self.mileage} km\n"
            "Fitur:\n"
        )
        for key, value in self.features.items():
            vehicle_info += f"  - {key}: {value}\n"
        return vehicle_info

# Child class 1
class Car(Vehicle):
    def __init__(self, brand, manufacture_date, price, mileage, features, num_seats):
        super().__init__(brand, manufacture_date, price, mileage, features)
        self.num_seats = num_seats  # Integer

    def display_info(self):
        # Mengambil informasi dari parent class dan menambahkannya
        vehicle_info = super().display_info()  # Pastikan ini mengembalikan string
        vehicle_info += f"Jumlah Kursi: {self.num_seats}\n"
        return vehicle_info

# Child class 2
class Motorcycle(Vehicle):
    def __init__(self, brand, manufacture_date, price, mileage, features, engine_capacity):
        super().__init__(brand, manufacture_date, price, mileage, features)
        self.engine_capacity = engine_capacity  # Float

    def display_info(self):
        # Mengambil informasi dari parent class dan menambahkannya
        vehicle_info = super().display_info()  # Pastikan ini mengembalikan string
        vehicle_info += f"Kapasitas Mesin: {self.engine_capacity} cc\n"
        return vehicle_info

# Child class 3
class Truck(Vehicle):
    def __init__(self, brand, manufacture_date, price, mileage, features, cargo_capacity):
        super().__init__(brand, manufacture_date, price, mileage, features)
        self.cargo_capacity = cargo_capacity  # Integer

    def display_info(self):
        # Mengambil informasi dari parent class dan menambahkannya
        vehicle_info = super().display_info()  # Pastikan ini mengembalikan string
        vehicle_info += f"Kapasitas Muatan: {self.cargo_capacity} kg\n"
        return vehicle_info

# Daftar kendaraan
vehicle_list = []

def add_vehicle(vehicle):
    """Menambahkan kendaraan ke dalam daftar"""
    vehicle_list.append(vehicle)
    print(f"{vehicle.brand} berhasil ditambahkan.")

def remove_vehicle(brand):
    """Menghapus kendaraan berdasarkan merek"""
    global vehicle_list
    vehicle_list = [v for v in vehicle_list if v.brand != brand]
    print(f"{brand} berhasil dihapus dari daftar.")

def get_vehicle_list():
    """Mengembalikan daftar kendaraan dalam list string"""
    if not vehicle_list:
        return ["Tidak ada kendaraan dalam daftar."]
    
    vehicle_info_list = [v.display_info() for v in vehicle_list]
    return vehicle_info_list

# Program utama
if __name__ == "__main__":
    while True:
        print("--- Pilih Aksi ---")
        print("1. Tambah Kendaraan")
        print("2. Hapus Kendaraan")
        print("3. Tampilkan Kendaraan")
        print("4. Keluar")
        action = input("Masukkan pilihan (1/2/3/4): ")
        
        if action == "1":
            print("--- Pilih Jenis Kendaraan ---")
            print("1. Mobil")
            print("2. Sepeda Motor")
            print("3. Truk")
            choice = input("Masukkan pilihan (1/2/3): ")
            
            brand = input("Masukkan merek kendaraan: ")
            manufacture_date = input("Masukkan tanggal produksi (YYYY-MM-DD): ")
            price = float(input("Masukkan harga kendaraan: "))
            mileage = int(input("Masukkan kilometer kendaraan: "))
            features = {}
            while True:
                key = input("Masukkan nama fitur (atau 'selesai' untuk mengakhiri): ")
                if key.lower() == "selesai":
                    break
                value = input(f"Masukkan nilai fitur untuk {key}: ")
                features[key] = value
            
            if choice == "1":
                num_seats = int(input("Masukkan jumlah kursi: "))
                vehicle = Car(brand, manufacture_date, price, mileage, features, num_seats)
            elif choice == "2":
                engine_capacity = float(input("Masukkan kapasitas mesin (cc): "))
                vehicle = Motorcycle(brand, manufacture_date, price, mileage, features, engine_capacity)
            elif choice == "3":
                cargo_capacity = int(input("Masukkan kapasitas muatan (kg): "))
                vehicle = Truck(brand, manufacture_date, price, mileage, features, cargo_capacity)
            else:
                print("Pilihan tidak valid.")
                continue
            
            add_vehicle(vehicle)
        
        elif action == "2":
            brand = input("Masukkan merek kendaraan yang ingin dihapus: ")
            remove_vehicle(brand)
        
        elif action == "3":
            print("\n--- Daftar Kendaraan ---")
            for info in get_vehicle_list():
                print(info)
                print("-")
        
        elif action == "4":
            print("Terima kasih telah menggunakan program ini.")
            break
        
        else:
            print("Pilihan tidak valid, silakan coba lagi.")
