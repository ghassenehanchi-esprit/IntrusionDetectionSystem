from django.http import HttpResponse
from django.shortcuts import render
from .functions import *
import joblib

clf_normal_dt=joblib.load('vot_hard_Normal.sav')
clf_ProbeAttack_dt=joblib.load('vot_hard_Probe.sav')
clf_Dos_dt=joblib.load('vot_hard_Dos.sav')
clf_U2R_dt=joblib.load('vot_hard_U2R.sav')
clf_R2L_dt=joblib.load('vot_hard_R2L.sav')


# List of keys in the desired order


def home(request):
    return render (request,"index.html")
def test(request):
    return render (request,'test.html')
def test_input(request):
    return render(request,'test_input.html')
def result(request):
    list=[]
    keys_in_order = ['duration', 'protocol_type', 'service', 'flag', 'src_bytes',
                 'dst_bytes', 'land', 'wrong_fragment', 'urgent', 'hot',
                 'num_failed_logins', 'logged_in', 'root_shell', 'su_attempted',
                 'num_root', 'num_file_creations', 'num_shells', 'num_access_files',
                 'num_outbound_cmds', 'is_host_login', 'is_guest_login', 'count',
                 'srv_count', 'serror_rate', 'rerror_rate', 'same_srv_rate',
                 'diff_srv_rate', 'srv_diff_host_rate', 'dst_host_count',
                 'dst_host_srv_count', 'dst_host_diff_srv_rate']
    for key in keys_in_order:
        value = request.POST[key]
        list.append(value)
    
    data=preprocessing(list)
    answer=detect_attacks(data,clf_normal_dt,clf_Dos_dt,clf_ProbeAttack_dt,clf_U2R_dt,clf_R2L_dt)
    return render(request,'result.html',{'answer':answer})







