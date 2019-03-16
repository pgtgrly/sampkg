from sampkg.sammod import Samclass, sam_func


def test_sam_func():
    x = Samclass()
    assert sam_func(x) == '0.00 olleh'
    y = Samclass("Link")
    assert sam_func(y) == '0.69 kniL'
