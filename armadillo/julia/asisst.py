import os  



def create_file_folder(file_folder_names=['data', 'result']):
    '''创建常用的辅助文件夹，分别用于存放数据和结果。
    '''
    cwd = os.getcwd()

    for file_folder_name in file_folder_names:
        if os.path.exists(os.path.join(cwd, file_folder_name))==False:
            os.mkdir(os.path.join(cwd, file_folder_name))
            print(f'文件夹{file_folder_name}创建完成!')
        else:
            print(f'文件夹{file_folder_name}已经存在!')



def clean_file_folder(file_folder_path, keyword=None):
    '''删除文件夹下包含关键词的所有文件。
    '''
    files = os.listdir(file_folder_path)
    
    if key_word:
        files_list = [file_name for file_name in files if key_word in file_name]   # 过滤出文件
    else:
        files_list = [file_name for file_name in files]

    files_deleted_cnt = 0
    
    for file_name in files_list:
        file_path = os.path.join(file_folder_path, file_name)
        try:
            os.remove(file_path)
            files_deleted_cnt = files_deleted_cnt + 1
            print(f'文件已删除：{file_path}')
        except OSError as e:
            print(f'Error: {e.strerror}')
    print('-'*60)
    print(f'文件夹:{path}')
    print(f'总文件数：{len(files)}')
    print(f'合计删除{files_deleted_cnt}个文件！')   
    print('-'*60)


