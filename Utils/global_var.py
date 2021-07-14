#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: global_var.py
# Author: zhouhanjiang@xunlei.com
# Create: 2021/03/30 17:30
# LastMod: 2021/04/23 14:38


"""
    global_var.py
"""

# import os

# from xldllib_common.until.logger import get_logger
# from xldllib_common.until.logger import set_global_logger_level
import xldllib_common.config.base_config as base_config

# logger = get_logger(os.path.basename(os.path.abspath(__file__)), os.path.abspath(__file__), level="INFO",
#                     log_file_max_bytes=1024 * 1024, log_to_file=True)

import xldllib_common.until.basic_tool_base as basic_tool_base
import xldllib_common.until.system_tool_base as system_tool_base

# set_global_logger_level("global_var","DEBUG")

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

'''
'全局变量操作函数实现区域
'''

globalvardict = {}


def set_global_var_dict(key, value):
    """
    设置全局变量到字典
    :param key: 键值
    :param value: 值
    :return:
    """

    try:
        # logger.debug("set_global_var_dict:key=" + str(key))
        if str(key).lower() == "xlluarunscript" or str(key).lower() == "validurllist" or str(key).lower() == "urllist":
            # logger.debug("get_global_var_dict:key's value no need to writelog")
            pass
        else:
            # logger.debug("set_global_var_dict:value=" + str(value))
            pass
        globalvardict[key] = value
        # logger.debug("set_global_var_dict:succeed")
        return True
    except Exception as msg:
        # logger.warning("err,msg=" + str(msg))
        print(("err,msg=" + str(msg)))
        return False


def get_global_var_dict(key=""):
    """
    :param key: 键值
    :return: 值
    """
    value = None
    try:
        # logger.debug("get_global_var_dict:key=" + str(key))
        if key in globalvardict:
            # logger.debug("get_global_var_dict:succeed")
            if str(key).lower() == "xlluarunscript" or str(key).lower() == "validurllist" or str(
                    key).lower() == "urllist":
                # logger.debug("get_global_var_dict:key's value no need to writelog")
                pass
            else:
                # logger.debug("get_global_var_dict:value=" + str(globalvardict[key]))
                pass
            value = globalvardict[key]
            return value
        else:
            # logger.debug("get_global_var_dict:failed.no value found")
            return value
    except Exception as msg:
        # logger.warning("err,msg=" + str(msg))
        print(("err,msg=" + str(msg)))
        return value


