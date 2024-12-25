
import pandas as pd
import sys
import os

def convert_size(size_str):
    size_str = size_str.strip()
    # 根据单位进行转换
    size_value = float(size_str[:-1])
    if size_str.endswith('T'):
        return size_value * 1024 * 1024 * 1024 * 1024
    elif size_str.endswith('G'):
        return size_value * 1024 * 1024 * 1024
    elif size_str.endswith('M'):
        return size_value * 1024 * 1024
    elif size_str.endswith('K'):
        return size_value * 1024
    else:
        return size_value

os.chdir('/Users/wangjien/TEST')
# df = pd.read_csv('20241224统计用户使用空间.txt',sep='\t', header=None, names=['size','user'])
df = pd.read_csv(sys.argv[1],sep='\t', header=None, names=['size','user'])
df['new_size'] = df['size'].apply(lambda x: convert_size(x))
df['user_id'] = df['user'].apply(lambda x: str(x).split('/')[-1])
df = df.sort_values(by='new_size', ascending=False)
# df.to_csv('20241224_new用户空间大小.txt', sep='\t', header=0, index=None)
df.to_csv(sys.argv[2], sep='\t', header=0, index=None)
