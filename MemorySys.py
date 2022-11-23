import os
import shutil
import os.path
import logging

MAX_BUF_file_SIZE = 3
DIR_MAX_ELEMS = 6


class Directory:
    def __init__(self):
        self.name = 'Assignment Directory'
        self.path = os.getcwd() + '\\test'  # 返回当前工作目录  Return to the current working directory
        file_list = os.listdir(self.path)  # 返回当前工作目录包含的文件的列表
        self.sub_dir = []  # 子文件目录
        self.sub_binary_file = []  # 二进制文件
        self.sub_log_file = []  # 日志
        self.sub_buffer_file = []  # 缓冲文件
        for file in file_list:
            filepath = os.path.join(self.path, file)  # 拼接文件路径
            #  Read all files in the current folder
            if os.path.isdir(filepath):
                self.sub_dir.append(filepath)

    def create_directory(self, directory_name):
        list_number = os.listdir(self.path)
        print(len(list_number))
        if len(list_number) < DIR_MAX_ELEMS:
            print("\nThe new name of this new directory: ")
            try:   # 尝试创建文件，如果失败执行‘except’语句
                print(directory_name)
                # 创建新文件并转化为目录格式
                # Create new files and convert to directory format
                os.mkdir(os.path.join(self.path, directory_name))
                self.sub_dir.append(directory_name)
                print("successfully create a directory!")
            except Exception as e:
                print("the directory created failed")
                if e.args[0] == 17:   # 抓取WindowsError，即不允许出现重名
                    # Grab WindowsError, that is, duplicate names are not allowed
                    print("Cannot create a file when it already exists.")

    def delete_directory(self, del_directory_name):

        if del_directory_name not in self.sub_dir:
            print("Directory does not exist")
        else:
            try:
                os.rmdir(os.path.join(self.path, del_directory_name))
                self.sub_dir.remove(del_directory_name)
                #  调用系统函数直接删除文件夹
                print("successfully delete such directory")
            except:
                print("fail to delete")

    def show_subfile(self):
        print("List files and subdirectories: \n")
        for s_dir in self.sub_dir:
            print(s_dir + '\n')
        print()
        # 循环，打印内容
        # Loop, print content

    def move_dir_path(self, dir, path):
        try:
            shutil.move(dir, path)  # shutil.move()实现文件的复制，移动
            print('a successful moving')
        except Exception as e:
            print(e)

    def create_binary_file(self, binary_name):
        list_number = os.listdir(self.path)
        print(len(list_number))
        if len(list_number) < DIR_MAX_ELEMS:
            try:
                # ‘wb' 表示创建的文件为二进制
                # 'wb' indicates that the created file is binary
                fp = open(os.path.join(self.path, binary_name), 'wb')
                print("successfully create a binary file!")
                self.sub_binary_file.append(binary_name)
                return fp
            except:
                print('create file failed')

    def delete_binary_file(self, name):
        try:
            os.remove(name)
        except Exception as e:
            print(e)

    def create_log_file(self, log_name):
        list_number = os.listdir(self.path)
        if len(list_number) < DIR_MAX_ELEMS:
            try:
                logger = logging.getLogger(__name__)
                #  logging.getLogger自动生成系统日志
                # logging.getLogger automatically generates system logs
                logger.setLevel(level=logging.INFO)
                handler = logging.FileHandler(log_name + ".txt")
                # Save the system log as a file
                print("\nsuccessfully create log file!")
                self.sub_log_file.append(log_name)
                return handler
            except:
                print('create log file failed.')
        else:
            print('create log file failed.')

    def delete_log_file(self, name):
        try:
            os.remove(name)
        except Exception as e:
            print(e)

    def update_log_file(self, name, content):
        try:
            with open(name, "a") as f:
                f.write(content)
                #  写入
        except:
            print("write file failed")

    def create_buffer(self, buffer_name):
        list_number = os.listdir(self.path)
        if len(list_number) < DIR_MAX_ELEMS:
            file = BufferFile(buffer_name)
            print("\nsuccessfully create buffer file!")
            self.sub_buffer_file.append(file)
            # 读文件
            return file
        else:
            print("write file failed")


class BufferFile:
    def __init__(self, name):
        self.name = name
        self.items = []
        fp = open(os.path.join(os.getcwd() + '\\test', name), 'wb')
        #  为 Buffer file 创建空间

    def push(self, content):
        if len(self.items) == MAX_BUF_file_SIZE:
            # Judge whether overflow occurs
            raise ValueError("The bufferFile size is limited！")
        #  #Add content from the end
        self.items.append(content)

    def pop(self) -> bool:
        if len(self.items) == 0:
            raise ValueError("Can't move the item from an empty buffer File")
            # Delete content from the end
        return self.items.pop()






