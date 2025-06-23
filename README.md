# PTcell - Single Cell 
PT5B cell in published Cell Reports (2023) paper
https://www.cell.com/cell-reports/fulltext/S2211-1247(23)00585-5?_returnURL=https%3A%2F%2Flinkinghub.elsevier.com%2Fretrieve%2Fpii%2FS2211124723005855%3Fshowall%3Dtrue

# PTcell
## Description
A model of mouse primary motor cortex (M1) pyramdial tract project (PT) corticospinal cell

Developed using NetPyNE (www.neurosimlab.org/netpyne)

## Setup and execution

Requires NEURON with Python and MPI support. 

1. Type or `./compile or the equivalent `nrnivmodl mod`. This should create a directory called either i686 or x86_64, depending on your computer's architecture. 
2. To run type: `./runsim [num_proc]' or the equivalent `mpiexec -np [num_proc] nrniv -python -mpi init.py`

## Overview of file structure:

* /init.py: Main executable; calls functions from other modules. Sets what parameter file to use.

* /netParams.py: Network parameters

* /cfg.py: Simulation configuration
