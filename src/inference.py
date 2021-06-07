#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from base_service import BaseService

logger = logging.getLogger(__name__)


class Inference(BaseService):
    """
    推理主类，须要继承BaseService，作为推理调用的主方法入口，支持文本字符串、JSON、二进制参数类型(文件、图片)
    方法介绍：
           predict:推理主方法

    __init__ 方法中可定义模型初始化逻辑
    """

    def __init__(self):
        self.load_context()

    def infer(self, data):
        return data

    def load_context(self):
        pass


