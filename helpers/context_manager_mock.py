from unittest.mock import patch, MagicMock, create_autospec, call, Mock
import pytest

# this examples shows how to mock a class that is used as a context manager in another module.
class Myclass:
    def __enter__(self):
        print("Entering context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context")

    def some_method(self):
        return "real value"


@pytest.fixture
def myclass_mock():
    mocked = MagicMock(autospec=Myclass)
    mocked.__enter__.return_value = mocked

    return mocked


@pytest.fixture(autouse=True)
def myclass_class_mock(myclass_mock):
    with patch(
            "module.main.Myclass", autospec=True
    ) as class_mock:
        class_mock.return_value = myclass_mock

        yield class_mock
