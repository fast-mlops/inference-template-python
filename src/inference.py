#!/usr/bin/env python
# -*- coding: utf-8 -*-
from fastml_engine.modelservice import BaseService


class Inference(BaseService):

    def load_context(self):
        """

        """
        print('load resource')

    def infer(self, input_data):
        output_data = input_data
        return output_data
