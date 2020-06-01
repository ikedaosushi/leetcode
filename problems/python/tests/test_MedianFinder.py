from MedianFinder import MedianFinder


def test_MedianFinder():
    obj = MedianFinder()

    obj.addNum(1)
    obj.addNum(2)
    assert obj.findMedian() == 1.5
    obj.addNum(3)
    assert obj.findMedian() == 2
    obj.addNum(4)
    assert obj.findMedian() == 2.5
    obj.addNum(4)
    assert obj.findMedian() == 3
