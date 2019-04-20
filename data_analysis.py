from pandas import DataFrame
# dataframe 分组，并且统计个数，按照降序排序
domain_dns_ip_count = df.groupby('ips').size().sort_values(ascending=False)
domain_dns_ip_count = df['ips'].value_counts(normalize=False)  # 直接用百分比表示