import os


"""
获取项目根目录。逻辑是，有 resource 的目录就是根目录。
"""
def find_project_root(current_file=__file__, marker_file='resource'):
    # 获取当前文件的绝对路径
    current_abs_path = os.path.abspath(current_file)

    # 获取当前文件所在的目录
    current_dir = os.path.dirname(current_abs_path)

    # 向上遍历目录树
    while current_dir != '/':  # 停止条件为达到文件系统根目录
        potential_marker_file = os.path.join(current_dir, marker_file)
        if os.path.exists(potential_marker_file):
            return current_dir
        else:
            # 移动到父目录
            parent_dir = os.path.dirname(current_dir)
            if parent_dir == current_dir:
                # 已经在文件系统的根目录
                break
            current_dir = parent_dir

    # 如果没有找到标记文件，返回None
    return None


def get_image_path():
    project_root = find_project_root()
    if project_root:
        print()
    else:
        print("未找到包含 resource 的项目根目录")
    resource_path = os.path.join(project_root, 'resource', 'image')
    return resource_path


def get_picture_path(picture):
    project_root = find_project_root()
    if project_root:
        print()
    else:
        print("未找到包含 resource 的项目根目录")
    resource_path = os.path.join(project_root, 'resource', 'image', picture+'.png')
    return resource_path


