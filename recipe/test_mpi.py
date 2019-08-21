from __future__ import print_function #Python 2.7 compatibility
from mpi4py import MPI

comMPI = MPI.COMM_WORLD
rank = comMPI.Get_rank()
nProc = comMPI.Get_size()

print('rank', rank, 'out of', nProc, 'proc.')