# 获取ES统计上报TestData字典
def get_download_lib_es_test_data_dict():
    """

        :return:
    """

    download_lib_es_test_data_dict = {}
    try:
        download_lib_es_test_data_dict = get_global_var_dict("download_lib_es_test_data_dict")
        if download_lib_es_test_data_dict is None:
            download_lib_es_test_data_dict = {}

        test_data = get_global_var_dict("test_data")
        if not isinstance(test_data, dict):
            test_data = base_config.dllib_test_data_dict_default
            # test_data = str(test_data).replace("'", "").replace('"', "").strip()
            set_global_var_dict("test_data", test_data)

        download_lib_es_test_data_dict = test_data

        device_id = get_global_var_dict("device_id")
        if not isinstance(device_id, str):
            device_id = str(system_tool_base.get_sys_hostname()).replace("'", "").replace('"', "").strip()
            device_id = str(device_id).replace("'", "").replace('"', "").strip()
            set_global_var_dict("device_id", device_id)
        download_lib_es_test_data_dict["device_id"] = device_id
        set_global_var_dict("download_lib_es_test_data_dict", download_lib_es_test_data_dict)

        tested_service_name = get_global_var_dict("tested_service_name")
        if not isinstance(tested_service_name, str):
            tested_service_name = base_config.dllib_tested_service_name_default
            tested_service_name = str(tested_service_name).replace("'", "").replace('"', "").strip()
            set_global_var_dict("tested_service_name", tested_service_name)
        download_lib_es_test_data_dict["tested_service_name"] = tested_service_name
        set_global_var_dict("download_lib_es_test_data_dict", download_lib_es_test_data_dict)

        udid = get_global_var_dict("udid")
        if not isinstance(udid, str):
            udid = str(system_tool_base.get_udid()).replace("'", "").replace('"', "").strip()
            udid = str(udid).replace("'", "").replace('"', "").strip()
            set_global_var_dict("udid", udid)
        download_lib_es_test_data_dict["udid"] = udid
        set_global_var_dict("download_lib_es_test_data_dict", download_lib_es_test_data_dict)

        tested_case_path = get_global_var_dict("tested_case_path")
        if not isinstance(tested_case_path, str):
            tested_case_path = base_config.es_report_log_tested_case_path_default
            tested_case_path = str(tested_case_path).replace("'", "").replace('"', "").strip()
            set_global_var_dict("tested_case_path", tested_case_path)
        download_lib_es_test_data_dict["tested_case_path"] = tested_case_path
        set_global_var_dict("download_lib_es_test_data_dict", download_lib_es_test_data_dict)

        time_stamp = get_global_var_dict("time_stamp")
        if not isinstance(time_stamp, str):
            time_stamp = str(basic_tool_base.get_now_time())
            time_stamp = str(time_stamp).replace("'", "").replace('"', "").strip()
            set_global_var_dict("time_stamp", time_stamp)
        download_lib_es_test_data_dict["time_stamp"] = time_stamp
        set_global_var_dict("download_lib_es_test_data_dict", download_lib_es_test_data_dict)

        failed_reason = get_global_var_dict("failed_reason")
        if not isinstance(failed_reason, int):
            failed_reason = base_config.dllib_test_job_failed_reason_default
            # failed_reason = str(failed_reason).replace("'", "").replace('"', "").strip()
            set_global_var_dict("failed_reason", failed_reason)
        download_lib_es_test_data_dict["failed_reason"] = failed_reason
        set_global_var_dict("download_lib_es_test_data_dict", download_lib_es_test_data_dict)

        group_id = get_global_var_dict("group_id")
        if not isinstance(group_id, str):
            group_id = base_config.dllib_test_group_id_default
            group_id = str(group_id).replace("'", "").replace('"', "").strip()
            set_global_var_dict("group_id", group_id)
        download_lib_es_test_data_dict["group_id"] = group_id
        set_global_var_dict("download_lib_es_test_data_dict", download_lib_es_test_data_dict)

        job_description = get_global_var_dict("job_description")
        if not isinstance(job_description, str):
            job_description = base_config.dllib_test_job_description_default
            job_description = str(job_description).replace("'", "").replace('"', "").strip()
            set_global_var_dict("job_description", job_description)
        download_lib_es_test_data_dict["job_description"] = job_description
        set_global_var_dict("download_lib_es_test_data_dict", download_lib_es_test_data_dict)

        product_version = get_global_var_dict("product_version")
        if not isinstance(product_version, str):
            product_version = base_config.dllib_test_product_version_default
            product_version = str(product_version).replace("'", "").replace('"', "").strip()
            set_global_var_dict("product_version", product_version)
        download_lib_es_test_data_dict["product_version"] = product_version
        set_global_var_dict("download_lib_es_test_data_dict", download_lib_es_test_data_dict)

        start_time = get_global_var_dict("start_time")
        if not isinstance(start_time, int):
            start_time = basic_tool_base.get_now_second_from_unixtime()
            # start_time = str(start_time).replace("'", "").replace('"', "").strip()
            set_global_var_dict("start_time", start_time)
        download_lib_es_test_data_dict["start_time"] = start_time
        set_global_var_dict("download_lib_es_test_data_dict", download_lib_es_test_data_dict)

        stop_time = get_global_var_dict("stop_time")
        if not isinstance(stop_time, int):
            stop_time = basic_tool_base.get_now_second_from_unixtime()
            # stop_time = str(stop_time).replace("'", "").replace('"', "").strip()
            set_global_var_dict("stop_time", stop_time)
        download_lib_es_test_data_dict["stop_time"] = stop_time
        set_global_var_dict("download_lib_es_test_data_dict", download_lib_es_test_data_dict)

        run_time = get_global_var_dict("run_time")
        if not isinstance(run_time, int):
            if isinstance(start_time, int) and isinstance(stop_time, int):
                run_time = stop_time - start_time
            else:
                run_time = -1  # basic_tool_base.get_now_second_from_unixtime()
            # run_time = str(run_time).replace("'", "").replace('"', "").strip()
            set_global_var_dict("run_time", run_time)
        download_lib_es_test_data_dict["run_time"] = run_time
        set_global_var_dict("download_lib_es_test_data_dict", download_lib_es_test_data_dict)

        task_id = get_global_var_dict("task_id")
        if not isinstance(task_id, str):
            task_id = base_config.dllib_test_task_id_default
            task_id = str(task_id).replace("'", "").replace('"', "").strip()
            set_global_var_dict("task_id", task_id)
        download_lib_es_test_data_dict["task_id"] = task_id
        set_global_var_dict("download_lib_es_test_data_dict", download_lib_es_test_data_dict)

        url = get_global_var_dict("url")
        if not isinstance(url, str):
            url = base_config.dllib_test_url_default
            url = str(url).replace("'", "").replace('"', "").strip()
            set_global_var_dict("url", url)
        download_lib_es_test_data_dict["url"] = url
        set_global_var_dict("download_lib_es_test_data_dict", download_lib_es_test_data_dict)

        set_global_var_dict("download_lib_es_test_data_dict", download_lib_es_test_data_dict)
        test_data = download_lib_es_test_data_dict
        set_global_var_dict("test_data", test_data)

        return download_lib_es_test_data_dict
    except Exception as msg:
        # logger.warning("err,msg=" + str(msg))
        print(("err,msg=" + str(msg)))
        return download_lib_es_test_data_dict


