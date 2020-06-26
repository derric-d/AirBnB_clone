#!/usr/bin/env python3
'''module for user class '''
from models.base_model import BaseModel


class User(BaseModel):
    '''class for base'''
    email = ""
    password = ""
    first_name = ""
    last_name = ""
