from setuptools import setup

with open("README.md", "r") as f:
      long_description = f.read()


setup(name='armadillo',                                     # 分发名称
      version='1.1.1',
      author="Thomas Young",
      author_email='thomasyounger02@gmail.com',
      description='Tools for Business Analysis',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url = "https://github.com/ThomasYounger02/armadillo",
      packages=['armadillo'],                               # 同级的文件包
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent"
          ],
      zip_safe=False)
