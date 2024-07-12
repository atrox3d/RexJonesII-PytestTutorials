import re
import attr
import pytest

def print_obj(obj):
    names = set()
    names.update(list(obj.__dict__))
    names.update(att for att in dir(obj) if not '__' in att)
    for name in sorted(names):
        try:
            print(f'print_obj | obj[{name}] = {obj.__dict__[name]}')
        except KeyError:
            print(f'print_obj | obj.{name} = {getattr(obj, name)}')

@pytest.fixture(params=['test-one-param', 2])
def get_class_request(request):
    print(f'get_request | {id(request) = }')
    print(f'get_request | {request.param = }')
    #
    # inject values inside calling class
    #
    print(request.cls)
    request.cls.id = id(request.function)
    request.id = id(request)

@pytest.mark.usefixtures("get_class_request")
class TestFixture:
    def test_fixture(self):
        print(self.id)
        print_obj(self)

@pytest.fixture(params=['test-one-param', 2])
def get_function_request(request):
    print(f'get_function_request | {id(request) = }')
    print(f'get_function_request | {request.param = }')
    #
    # inject values inside request object
    #
    request.function.id = id(request.function)
    request.id = id(request)
    #
    # return modified request object
    #
    return request

# @pytest.mark.skip
def test_request(get_function_request):
    #
    # get_request is the request object for each param in params (_pytest.fixtures.SubRequest)
    # 
    print(f'test_request | {type(get_function_request) = }')

    print_obj(get_function_request)

    print(f'test_request | {test_request.id = }')
    print(f'test_request | {get_function_request.function.id = }')
    print(f'test_request | {get_function_request.id = }')
    assert id(test_request) == test_request.id
    assert id(get_function_request) == get_function_request.id
