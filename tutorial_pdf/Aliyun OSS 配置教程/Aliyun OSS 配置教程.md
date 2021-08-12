# 账号注册并登录

打开 https://www.aliyun.com/product/oss 官网

![1](.\images\1624498766154.png)

注册账号

![2](.\images\1624498799595.png)

登录

![3](.\images\1624498812186.png)



# 开通对象存储 OSS

1. 进行实名认证 [https://account.console.aliyun.com/v2/#/authc/types](#/authc/types)

2. 点击立即开通
3. 勾选服务协议并点击立即开通

![4](.\images\1624498871753.png)

![5](.\images\1624498877083.png)



# 创建 bucket 

打开 https://oss.console.aliyun.com/bucket 并点击创建 Bucket

![6](.\images\wps1.jpg) 

1. 填写 Bucket 名称

2. 根据用户群体就近选择地域

3. 其他选项根据自己情况选择，作为项目课的连续选择默认就好了

4. 点击确定按钮

![7](.\images\wps2.jpg)



# 创建用户

打开 https://ram.console.aliyun.com/users 并点击创建用户

![8](.\images\wps3.jpg) 

1. 填写登录名称和显示名称

2. 勾选编程访问，控制台访问可选可不选（我们都是用 python 编程进行访问，所以一般不会进行控制台访问）

3. 点击确定创建用户

![9](.\images\wps4.jpg)



# 给用户添加权限

完成上面的操作在用户管理界面 https://ram.console.aliyun.com/users 就可以看到我们刚刚创建的用户了，然后点击添加权限给用户分配权限。

![10](.\images\wps5.jpg) 

1. 查找和 Aliyun OSS 有关的权限

2. 把和 Aliyun OSS 有关的权限都选上

3. 点击确定按钮

![11](.\images\wps6.jpg)



# 获取 AccessKey

在用户管理界面点击之前创建的用户进入详情页。

![12](.\images\wps7.jpg) 

拖到最底部选择创建 AccessKey

![13](.\images\wps8.jpg) 

注意及时保存 AccessKey。弹窗关闭后就无法再次获取对应信息，但是可以随时创建新的 AccessKey。

![14](.\images\wps9.jpg)



# 在项目中配置 Aliyun OSS

1. 安装依赖包 
   1. pip install oss2
   2. pip install django-oss-storage

2. 在 settings.py 中添加 oss 配置

```
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
DEFAULT_FILE_STORAGE = 'django_oss_storage.backends.OssMediaStorage'
TESTING = ((' '.join(sys.argv)).find('manage.py test') != -1)

if TESTING:
  DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
```

3. 比较机密的 AccessKey 信息可以配置在 local_settings.py 里

```
OSS_ACCESS_KEY_ID = 'YOUR_ACCESS_KEY_ID'
OSS_ACCESS_KEY_SECRET = 'YOUR_SECRET_ACCESS_KEY'
OSS_ENDPOINT = 'oss-cn-hangzhou.aliyuncs.com'  # 访问域名, 根据服务器上的实际配置修改
OSS_BUCKET_NAME = 'YOUR_BUCKET_NAME'  # oss 创建的 BUCKET 名称
```