from collections import deque

# Fungsi BFS untuk mencari rute terpendek dengan bobot terkecil antar kota
def bfs_shortestpath(graf, mulai, tujuan):
    # Queue untuk menyimpan node-node yang dikunjungi
    queue = deque([(mulai, 0)])
    # Set untuk menyimpan node-node yang sudah dikunjungi
    visited = set()

    while queue:
        # penetapan current_node pada antrian pertama ( queue )
        current_node, current_cost = queue.popleft()
        # Jika current_node belum dikunjungi, maka set visited
        if current_node not in visited:
            visited.add(current_node)

            # return current_cost jika node saat ini sama dengan node tujuan
            if current_node == tujuan:
                return current_cost

            # Tambahkan node-node tetangga yang belum dikunjungi ke dalam antrian
            for neighbor, neighbor_cost in graf[current_node].items():
                if neighbor not in visited:
                    total_cost = current_cost + neighbor_cost
                    queue.append((neighbor, total_cost))

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
shortestpath_cost = bfs_shortestpath(graf, mulai, tujuan)

if shortestpath_cost is None:
    print(f"Tidak ada rute dari {mulai} ke {tujuan}.")
else:
    print(f"Rute terpendek dengan bobot terkecil dari {mulai} ke {tujuan} adalah sebesar {shortestpath_cost}.")
