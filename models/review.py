#!/usr/bin/env python3
'''module for reviews'''
from models.base_model import BaseModel


class Review(BaseModel):
    '''class for review'''
    place_id = ""
    user_id = ""
    text = ""
