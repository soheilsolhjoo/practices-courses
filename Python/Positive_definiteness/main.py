import numpy as np
import time

# Define your 3x3 Hessian matrix
hessian_matrix = np.array([[2, -1, 0],
                           [-1, 2, -1],
                           [0, -1, 2]])

# Method 1: Cholesky Decomposition
cholesky_times = []
for _ in range(100):
    start_time = time.time()
    try:
        cholesky_decomposition = np.linalg.cholesky(hessian_matrix)
        cholesky_times.append(time.time() - start_time)
    except np.linalg.LinAlgError:
        cholesky_times.append(time.time() - start_time)

cholesky_average_time = sum(cholesky_times) / len(cholesky_times)

# Method 2: Principal Minors and Signs Test (Sylvester's Criterion)
sylvester_times = []
for _ in range(100):
    start_time = time.time()
    principal_minors = [hessian_matrix[0, 0],
                        np.linalg.det(hessian_matrix[:2, :2]),
                        np.linalg.det(hessian_matrix[:3, :3])]
    if all(minor > 0 for minor in principal_minors):
        sylvester_times.append(time.time() - start_time)
    else:
        sylvester_times.append(time.time() - start_time)

sylvester_average_time = sum(sylvester_times) / len(sylvester_times)

# Print average timings
print("Average Timings (100 iterations each):")
print("Method 1 (Cholesky Decomposition) Average Time:", cholesky_average_time, "seconds")
print("Method 2 (Sylvester's Criterion) Average Time:", sylvester_average_time, "seconds")
