import pytest
import os
from MemorySys import Directory, MAX_BUF_file_SIZE, DIR_MAX_ELEMS


@pytest.fixture
def directory() -> Directory:
    fs = Directory()
    return fs


def test_directory_create():
    fs = Directory()
    fs.create_directory('two')


def test_filesystem_create_multiple_directories():
    fs = Directory()
    first = len(fs.sub_dir)
    fs.create_directory('three')
    fs.create_directory('four')

    assert len(fs.sub_dir) == first + 2


def test_delete_directory():
    fs = Directory()
    fs.create_directory('five')
    first = len(fs.sub_dir)
    fs.delete_directory('five')
    fs.show_subfile()
    #  如果删除后，目录中少了一个元素则通过测试
    #  If an element is missing from the directory after deletion, the test passes
    assert len(fs.sub_dir) == first - 1


def test_create_binary_file():
    fs = Directory()
    first = len(fs.sub_binary_file)
    fs.create_binary_file('seven')
    assert len(fs.sub_binary_file) == first + 1


def test_mov_directory():
    fs = Directory()
    fs.create_directory('six')
    print('------------------------')
    #  将刚才创建的‘seven’文件移入‘six’文件夹，并检测该文件夹中是否包含‘seven’
    #  Try to move the 'seven' file just created into the 'six' folder, and check whether the folder contains' seven '
    fs.move_dir_path(os.getcwd() + '\\test\\seven', os.getcwd() + '\\test\\six')

    assert os.listdir(os.getcwd() + '\\test\\six')[0] == 'seven'
    print()


def test_create_log_file():
    fs = Directory()
    first = len(fs.sub_log_file)
    fs.create_log_file("seven")
    fs.update_log_file("seven", 'test-content')
    fs.delete_log_file("seven")
    #  this is Similar to the test method for creating files previously
    assert len(fs.sub_log_file) == first + 1


def test_create_buffer():
    fs = Directory()
    fs.create_buffer("eight")
    fs.sub_buffer_file[0].push('content1')
    fs.sub_buffer_file[0].push('content2')
    fs.sub_buffer_file[0].push('content3')

    print(fs.sub_buffer_file[0].items)

    assert fs.sub_buffer_file[0].items[2] == 'content3'
    #  检测是否符合队列的数据结构  Check whether the data structure of the queue is met

    try:
        fs.sub_buffer_file[0].push('content4')
    except Exception as e:
        assert e.args[0] == 'The bufferFile size is limited！'
        #  测试是否满足元素的最大数量
    #  Test whether the maximum number of elements is met


def test_delete_buffer():
    fs = Directory()
    fs.create_buffer("nine")
    fs.sub_buffer_file[0].push('content1')
    fs.sub_buffer_file[0].push('content2')
    fs.sub_buffer_file[0].pop()
    print(fs.sub_buffer_file[0].items)
    assert len(fs.sub_buffer_file[0].items) == 1
    #  测试删除功能，比较长度
    #  Test the deletion function and compare the length
