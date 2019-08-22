#coding:utf-8
'''
founction：用于存储变量的类
即是excel中每个参数所处的列
'''

class Global_var():
    id = '0'
    module_name = '1'
    url = '2'
    run = '3'
    request_method = '4'
    header = '5'
    case_depend_id = '6'
    data_depend = '7'
    field_case_depend = '8'
    request_data = '9'
    expect_result = '10'
    infact_result = '11'

def get_id():
    return Global_var.id

def get_module_name():
    return Global_var.module_name

def get_url():
    return Global_var.url

def get_request_method():
    return Global_var.request_method

def get_header():
    return Global_var.header

def get_case_depend_id():
    return Global_var.case_depend_id

def get_data_depend():
    return Global_var.data_depend

def get_field_case_depend():
    return Global_var.field_case_depend

def get_request_data():
    return  Global_var.request_data

def get_expext_result():
    return Global_var.expect_result

def get_infact_result():
    return Global_var.infact_result