import requests

response = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA') 

# ����ͨ��requests�����������ӣ���ȡ��ҳ����





from pyquery import PyQuery

document = PyQuery(response.text)

content = document('#js_content').text() # ����ҳ������ȡΪһ���ַ����ı���Ϊ����



# print(content)





import mymodule.stats_word





try:

    if not isinstance(content,str):

        raise ValueError()

    

except ValueError:

    print('����Ĳ����ı���ʽ�����������룺')   

dic = mymodule.stats_word.stats_text_cn(content) # ���ú������зִʲ�ͳ�ƴ�Ƶ

str_1 = str(dic) # ����Ƶͳ�ƽ�����ֵ���ʽ��ת�����ַ���

print(str_1)





import getpass

sender = input('�����뷢��������:')

password = getpass.getpass('�����뷢��������:')

recipients = input('�������ռ�������:') # ����getpass������ʾ�Լ������������



import yagmail

yag=yagmail.SMTP( sender, password, host='smtp.qq.com')

yag.send(recipients,'19100205 Ceaar1978', str_1) # ����yagmail�ⷢ���ʼ�

#�����뷢��������:4655438@qq.com

#Warning: Password input may be echoed.

#�����뷢��������:cerirwzrinsgcaie

#�������ռ�������:pythoncamp@163.com