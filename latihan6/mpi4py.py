from mpi4py import MPI

def worker(rank, size):
    """Fungsi untuk menjalankan tugas pada proses MPI"""
    print('Worker', rank, 'of', size)
if _name_ == '_main_':
# Inisialisasi MPI
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()
# Panggil fungsi worker pada setiap proses MPI
    worker(rank, size)