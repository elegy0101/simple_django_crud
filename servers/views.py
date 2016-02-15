from django.shortcuts import render, redirect, get_object_or_404
from servers.forms import ServerForm
from servers.models import Server

def servers_list(request, template_name='server_list.html'):
    servers = Server.objects.all()
    data = {}
    data['object_list'] = servers
    return render(request, template_name, data)

def server_create(request, template_name='server_form.html'):
    form = ServerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('servers_list')
    return render(request, template_name, {'form':form})

def server_update(request, pk, template_name='server_form.html'):
    server = get_object_or_404(Server, pk=pk)
    form = ServerForm(request.POST or None, instance=server)
    if form.is_valid():
        form.save()
        return redirect('servers_list')
    return render(request, template_name, {'form':form})

def server_delete(request, pk, template_name='server_confirm_delete.html'):
    server = get_object_or_404(Server, pk=pk)
    if request.method=='POST':
        server.delete()
        return redirect('servers_list')
    return render(request, template_name, {'object':server})
