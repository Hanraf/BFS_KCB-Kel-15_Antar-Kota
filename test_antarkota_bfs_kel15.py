from collections import deque

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
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'D': 5, 'E': 1},
    'C': {'A': 3, 'F': 11},
    'D': {'B': 5},
    'E': {'B': 4, 'F': 1},
    'F': {'C': 6, 'E': 1}
}

mulai = input("Masukkan kota asal       : ").upper()
tujuan = input("Masukkan kota tujuan    : ").upper()
lewat = []

while True:
    mampir = input("Apakah ingin menambahkan kota yang harus dilewati ( y / n )? ")
    if mampir == 'y' or mampir == 'Y':
        tambah = input("Masukkan kota yang ingin dilewati : ").upper()
        if tambah in graf.keys():
            lewat.append(tambah)
        else:
            print("Kota tidak terdaftar!!")
    else:
        break

# Menghitung jarak dan rute dari kota awal ke tujuan
if lewat: # Menghitung jika terdapat kota yang harus dilewati
    # Jika terdapat kota tambahan dari kota awal ke kota - kota yang harus dilewati sebelum mencapai tujuan
    jarak_terpendeklewat, rute_terpendeklewat = bfs_shortestpath(graf, mulai.upper(), lewat[0])

    if len(lewat) > 1:
        for i in range(len(lewat)-1):
            jarak_temp, rute_temp = bfs_shortestpath(graf, lewat[i], lewat[i+1])
            jarak_terpendeklewat += jarak_temp
            rute_terpendeklewat += rute_temp[1:]
    
    jarak_terpendek, rute_terpendek = bfs_shortestpath(graf, lewat[-1], tujuan.upper())
    # Menghitung seluruh jarak yang terakumulasi
    totaljarak_terpendek = jarak_terpendeklewat + jarak_terpendek
    # Menggabungkan seluruh rute yang dilewati
    totalrute_terpendek = rute_terpendeklewat + rute_terpendek[1:]
else: # Menghitung jika tidak terdapat kota yang harus dilewati
    # Hasil dari return akan dimasukkan masing - masing secara terpisah ke variabel totaljarak_terpendek dan totalrute_terpendek
    totaljarak_terpendek, totalrute_terpendek = bfs_shortestpath(graf, mulai, tujuan)
   
# Untuk menghitung jumlah rute / node yang dilewati
counter = 0
if totaljarak_terpendek is None:                                 #jika tidak terdapat rute / daerah terisolasi
    print(f"Tidak ada rute dari {mulai} ke {tujuan}.")
else:                                                       #jika terdapat rute untuk mencapai tujuan
    print(f"Diperlukan jarak tempuh sejauh {totaljarak_terpendek}km dan melewati {len(totalrute_terpendek)-2} kota untuk mencapai kota {tujuan} dengan jarak terpendek")
    for i in range(len(totalrute_terpendek)):
        kota = totalrute_terpendek[i]
        if i == len(totalrute_terpendek)-1:
           print(f" hingga tibalah di {kota}")
        elif i == 0:
            print(f"Dimulai dari {kota}", end='')
        elif i % 3 == 0:
            print(f" lalu ke {kota}", end='')
        elif i % 5 == 0:
            print(f" kemudian lewati {kota}", end='')
        elif i % 7 == 0:
            print(f" lanjutkan ke {kota}", end='')
        elif i % 2 == 0:
            print(f" berikutnya {kota}", end='')
        else:
            print(f" selanjutnya menuju {kota}", end='')

print("Rute :", " -> ".join(totalrute_terpendek))