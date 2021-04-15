import time

def generate(size):
    current_index = 0
    samples = []
    while current_index < size:
        sample = current_index + 1
        samples.append(sample)
        current_index += 1
    return samples