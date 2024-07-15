import re
import attr
import pytest

def print_obj(obj):
    ''' prints attributes of object merging __dict__ and then dir() '''

    obj_name = obj.__class__.__name__
    names = set()
    names.update(list(obj.__dict__))
    names.update(att for att in dir(obj) if not '__' in att)
    for name in sorted(names):
        try:
            print(f'print_obj | {obj_name}[{name}] = {obj.__dict__[name]}')
        except KeyError:
            print(f'print_obj | {obj_name}.{name} = {getattr(obj, name)}')

@pytest.fixture(params=['test-one-param', 2])
def get_class_request(request):
    ''' adds attributes to the client class '''

    print(f'get_class_request | {id(request) = }')
    print(f'get_class_request | {request.param = }')
    #
    # inject values inside calling class
    #
    print(f'get_class_request | {request.cls = }')
    print(f'get_class_request | setting {request.cls.__name__}.id = {id(request.function)}')
    request.cls.id = id(request.function)
    print(f'get_class_request | setting request.id = {id(request)}')
    request.id = id(request)

@pytest.mark.usefixtures("get_class_request")
class TestFixture:
    def test_fixture(self):
        ''' this will be called two times, one for each param in get_class_request '''
        #
        # class is modified by get_class_request
        #
        print(f'TestFixture::test_fixture | {self.id = }')
        print_obj(self)

@pytest.fixture(params=['test-one-param', 2])
def get_function_request(request):
    ''' returns the request object created from params in fixture '''
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
