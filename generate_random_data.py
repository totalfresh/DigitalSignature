import numpy as np

# Helper function to load samples from a file
def load_samples_from_file(filename, num_samples):
    with open(filename, 'r') as file:
        samples = [int(line.strip(), 8) for line in file if line.strip()][:num_samples]
    return samples

# Function to extract bits from samples
def extract_bits(samples, num_bits):
    extracted_bits = []
    for sample in samples:
        extracted_bits.append(sample & ((1 << num_bits) - 1))  # Keep only the last bits
    return extracted_bits

# Tent map function
def tent_map(x, alpha):
    if x < 0.5:
        return alpha * x
    else:
        return alpha * (1 - x)

def generate_random_data():
    # Input parameters for TRNG
    num_bytes = 8192  # Generate more random data
    L = 8  # Size of CCML
    epsilon = 0.001  # Coupling constant
    omega = 0.5  # Weighting coefficient
    gamma = int(np.floor(L / 2))  # Number of iterations
    b = 3  # Number of bits extracted from each sample
    alpha = 1.999999999999999999999999999999999999999999999999999999999999
    num_samples_to_load = 100000  # Number of samples to load

    # Load samples from a text file
    samples = load_samples_from_file('binary_data.txt', num_samples_to_load)
    print(f"Loaded {len(samples)} samples")

    extracted_bits = extract_bits(samples, b)
    print(f"Extracted {len(extracted_bits)} bits")

    # Initialize CCML variables
    x_values = np.array([0.141592, 0.653589, 0.793238, 0.462643, 0.383279, 0.502884, 0.197169, 0.399375])
    x = x_values.copy()
    c = 0  # Counter

    # Main loop of the TRNG algorithm
    O = []  # Output as a list of bits
    while len(O) < num_bytes:
        for i in range(L):
            x[i] = (omega * extracted_bits[c % len(extracted_bits)] / 8 + x[i]) * (1 / (1 + omega))
        c += 1
        for t in range(gamma):
            for i in range(L):
                x[i] = (1 - epsilon) * tent_map(x[i], alpha) + epsilon / 2 * (tent_map(x[(i + 1) % L], alpha) + tent_map(x[(i - 1) % L], alpha))
        for i in range(L):
            z = np.uint64(np.floor(x[i] * 255))  # Ensure values <0; 255>
            O.append(z)
            if len(O) >= num_bytes:
                break
        if len(O) >= num_bytes:
            break

    print(f"Generated {len(O)} bytes of random data")

    # Convert output to bytes
    O_bytes = bytes(O)
    print(f"Generated {len(O_bytes)} bytes of random data for key generation")

    # Save data to a binary file
    with open('static/random_data_for_key.bin', 'wb') as f:
        f.write(O_bytes)

    # Save data to a text file in binary format
    with open('static/random_data_for_key.txt', 'w') as f:
        f.write(''.join(format(byte, '08b') for byte in O_bytes))

    print(f"Saved random data to static/random_data_for_key.bin and static/random_data_for_key.txt")
