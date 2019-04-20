# encoding:utf-8
"""
在中国境内，通过访问已知非法域名的IP地址和端口号，验证其是否可获取网页内容。
"""
import pycurl
import StringIO

def get_web_content(domain, ip, port):
    c=pycurl.Curl()
    # 配置
    c.setopt(pycurl.USERAGENT,"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36")  # 设置user-agent
    c.setopt(pycurl.CONNECTTIMEOUT, 5)  # 连接的等待时间，设置为0则不等待
    c.setopt(pycurl.TIMEOUT, 5)  # 请求超时时间

    if port== 443:
        url = 'https://' + domain

    else:
        url = 'http://' + domain
    c.setopt(pycurl.URL, url)
    resolve_url = ':'.join([domain,str(port),ip])
    c.setopt(pycurl.RESOLVE,[resolve_url])
    b = StringIO.StringIO()
    c.setopt(pycurl.WRITEFUNCTION, b.write)

    #c.setopt(c.FOLLOWLOCATION, 1)
    #c.setopt(c.HEADER, True)
    c.perform()
    page = b.getvalue()
    b.close()
    c.close()
    return page


if __name__ == '__main__':

    # domain = 'xitenow.com'
    # domain = 'www.youtube.com'
    # port = 443
    # port = 80
    # ip = '192.96.205.3'
    # ip = '2404:6800:4005:811::200e'
    # curl https://www.theporndude.com/ --resolve "www.theporndude.com:443:104.17.34.108"
    domain = 'www.jiji.com'
    ip = '104.17.34.108'
    port = 443
    page = get_web_content(domain, ip, port)
    fp = open('test.html','w')
    fp.write(page)
    fp.close()