# 获取ES统计上报 DownloadTestESDataBase 字典
def get_download_test_es_data_base_dict():
    """
        get_download_test_es_data_base_dict
        DownloadTestESDataBase
    """
    download_test_es_data_base_dict = {}
    download_lib_es_test_data_dict = get_download_lib_es_test_data_dict()
    download_test_es_data_base_dict["UDID"] = download_lib_es_test_data_dict["udid"]
    download_test_es_data_base_dict["DeviceID"] = download_lib_es_test_data_dict["device_id"]
    download_test_es_data_base_dict["TestedServiceName"] = download_lib_es_test_data_dict["tested_service_name"]
    return download_test_es_data_base_dict


# 获取ES统计上报日志基准字典
def get_download_lib_es_log_dict():
    """
        http://wiki.xunlei.cn/pages/viewpage.action?pageId=61327823#hub%E5%B7%A5%E5%85%B7&http%E6%8E%A5%E5%8F%A3_20210222-%E4%BC%A0%E8%BE%93%E5%BA%93ES%E6%97%A5%E5%BF%97%E4%B8%8A%E6%8A%A5
        :return:
    """

    download_lib_es_log_dict = {}
    try:
        download_test_es_data_base_dict = get_download_test_es_data_base_dict()
        download_lib_es_log_dict["DownloadTestESDataBase"] = download_test_es_data_base_dict

        download_lib_es_test_data_dict = get_download_lib_es_test_data_dict()

        download_lib_es_log_dict["Timestamp"] = str(download_lib_es_test_data_dict["time_stamp"])
        download_lib_es_log_dict["TestCasePath"] = str(download_lib_es_test_data_dict["tested_case_path"])

        return download_lib_es_log_dict
    except Exception as msg:
        # logger.warning("err,msg=" + str(msg))
        print(("err,msg=" + str(msg)))
        return None


# 获取ES上报统计信息基准字典
def get_download_lib_es_result_dict():
    """
        http://wiki.xunlei.cn/pages/viewpage.action?pageId=61327823#hub%E5%B7%A5%E5%85%B7&http%E6%8E%A5%E5%8F%A3_20210222-%E4%BC%A0%E8%BE%93%E5%BA%93ES%E7%BB%9F%E8%AE%A1%E4%B8%8A%E6%8A%A5
        :return:
    """

    download_lib_es_result_dict = {}
    try:
        download_test_es_data_base_dict = get_download_test_es_data_base_dict()
        download_lib_es_result_dict["DownloadTestESDataBase"] = download_test_es_data_base_dict

        download_lib_es_test_data_dict = get_download_lib_es_test_data_dict()

        download_lib_es_result_dict["Timestamp"] = download_lib_es_test_data_dict["time_stamp"]
        download_lib_es_result_dict["JobID"] = str(download_lib_es_test_data_dict["job_description"])
        download_lib_es_result_dict["TaskID"] = str(download_lib_es_test_data_dict["task_id"])
        download_lib_es_result_dict["GroupID"] = str(download_lib_es_test_data_dict["group_id"])
        download_lib_es_result_dict["ProductVersion"] = str(download_lib_es_test_data_dict["product_version"])
        download_lib_es_result_dict["URL"] = str(download_lib_es_test_data_dict["url"])
        download_lib_es_result_dict["TestData"] = str(download_lib_es_test_data_dict)
        download_lib_es_result_dict["TestCasePath"] = str(download_lib_es_test_data_dict["tested_case_path"])
        download_lib_es_result_dict["FailedReason"] = str(download_lib_es_test_data_dict["failed_reason"])
        download_lib_es_result_dict["StartTime"] = str(download_lib_es_test_data_dict["start_time"])
        download_lib_es_result_dict["StopTime"] = str(download_lib_es_test_data_dict["stop_time"])
        download_lib_es_result_dict["RunTime"] = str(download_lib_es_test_data_dict["run_time"])

        return download_lib_es_result_dict
    except Exception as msg:
        # logger.warning("err,msg=" + str(msg))
        print(("err,msg=" + str(msg)))
        return None


