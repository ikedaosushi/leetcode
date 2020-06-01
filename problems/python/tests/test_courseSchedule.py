import pytest
from courseSchedule import Solution


@pytest.mark.parametrize("numCourses,prerequisites,expected", [
    (2, [[1, 0]], True),
    (2, [[1, 0], [0, 1]], False)
])
def test_courseSchedule(numCourses, prerequisites, expected):
    actual = Solution().canFinish(numCourses, prerequisites)
    assert actual == expected
