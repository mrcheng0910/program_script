# windows下使用jupyter有时候不显示print的内容，增加下面五行代码到头部
import sys
stdi, stdo, stde = sys.stdin, sys.stdout, sys.stderr
reload(sys)
sys.setdefaultencoding('utf-8')
sys.stdin, sys.stdout, sys.stderr = stdi, stdo, stde


# 输入图像要加
%matplotlib inline


# 动态加载import文件
%load_ext autoreload
%autoreload 2

# 保存csv文件时，不保存默认index
df.to_csv('analysis_domain_censor/local_data/b.csv', index=False)

# 同时显示多行
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"