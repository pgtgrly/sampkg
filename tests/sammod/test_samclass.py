from sampkg.sammod import Samclass


def test_samclass():
    x = Samclass()
    assert x.sam_inst_func() == 'hello hello'
    assert x.samstring == 'hello'
    assert Samclass.counter == 1
    y = Samclass("Link")
    assert y.sam_inst_func() == 'hello Link'
    assert y.samstring == 'Link'
    assert y.counter == 2
