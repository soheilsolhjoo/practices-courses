# On positive definiteness of a Hessain matrix
A Hessian matrix is considered positive definite if it meets a fundamental mathematical criterion that confirms its curvature properties. Specifically, a Hessian matrix associated with a multivariable function is deemed positive definite when all of its principal minors—the determinants of its upper-left submatrices—are positive. This property signifies that the function has a local minimum at the point corresponding to the Hessian matrix. Positive definiteness of the Hessian matrix implies that the function's second-order derivatives are uniformly positive in all directions around the point of interest, signifying a bowl-like shape in the vicinity of the minimum. This crucial concept plays a pivotal role in optimization, ensuring that a given point is indeed a local minimum.

# This code
In this code, we first define a 3x3 Hessian matrix that you want to analyze. Then, we proceed with two methods for checking its positive definiteness:

*Cholesky Decomposition*: We attempt Cholesky decomposition for the matrix in a loop 100 times. Cholesky decomposition is used to determine if the matrix is positive definite. We measure the execution time for each attempt and calculate the average execution time over the 100 iterations.

*Sylvester's Criterion*: We apply Sylvester's Criterion for positive definiteness in a loop 100 times. We calculate the principal minors of the matrix and check if they are all positive. Similar to the Cholesky method, we measure the execution time for each attempt and calculate the average execution time.

Finally, we print the average execution times for both methods. This allows you to compare the performance of Cholesky Decomposition and Sylvester's Criterion over multiple iterations and get a sense of which method is more efficient for your specific matrix and computational environment.

**This code is written using OpenAI ChatGPT-3.5.**