# 测试 glboal_var 模块
def test_glboal_var():
    # set_global_logger_level()
    # logger.info("test_glboal_var. start")

    para = "sss"
    set_global_var_dict("para", para)
    para_val = get_global_var_dict("para")
    para_val_type = basic_tool_base.get_para_type(parameter=para_val)
    print("test_glboal_var.para_val(string)=" + str(para_val) + ";para_val_type=" + str(para_val_type))
    # logger.info("test_glboal_var.para_val(string)=" + str(para_val) + ";para_val_type=" + str(para_val_type))
    para = 123
    set_global_var_dict("para", para)
    para_val = get_global_var_dict("para")
    para_val_type = basic_tool_base.get_para_type(parameter=para_val)
    print("test_glboal_var.para_val(string)=" + str(para_val) + ";para_val_type=" + str(para_val_type))
    para = 123.4556
    set_global_var_dict("para", para)
    para_val = get_global_var_dict("para")
    para_val_type = basic_tool_base.get_para_type(parameter=para_val)
    print("test_glboal_var.para_val(string)=" + str(para_val) + ";para_val_type=" + str(para_val_type))
    # logger.info("test_glboal_var.para_val(float)=" + str(para_val) + ";para_val_type=" + str(para_val_type))
    para = True
    set_global_var_dict("para", para)
    para_val = get_global_var_dict("para")
    para_val_type = basic_tool_base.get_para_type(parameter=para_val)
    print("test_glboal_var.para_val(string)=" + str(para_val) + ";para_val_type=" + str(para_val_type))
    # logger.info("test_glboal_var.para_val(boolen)=" + str(para_val) + ";para_val_type=" + str(para_val_type))
    para = None
    set_global_var_dict("para", para)
    para_val = get_global_var_dict("para")
    para_val_type = basic_tool_base.get_para_type(parameter=para_val)
    print("test_glboal_var.para_val(string)=" + str(para_val) + ";para_val_type=" + str(para_val_type))
    # logger.info("test_glboal_var.para_val(NoneType)=" + str(para_val) + ";para_val_type=" + str(para_val_type))
    para = []
    set_global_var_dict("para", para)
    para_val = get_global_var_dict("para")
    para_val_type = basic_tool_base.get_para_type(parameter=para_val)
    print("test_glboal_var.para_val(string)=" + str(para_val) + ";para_val_type=" + str(para_val_type))
    # logger.info("test_glboal_var.para_val(list)=" + str(para_val) + ";para_val_type=" + str(para_val_type))
    para = {}
    set_global_var_dict("para", para)
    para_val = get_global_var_dict("para")
    para_val_type = basic_tool_base.get_para_type(parameter=para_val)
    print("test_glboal_var.para_val(string)=" + str(para_val) + ";para_val_type=" + str(para_val_type))
    # logger.info("test_glboal_var.para_val(dict)=" + str(para_val) + ";para_val_type=" + str(para_val_type))
    para = ()
    set_global_var_dict("para", para)
    para_val = get_global_var_dict("para")
    para_val_type = basic_tool_base.get_para_type(parameter=para_val)
    print("test_glboal_var.para_val(string)=" + str(para_val) + ";para_val_type=" + str(para_val_type))
    # logger.info("test_glboal_var.para_val(tuple)=" + str(para_val) + ";para_val_type=" + str(para_val_type))

    # logger.info("test_glboal_var. end")


if __name__ == '__main__':
    # set_global_logger_level("global_var")

    # logger.info("main.test start")

    # 测试 glboal_var 模块
    test_glboal_var()

    # logger.info("main.test stop")
