#### 介绍
自定义推理代码开发模版

#### 框架说明

>工程结构  

```shell script
template-python|
                 --|src -->代码:预置推理脚本,自定义脚本
                 --|conf -->配置文件:可编辑修改
                 --|requirements.txt
                 --|README.md 模版说明
                 --|model 模型路径
```

>文件说明  

src/base_service.py：抽象基类，定义基础方法。详见源码


src/inference.py：推理实现类，详见源码


conf/endpoint.json：接口配置，与推理脚本对应，支持多个推理脚本，提供多个服务接口  
```json
[
  {
    "script_name": "inference",
    "subclass_name": "Inference"
  }
]
```

/requirements.txt：声明Python依赖配置，示例如下  
```properties
numpy
tensorflow==1.13.1
```

#### 特性
1.  结合fastml-engine引擎，无需开发Web部分代码，只需关注推理函数代码  
2.  将通用流程标准化，可变部分配置化，灵活适用多种场景  