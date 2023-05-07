import ray
@ray.remote
def worker(num):
    """Fungsi untuk menjalankan tugas pada proses multiprocessing"""
    print('Worker', num)
if _name_ == '_main_':
# Inisialisasi Ray
    ray.init()
# Buat task untuk setiap item secara parallel
    results = [worker.remote(i) for i in range(5)]
# Ambil hasil task secara parallel
    ray.get(results)