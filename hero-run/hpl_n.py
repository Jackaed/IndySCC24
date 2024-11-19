import math
import argparse

def compute_value(N, NB, alpha):
    # Step 1: Get the number of bytes total, factoring in alpha
    bytes_total = 128266124 * 1024 * N * alpha
    
    # Step 2: Divide by 8 to get the number of 8-byte doubles
    num_doubles = bytes_total // 8
    
    # Step 3: Take the square root (square matrix)
    sqrt_value = math.sqrt(num_doubles)

    # Step 4: Round down to the nearest multiple of NB
    rounded_value = int(sqrt_value // NB) * NB
    
    return rounded_value

if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Compute rounded value based on nodes, block size, and alpha.")
    parser.add_argument("N", type=int, help="Number of nodes")
    parser.add_argument("NB", type=int, help="Block size")
    parser.add_argument("alpha", type=float, help="Alpha parameter (0-1) to scale the number of bytes")

    args = parser.parse_args()
    
    # Call the function with command line arguments
    result = compute_value(args.N, args.NB, args.alpha)
    print(result)

