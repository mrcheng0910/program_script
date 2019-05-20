#encoding:utf-8
"""
显示下载进度条，来源https://blog.csdn.net/qq_40666028/article/details/79335961
"""
from urllib import urlretrieve
from tqdm import tqdm


class TqdmUpTo(tqdm):
    # Provides `update_to(n)` which uses `tqdm.update(delta_n)`.

    last_block = 0
    def update_to(self, block_num=1, block_size=1, total_size=None):
        '''
        block_num  : int, optional
            到目前为止传输的块 [default: 1].
        block_size : int, optional
            每个块的大小 (in tqdm units) [default: 1].
        total_size : int, optional
            文件总大小 (in tqdm units). 如果[default: None]保持不变.
        '''
        if total_size is not None:
            self.total = total_size
        self.update((block_num - self.last_block) * block_size)
        self.last_block = block_num
#
eg_link = "ftp://rs.internic.net/domain/root.zone"
file = eg_link.split('/')[-1]
#
with TqdmUpTo(unit='B', unit_scale=True, unit_divisor=1024, miniters=1, desc=file) as t:  # 继承至tqdm父类的初始化参数
    urlretrieve(eg_link, filename=file, reporthook=t.update_to, data=None)
