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

mulai = 'A'
tujuan = 'F'
# Untuk menghitung jumlah rute / node yang dilewati
counter = 0
# Hasil dari return akan dimasukkan masing - masing secara terpisah ke variabel jarak_terpendek dan rute_terpendek
jarak_terpendek, rute_terpendek = bfs_shortestpath(graf, mulai, tujuan)


if jarak_terpendek is None:                                 #jika tidak terdapat rute / daerah terisolasi
    print(f"Tidak ada rute dari {mulai} ke {tujuan}")
else:                                                       #jika terdapat rute untuk mencapai tujuan
    print(f"Diperlukan jarak tempuh sejauh {jarak_terpendek}km dan melewati {len(rute_terpendek)-2} kota untuk mencapai kota {tujuan} dengan jarak terpendek")
    for i in rute_terpendek:
        counter += 1
        if i == tujuan:
           print(f" hingga tibalah di {i}")
           # Pengecekan jumlah rute / node ke-n untuk mencapai tujuan
           print(counter)
        elif i == mulai:
            print(f"Dimulai dari {i}", end='')
        elif counter % 3 == 0:
            print(f" lalu ke {i}", end='')
        elif counter % 5 == 0:
            print(f" kemudian lewati {i}", end='')
        else:
            print(f" selanjutnya menuju {i}", end='')

    #print(f"Rute terpendek adalah {rute_terpendek} dengan bobot terkecil dari {mulai} ke {tujuan} sebesar {jarak_terpendek}.")
