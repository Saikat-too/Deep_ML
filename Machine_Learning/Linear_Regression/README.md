# Linear Regression

Linear regression is a popular regression learning algorithm that learns a model which is a linear combination of features fo the input example.

## 3.1

We have a collection of labeled examples ${(x_i , y_i)}_{i=1}^{N}$----------(1) , where $N$ is the size of the collection, ${x_i}$ is the $D$-dimensional
feature vector of example i = 1, ...., N, ${y_i}$ is real-valued target and every feature ${x_i}^{(j)}$ , j = 1 , ... ,D, is also a real
number.

Builiding a model $f_{w,b}(X)$ as alinear combination of features of example $\mathbf{x}$: $\mathbf{f_{w,b}(x) = wx + b}$ , where $\mathbf{w}$ is
a D-dimensional vector of parameters and b is  a real number. The notation $f_{w,b}(x)$ means the model $f$ is parameterized by two values
$\mathbf{w}$ and $\mathbf{b}$

## 3.2
$\frac{1}{N}\sum_{i=1..N}(f_{w,b}(x_i)-(y_i))^2$ ---------------(2).
The expression $(f(x_i) - (y_i))^2$ in the above objective is called the $\textbf{loss function}$ . It's a measure of penalty for misclassification of
example $\mathbf{i}$. This particular choice of the losss function is called $\textbf{squared error loss}$ . All model based learning algorithms
have a loss function and what do we do to find the best model is we try to minimize the objective loss , also called the $\textbf{empirical risk}$.
The average loss or empirical risk for a model is the average of all penalties obtained by applying the model to the training data.

Linear models rarely overfit. $\textbf{Overfitting}$ is the property of a model such that the model predicts very well labels of the examples used
during training but frequently makes errors when applied to examples there weren't seen by the learning algorithm during training.

If we can calculate the gradient of the function in eq. 2 , we can then set this gradient to zero and find the solution to a system of equations that
gives us the optimal values $\mathbf{w}$ and $\mathbf{b}$.

## Normal Equation

The normal equation is a closed form solution to find the value of $\theta$ that minimizes the cost functionn for ordinary linear
regression . Another way to describe the normal equation is an analytical to fnd the coefficients that minimize the loss
function. Linear regression makes a prediction y_hat . $\mathbf{\hat{y} = \theta_{0}x_{0} + \theta_{1}x_{1} + \theta_{2}x_{2} +...+\theta_{n}x_{n}}$.
Where $\mathbf{\theta}$ represents the parameters and $\mathbf{n}$ is the number of features. In vector form $\mathbf{\hat{y}= h(\theta)}$.
$\mathbf{h(\theta)}$ is the hypothesis function.Given this approximate target function. We can use our model to make predictions to determine if our model has learned well
It's important we measure the performance of our model on the training data . For this purpose , we compute a loss function . The goal of the function
is to find $\mathbf{theta}$ that minimize our loss function. Loss function mathmatical form $\mathbf{J(\theta_{0},\theta_{1},...,\theta_{m}) = \frac{1}{2m}\sum_{i=1}^{m}
(h_\theta(x_(i))-y^(i))^2}$  . The  normal equation : $\mathbf{\theta = (X^{T}X)^{-1}X^{T}y}$

## Gradient Descent

$\textbf{MSE(J)} = \frac{1}{2n}\sum_{i=1}^{n}(mx_{i} - y)^2$






After differentiating cost function with respect to the slop or coefficient $\textbf{m}$
$\frac{\partial J}{\partial m} = \frac{1}{n}(mx_{i} - y)x_{i}$

here changing in m will be : $ m = m - learning_rate * \frac{\partial J}{\partial m}$

here J = $\textbf{cost}$ , m = $\textbf{slop/intercept}$ , x = $\textbf{input}$ , y = $\textbf{output}$
