import subprocess
from itertools import product


def generate_hpl_file(N, NB, P, Q):
    return f"""HPLinpack benchmark input file
Innovative Computing Laboratory, University of Tennessee
HPL.out      output file name (if any)
6            device out (6=stdout,7=stderr,file)
1            # of problems sizes (N)
{N}          Ns
1            # of NBs
{NB}         NBs
0            PMAP process mapping (0=Row-,1=Column-major)
1            # of process grids (P x Q)
{P}          Ps
{Q}          Qs
16.0         threshold
3            # of panel fact
0 1 2        PFACTs (0=left, 1=Crout, 2=Right)
2            # of recursive stopping criterium
2 4          NBMINs (>= 1)
1            # of panels in recursion
2            NDIVs
3            # of recursive panel fact.
0 1 2        RFACTs (0=left, 1=Crout, 2=Right)
1            # of broadcast
0            BCASTs (0=1rg,1=1rM,2=2rg,3=2rM,4=Lng,5=LnM)
1            # of lookahead depth
0            DEPTHs (>=0)
2            SWAP (0=bin-exch,1=long,2=mix)
64           swapping threshold
0            L1 in (0=transposed,1=no-transposed) form
0            U  in (0=transposed,1=no-transposed) form
1            Equilibration (0=no,1=yes)
8            memory alignment in double (> 0)"""


def write_string_to_file(file_name, string):
    with open(file_name, "w+") as f:
        f.write(string)


def grid_search_HPL_parameters():
    DAT_FOLDER = "./attempts"
    RUN_FOLDER = "./basic_hpl_build/bin"
    LOG_FOLDER = "./logs"

    NUM_NODES = "4"
    blas_module = "openblas/0.3.28/gcc"
    mpi_module = "openmpi/5.0.5/gcc"

    Ns = [1, 2, 3, 4]
    NBs = [1, 2, 3, 4]
    PQs = [(1, 2), (3, 4), (5, 6), (7, 8)]

    parameter_combinations = product(Ns, NBs, PQs)

    for N, NB, (P, Q) in parameter_combinations:
        file_name = f"{DAT_FOLDER}/hpl_{N}_{NB}_{P}_{Q}_{NUM_NODES}.dat"
        write_string_to_file(file_name, generate_hpl_file(N, NB, P, Q))

        subprocess.run(["cp", file_name, "."])
        run_hpl(blas_module, mpi_module, NUM_NODES, f"{RUN_FOLDER}/xhpl",
                f"{LOG_FOLDER}/hpl_{N}_{NB}_{P}_{Q}_{NUM_NODES}.log")


def grid_search_build_params():
    compilers = ["gcc", "clang", "icx"]
    blas_libraries = ["openblas", "intelmkl"]
    openmpi_libraries = ["openmpi", "intelmpi"]

    NUM_NODES = 4
    LOG_FOLDER = "./logs"

    parameter_combinations = product(compilers, blas_libraries,
                                     openmpi_libraries)

    bash_script = "./build_hpl.sh"

    for compiler, blas_library, mpi_library in parameter_combinations:
        if mpi_library == "openmpi":
            mpi_library = f"{mpi_library}/5.0.5/{compiler}"

        if blas_library == "openblas":
            blas_library = f"{blas_library}/0.3.28/{compiler}"

        install_dir = f"./hpl_with_{compiler}_{blas_library}_{mpi_library}_{NUM_NODES}"

        subprocess.run(["bash", bash_script, compiler, blas_library,
                        mpi_library, install_dir])
        run_hpl(blas_library, mpi_library, NUM_NODES,
                f"{install_dir}/bin/xhpl",
                f"{LOG_FOLDER}/hpl_{compiler}_{blas_library}_{mpi_library}_{NUM_NODES}.log")


def run_hpl(blas_module, mpi_module, num_nodes, xhpl_path, log_file_path):
    run_script = "./run_hpl.sh"

    subprocess.run(["sbatch", "-N", num_nodes, "-n",
                    str(int(num_nodes)*32), run_script, mpi_module,
                    blas_module, xhpl_path, log_file_path])


if __name__ == "__main__":
    pass
    # write_string_to_file(sys.argv[1], generate_hpl_file(*sys.argv[2:]))
    # grid_search_HPL_parameters()
