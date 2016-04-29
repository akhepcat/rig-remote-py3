#!/usr/bin/env python

# import modules
import pytest
import socket
from modules.ui import RigRemote
from modules.app_config import AppConfig
import Tkinter as tk

#def test_bad_signal_conf():
#    root = tk.Tk()
#    ac = AppConfig("./test/bad-signal-config.file")
#    rr = RigRemote(root, ac)
#    rr.apply_config(ac)

def test_load_conf1():
    root = tk.Tk()
    ac = AppConfig("./test/test-config.file")
    rr = RigRemote(root, ac)
    rr.apply_config(ac)
    assert (rr.params["txt_hostname"].get() == "127.0.0.1")

def test_load_conf2():
    root = tk.Tk()
    ac = AppConfig("./test/test-config.file")
    rr = RigRemote(root, ac)
    rr.apply_config(ac)
    assert (rr.params["txt_port"].get() == "7356")

def test_load_conf3():
    root = tk.Tk()
    ac = AppConfig("./test/test-config.file")
    rr = RigRemote(root, ac)
    rr.apply_config(ac)
    assert (rr.params["txt_range_max"].get() == "160,000")

def test_load_conf4():
    root = tk.Tk()
    ac = AppConfig("./test/test-config.file")
    rr = RigRemote(root, ac)
    rr.apply_config(ac)
    assert (rr.params["txt_range_min"].get() == "159,000")

def test_load_conf5():
    root = tk.Tk()
    ac = AppConfig("./test/test-config.file")
    rr = RigRemote(root, ac)
    rr.apply_config(ac)
    assert (rr.params["cbb_mode"].get() == "")

def test_load_conf6():
    root = tk.Tk()
    ac = AppConfig("./test/test-config.file")
    rr = RigRemote(root, ac)
    rr.apply_config(ac)
    assert (rr.params["txt_interval"].get() == "100")

def test_load_conf7():
    root = tk.Tk()
    ac = AppConfig("./test/test-config.file")
    rr = RigRemote(root, ac)
    rr.apply_config(ac)
    assert (rr.params["txt_passes"].get() == "0")

def test_load_conf8():
    root = tk.Tk()
    ac = AppConfig("./test/test-config.file")
    rr = RigRemote(root, ac)
    rr.apply_config(ac)
    assert(rr.params["ckb_auto_bookmark"].is_checked() == 0)

def test_load_conf9():
    root = tk.Tk()
    ac = AppConfig("./test/test-config.file")
    rr = RigRemote(root, ac)
    rr.apply_config(ac)
    assert (rr.params["txt_frequency"].get() == "")

def test_load_conf10():
    root = tk.Tk()
    ac = AppConfig("./test/test-config.file")
    rr = RigRemote(root, ac)
    rr.apply_config(ac)
    assert(rr.params["ckb_wait"].is_checked() == 0)

def test_load_conf11():
    root = tk.Tk()
    ac = AppConfig("./test/test-config.file")
    rr = RigRemote(root, ac)
    rr.apply_config(ac)
    assert (rr.params["txt_sgn_level"].get() == "-40")

def test_load_conf12():
    root = tk.Tk()
    ac = AppConfig("./test/test-config.file")
    rr = RigRemote(root, ac)
    rr.apply_config(ac)
    assert(rr.params["ckb_log"].is_checked() == 0)

def test_load_conf13():
    root = tk.Tk()
    ac = AppConfig("./test/test-config.file")
    rr = RigRemote(root, ac)
    rr.apply_config(ac)
    assert(rr.params["ckb_record"].is_checked() == 0)


def test_load_conf13():
    root = tk.Tk()
    ac = AppConfig("./test/test-config.file")
    rr = RigRemote(root, ac)
    rr.apply_config(ac)
    assert(rr.params["ckb_auto_bookmark"].is_checked() == 0)

def test_load_conf14():
    root = tk.Tk()
    ac = AppConfig("./test/test-config.file")
    rr = RigRemote(root, ac)
    rr.apply_config(ac)
    assert (rr.params["txt_description"].get() == "")

def test_load_conf15():
    root = tk.Tk()
    ac = AppConfig("./test/test-config.file")
    rr = RigRemote(root, ac)
    rr.apply_config(ac)
    assert (rr.params["cbb_mode"].current() == 0)

def test_load_conf16():
    root = tk.Tk()
    ac = AppConfig("./test/test-config.file")
    rr = RigRemote(root, ac)
    rr.apply_config(ac)
    assert (rr.params["cbb_mode"].config()["values"][4] == ('', 'OFF', 'RAW', 'AM', 'FM', 'WFM', 'WFM_ST', 'LSB', 'USB', 'CW', 'CWL', 'CWU'))



