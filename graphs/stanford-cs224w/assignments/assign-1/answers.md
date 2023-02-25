# Answers

## Ex. 1

$v_a = (1-\beta)\frac{1}{3}(v_1 + v_2 + v_4)$ 

$v_b = (1-\beta)\frac{1}{3}(v_3 + v_4 + v_5)$ 

$v_c = (1-\beta)\frac{1}{2}(v_3 + v_5)$ 

$v_d = (1-\beta)v_2$ 

Rewriting the system with the following auxiliary variables:
- $v_a^{\prime} = \frac{3}{1-\beta}v_a$
- $v_b^{\prime} = \frac{3}{1-\beta}v_b$
- $v_c^{\prime} = \frac{2}{1-\beta}v_c$
- $v_d^{\prime} = \frac{1}{1-\beta}v_d$

So, to find if a new user Pagerank score can be computed in terms of $v_i^{\prime}$ with $i \in \{a, b, c, d\}$,
we need to solve the following system of equations:

$
\begin{bmatrix}
1 & 0 & 0 & 0 \\
1 & 0 & 0 & 1 \\
0 & 1 & 1 & 0 \\
1 & 1 & 0 & 0 \\
0 & 1 & 1 & 0
\end{bmatrix}
$
$
\begin{bmatrix}
c_a \\
c_b \\
c_c \\
c_d 
\end{bmatrix}
$ = $
\begin{bmatrix}
x_1 \\
x_2 \\
x_3 \\
x_4 \\
x_5 
\end{bmatrix}
$ 

where $x_i$ are the coefficients to the teleport sets of the new nodes.

That is:
- $x^{Eloise} = \begin{bmatrix} 1, 0, 0, 0, 0 \end{bmatrix}$
- $x^{Felicity} = \begin{bmatrix} 0, 0, 0, 0, 1 \end{bmatrix}$
- $x^{Glynnis} = \begin{bmatrix} 0.1, 0.3, 0.2, 0.2, 0.2 \end{bmatrix}$

We get:
- $c^{Eloise} = \begin{bmatrix} 1, -1, 1, -1 \end{bmatrix}$
- $c^{Felicity}$ can not be found, as the system has no solution
- $c^{Glynnis} = \begin{bmatrix} 0.1, 0.1, 0.1, 0.2 \end{bmatrix}$

# Question 1.4

The set of personalized PageRank vectors that can be computed are the set of vectors that can be written as a linear combination of $V$.

