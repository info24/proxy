from unittest import mock
import requests

def get(url):
    return {'code': 1}

@mock.patch('requests.get', get)
def run():
    r = requests.get('http://www.baidu')
    print(r)
'''
mock.path装饰器的第一个参数为要mock被替代的方法
        第二个参数为要执行的方法
'''
run()   # 打印结果为 {'code': 1}

mock_get = mock.Mock(return_value="hello get")

@mock.patch.object(requests, 'get', mock_get)
def goo():
    r = requests.get('hadfadf')
    print(r)
'''
mock.patch.object可以patch一个mock对象
第一个参数为 mock类
第二个参数为 mock方法
第三个参数为 mock对象
'''

goo()   # 打印的结果为'hello get'


goo = mock.Mock(side_effect=[10, 22, 33])   # 调用goo可以依次打印列表
goo()   # 10
goo()   # 22
goo()   # 33

dicts = {'a': 1, 'b': 2}
def side_effect(arg):
    return dicts.get(arg)

foo = mock.Mock(side_effect=side_effect)
foo('a')    # 1


'''
例子讲解
'''
def get():
    return 622
def get_new_jobid():
    return 623

def put_event(a):
    print('put_event')

def get_ip(a):
    return "172.16.1.1"

def get_text(a):
    return '1,2,3,3,4,5'
def write(a):
    pass

@mock.patch('dbjobs.get_last_id', get)
@mock.patch('dbjobs.get_new_jobid', get_new_jobid)
@mock.patch('dbjobs.put_event', put_event)
@mock.patch('dbjobs.get_ip', get_ip)
@mock.patch('dbjobs.get_text', get_text)
@mock.patch('dbjobs.write', write)
def run1():
    '''
    run()函数里有很多调用函数如，get_last_id， get_new_jobid, put_event等等，
    如果这些函数的调用可能存在问题，那么，我们就可以用mock.patch来mock这些函数，
    这样，它就直接调用我们定义的函数
    '''
    r = run()
