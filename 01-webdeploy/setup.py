from setuptools import setup

setup(
    name='webdeploy-80',
    version='0.1',
    author='Mark Jones',
    author_email='marks.jones@yahoo.co.uk',
    description='Webdeploy 80 is a tool to deploy static websites to AWS.',
    license='GPLv3+',
    packages=['webdeploy'],
    url='https://github.com/swantaff/automating-aws-with-python/tree/master/01-webdeploy',
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        webdeploy=webdeploy.webdeploy:cli
    '''
)