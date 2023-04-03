from collections import deque
import os

# Fungsi BFS untuk mencari rute terpendek dengan bobot terkecil antar kota
def bfs_shortestpath(graf, mulai, tujuan):
    # Queue untuk menyimpan total jarak tempuh dan node-node yang dikunjungi
    queue = deque([(mulai, 0, [mulai])])
    # Set untuk menyimpan node-node yang sudah dikunjungi
    visited = set()

    while queue:
        # penetapan current_node pada antrian pertama ( queue )
        current_node, current_cost, current_route = queue.popleft()
        # Jika current_node belum dikunjungi, maka set visited
        if current_node not in visited:
            visited.add(current_node)

            # return current_cost jika node saat ini sama dengan node tujuan
            if current_node == tujuan:
                return current_cost, current_route

            # Tambahkan node-node tetangga yang belum dikunjungi ke dalam antrian
            for neighbor, neighbor_cost in graf[current_node].items():
                if neighbor not in visited:
                    total_cost = current_cost + neighbor_cost
                    queue.append((neighbor, total_cost, current_route + [neighbor]))

            # Urutkan antrian berdasarkan cost terkecil
            queue = deque(sorted(queue, key=lambda x: x[1]))

    # Jika tidak ditemukan rute dari awal ke tujuan, maka return None
    return None

# Membuat graph berbobot dengan dictionary
graf = {
    'Surabaya': {'Gresik': 20.7, 'Sidoarjo': 27, 'Mojokerto': 51.9, 'Tuban': 112},
    'Gresik': {'Surabaya': 20.7, 'Lamongan' : 29.5, 'Tuban': 93.3, 'Mojokerto': 52.4},
    'Sidoarjo': {'Surabaya': 27, 'Malang' : 71.3, 'Mojokerto': 36.1},
    'Malang': {'Sidoarjo': 71.3},
    'Lamongan': {'Gresik': 30.6, 'Babat': 28.9},
    'Babat': {'Mojokerto': 66.4,'Lamongan': 28.3, 'Tuban': 32.5, 'Bojonegoro': 37.7},
    'Tuban': {'Bojonegoro': 45, 'Babat': 31.2, 'Gresik': 93.1, 'Surabaya': 112},
    'Bojonegoro': {'Tuban': 45.4,'Babat': 38.1,'Nganjuk': 65.6},
    'Mojokerto': {'Babat': 67.1,'Lamongan': 51,'Surabaya': 52.8, 'Sidoarjo': 36.1,'Nganjuk': 71.5},
    'Nganjuk': {'Bojonegoro': 65.6, 'Mojokerto': 73},
}

print("Pilihan kota yang tersedia :")
for i in graf.keys():
    print(f"{i}")

mulai = input("Masukkan kota asal       : ").lower().capitalize()
tujuan = input("Masukkan kota tujuan    : ").lower().capitalize()
# Hasil dari return akan dimasukkan masing - masing secara terpisah ke variabel jarak_terpendek dan rute_terpendek
jarak_terpendek, rute_terpendek = bfs_shortestpath(graf, mulai, tujuan)


if jarak_terpendek is None:                                 #jika tidak terdapat rute / daerah terisolasi
    print(f"Tidak ada rute dari {mulai} ke {tujuan}.")
else:                                                       #jika terdapat rute untuk mencapai tujuan
    print(f"Diperlukan jarak tempuh sejauh {jarak_terpendek}km dan melewati {len(rute_terpendek)-2} kota untuk mencapai kota {tujuan} dengan jarak terpendek")
    for i in range(len(rute_terpendek)):
        kota = rute_terpendek[i]
        if i == len(rute_terpendek)-1:
           print(f" hingga tibalah di {kota}")
        elif i == 0:
            print(f"Dimulai dari {kota}", end='')
        elif i % 3 == 0:
            print(f" lalu ke {kota}", end='')
        elif i % 5 == 0:
            print(f" kemudian lewati {kota}", end='')
        elif i % 2 == 0:
            print(f" berikutnya {kota}", end='')
        else:
            print(f" selanjutnya menuju {kota}", end='')

print("Rute :", " -> ".join(rute_terpendek))

os.system("PAUSE")