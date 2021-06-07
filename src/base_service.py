import six
import logging
from abc import ABCMeta, abstractmethod

logger = logging.getLogger(__name__)


@six.add_metaclass(ABCMeta)
class BaseService(object):
    """
    推理主类，须要继承BaseService，作为推理调用的主方法入口，支持文本字符串、JSON、二进制参数类型(文件、图片)
    方法介绍：
           predict:推理主方法
    """

    def __init__(self, model_path='model/'):
        """
        :param model_path: 默认路径model
        """
        self.model_path = model_path

    @abstractmethod
    def infer(self, data):
        """
        推理方法
        """
        return data

    @abstractmethod
    def load_context(self):
        pass
