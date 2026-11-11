
import pytest
import torch


@pytest.fixture
def gpu():
    if not torch.cuda.is_available():
        pytest.skip("CUDA GPU is not available")

    return torch.device("cuda")


def test_gpu_available(gpu):
    assert torch.cuda.is_available()


def test_gpu_tensor_computation(gpu):
    a = torch.tensor([1.0, 2.0, 3.0], device=gpu)
    b = torch.tensor([4.0, 5.0, 6.0], device=gpu)

    result = a + b
    expected = torch.tensor([5.0, 7.0, 9.0], device=gpu)

    assert torch.allclose(result, expected)


def test_cpu_gpu_consistency(gpu):
    torch.manual_seed(42)

    a = torch.randn(500, 500)
    cpu_result = torch.matmul(a, a)

    gpu_a = a.to(gpu)
    gpu_result = torch.matmul(gpu_a, gpu_a)

    assert torch.allclose(
        cpu_result,
        gpu_result.cpu(),
        rtol=1e-3,
        atol=1e-4
    )


def test_gpu_matrix_multiplication(gpu):
    a = torch.randn(1000, 1000, device=gpu)
    b = torch.randn(1000, 1000, device=gpu)

    result = torch.matmul(a, b)
    torch.cuda.synchronize()

    assert result.shape == (1000, 1000)
    assert result.device.type == "cuda"
