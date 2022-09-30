Awesome work! Your implementation is just about perfect. One very small error with the alignment score:

The alignment score is JUST the value in the bottom right of the F-matrix, not the sum of the entire path (which is how you have it now). The F-matrix is already keeping track of the score of the entire path, so you only need the last value in the path (-0.25)

9.75/10
