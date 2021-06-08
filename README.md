#### 介绍
推理代码开发模版

#### 特性
1.  结合fastml-engine引擎，无需开发Web部分代码，只需关注推理函数代码
2.  将通用流程标准化，可变部分配置化，灵活适用多种场景

#### 框架说明

>工程结构  

```shell script
template-python|
                 --|src 代码:预置推理脚本,自定义脚本
                 --|requirements.txt python依赖配置  
                 --|model 模型文件目录
                 --|README.md 模版说明
                 
```

>文件说明  

```text

  src/inference.py：推理方法实现，详见源码，注意inference.py脚本名称不可修改
  requirements.txt：声明项目python依赖
  model/  默认模型文件目录
```
> inference.py开发
```python
#引入fastml_engine模块，并实现BaseService
from fastml_engine.modelservice import BaseService

#可自行定义<Inference>类名称，作为推理服务接口默认名称
class Inference(BaseService):
    def load_context(self):
        """
        在此加载模型、参数、数据等资源，服务启动会被默认初始化
        """
        print('load resource')
    def infer(self, input_data):
        """
        推理方法，自定义方法实现逻辑
        """
        output_data = input_data
        return output_data

```
```python
from fastml_engine.modelservice import BaseService

#允许定义多个实现类，将被自动注册为推理接口,
#接口名称为/algo/inference1,/algo/inference2
class Inference1(BaseService):
    def load_context(self):
        """
        在此加载模型、参数、数据等资源，服务启动会被默认初始化
        """
        print('load resource')
    def infer(self, input_data):
        """
        推理方法，自定义方法实现逻辑
        """
        output_data = input_data
        return output_data

class Inference2(BaseService):
    def load_context(self):
        """
        在此加载模型、参数、数据等资源，服务启动会被默认初始化
        """
        print('load resource')
    def infer(self, input_data):
        """
        推理方法，自定义方法实现逻辑
        """
        output_data = input_data
        return output_data

```



