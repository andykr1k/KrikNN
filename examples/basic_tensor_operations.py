from kriknn.engine.tensor import Tensor


def basic_tensor_operations():
    # Create tensors
    tensor1 = Tensor([[1.0, 2.0], [3.0, 4.0]])
    tensor2 = Tensor([[2.0, 0.0], [1.0, 2.0]])

    # Matrix multiplication
    result_mul = tensor1 @ tensor2
    print("Matrix Multiplication Result:")
    print(result_mul.data)
    # Output: [[4.0, 4.0], [10.0, 8.0]]

    # Addition
    tensor3 = Tensor([[5.0, 6.0], [7.0, 8.0]])
    result_add = tensor1 + tensor3
    print("\nAddition Result:")
    print(result_add.data)
    # Output: [[6.0, 8.0], [10.0, 12.0]]

    # Print shapes
    print("\nShape of tensor1:", tensor1.shape)
    print("Shape of result_mul:", result_mul.shape)
    print("Shape of result_add:", result_add.shape)


if __name__ == "__main__":
    basic_tensor_operations()
