from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from .models import Asset, Software, Server, NetworkDevice, StorageDevice, SecurityDevice, EventLog
from login.models import LoginLog, User
from django.urls import reverse
from django.shortcuts import get_object_or_404, get_list_or_404
from .forms import SoftwareForm
# from django.contrib.auth.decorators import login_required
from util.tool import login_required, post_required
# Create your views here.


def event_log(name, event_type, asset, new_asset, component, detail, user, address, useragent, memo=None):
    event = EventLog()
    event.name = name
    event.event_type = event_type
    event.asset = asset
    event.new_asset = new_asset
    event.component = component
    event.detail = detail
    event.user = user
    event.address = address
    event.useragent = useragent
    event.memo = memo
    event.save()
    
    
@login_required
def index(request):
    # assets = get_list_or_404(Asset)
    total = Asset.objects.count()
    if total == 0:  # 访问系统无数据时, 0 做除数报错
        total = 1
    upline = Asset.objects.filter(status=0).count()
    offline = Asset.objects.filter(status=1).count()
    unknown = Asset.objects.filter(status=2).count()
    breakdown = Asset.objects.filter(status=3).count()
    backup = Asset.objects.filter(status=4).count()
    up_rate = round(upline / total * 100)
    o_rate = round(offline / total * 100)
    un_rate = round(unknown / total * 100)
    bd_rate = round(breakdown / total * 100)
    bu_rate = round(backup / total * 100)
    server_number = Server.objects.count()
    networkdevice_number = NetworkDevice.objects.count()
    storagedevice_number = StorageDevice.objects.count()
    securitydevice_number = SecurityDevice.objects.count()
    software_number = Software.objects.count()
    return render(request, 'assets/index.html', locals())


@login_required
def hardware_assets(request):
    # assets = get_list_or_404(Asset)
    assets = Asset.objects.all()
    return render(request, 'assets/hardware.html', locals())


@login_required
@post_required
def delete_hardware_assets(request):
    pk = request.POST.get('id')
    asset = get_object_or_404(Asset, pk=pk)
    asset_name = asset.name
    asset_sn = asset.sn
    asset.delete()
    name = "删除硬件资产"
    event_type = 3
    asset = None
    new_asset = None
    component = None
    detail = "删除硬件资产：{0}_{1}".format(asset_name, asset_sn)
    username = request.session.get('username')
    user = User.objects.get(username=username)
    address = request.META.get('REMOTE_ADDR', None)
    useragent = request.META.get('HTTP_USER_AGENT', None)
    event_log(name, event_type, asset, new_asset, component, detail, user, address, useragent)
    return JsonResponse({"code": 200, "err": ""})


@login_required
@post_required
def add_hardware_assets(request):
    pass
    return JsonResponse({"code": 200, "err": ""})
    

@login_required
def software_assets(request):
    # assets = get_list_or_404(Asset)
    assets = Software.objects.all()
    return render(request, 'assets/software.html', locals())


# @csrf_exempt
@login_required
@post_required
def delete_software_assets(request):
    pk = request.POST.get('id')
    asset = get_object_or_404(Software, pk=pk)
    asset_id = asset.id
    asset_version = asset.version
    asset.delete()
    name = "删除软件资产"
    event_type = 3
    asset = None
    new_asset = None
    component = None
    detail = "删除软件资产：{0}_{1}".format(asset_id, asset_version)
    username = request.session.get('username')
    user = User.objects.get(username=username)
    address = request.META.get('REMOTE_ADDR', None)
    useragent = request.META.get('HTTP_USER_AGENT', None)
    event_log(name, event_type, asset, new_asset, component, detail, user, address, useragent)
    return JsonResponse({"code": 200, "err": ""})


@login_required
@post_required
def add_software_assets(request):
    softwareform = SoftwareForm(request.POST)
    if softwareform.is_valid():
        if Software.objects.filter(version=softwareform.cleaned_data.get('version')).count() > 0:
            error_message = '{} 已存在!'.format(softwareform.cleaned_data.get('version'))
            return JsonResponse({"code": 400, "err": error_message})
        software = Software()
        software.sub_asset_type = int(softwareform.cleaned_data.get('subassettype'))
        software.license_num = int(softwareform.cleaned_data.get('licensenum'))
        software.version = softwareform.cleaned_data.get('version')
        software.save()
        name = "新增软件资产"
        event_type = 1
        asset = None
        new_asset = None
        component = None
        detail = "新增软件资产：{0}".format(software.version)
        username = request.session.get('username')
        user = User.objects.get(username=username)
        address = request.META.get('REMOTE_ADDR', None)
        useragent = request.META.get('HTTP_USER_AGENT', None)
        event_log(name, event_type, asset, new_asset, component, detail, user, address, useragent)
        return JsonResponse({"code": 200, "err": ""})
    else:
        error_message = '请检查填写的内容!'
        return JsonResponse({"code": 401, "err": error_message})


@login_required
def detail(request, asset_id):
    # assets = get_list_or_404(Asset)
    asset = get_object_or_404(Asset, id=asset_id)
    return render(request, 'assets/detail.html', locals())


@login_required
def operation(request):
    events = EventLog.objects.all()
    return render(request, 'assets/audit_operation.html', locals())


@login_required
def audit_login(request):
    # assets = get_list_or_404(Asset)
    events = LoginLog.objects.all()
    return render(request, 'assets/audit_login.html', locals())
    
    