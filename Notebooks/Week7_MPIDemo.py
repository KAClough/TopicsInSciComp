"""
Parallel Hello World
"""

from mpi4py import MPI
import sys

# note: This week I show you some optional content on parallelisation. You should first install MPI4py into your environment, using:

# conda activate myenv
# conda install mpi4py

# Then try running the following code - it must be run on the command line using (e.g. for 4 processes):

# mpirun -n 4 python Week7MPIDemo.py

# (Note that this code is run by each process, so imagine each person (process)
# receiving this code and executing it independently.)

# Find out who you are in the group of MPI processes
comm = MPI.COMM_WORLD
num_ranks = comm.Get_size()
my_rank = comm.Get_rank()

# First just print off your rank
print("Hello, World! I am process " + str(my_rank) + " of " 
                  + str(num_ranks) + " on " + str(comm))

# Wait until everyone gets here before going forward
comm.Barrier()

# This just makes sure the printing is done in the terminal before we move on
# Otherwise the output gets mixed up (even though the program order is right)
sys.stdout.flush()

# Now do some communication with the other ranks
message_value = my_rank
max_rank = num_ranks - 1
if my_rank == 0:
    comm.send(message_value, dest = my_rank+1)
    print("I am the first rank I have no message")
    
elif ((my_rank > 0) and (my_rank < max_rank)) :
    message_received = comm.recv()
    print("I am rank " + str(my_rank) + " with message " 
           + str(message_received))
    comm.send(message_value, dest = my_rank+1)
    
else :
    message_received = comm.recv()
    print("I am the last rank " + str(my_rank) + " with message " 
           + str(message_received))

# For more practise, try implementing the Euler method for N variables as shown in the lecture.

