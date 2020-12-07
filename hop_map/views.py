from django.shortcuts import render
from django.http import HttpResponse
from ip2geotools.databases.noncommercial import DbIpCity
from icmplib import ping, multiping, traceroute, Host, Hop


def index(request):
    return render(request, "default.html")

def response(request):
    if request.method == 'POST':
        search = request.POST['site']
        details = []
        i = 0
        hops = traceroute(search)
        # print(hops)
        for hop in hops:
            i = i + 1
            # print(hop.address)
            if (i >= 2):
                response = DbIpCity.get(hop.address, api_key='free')
                '''print(response.ip_address)
                print(response.city)
                print(response.region)
                print(response.country)
                print(response.latitude)
                print(response.longitude)'''
                details.append([hop.address, response.latitude, response.longitude])

        # for detail in details:
        #     long = detail[2]
        #     lat = detail[1]
        #     context = {'long': str(long), 'lat': str(lat)}
        #     return render(request, "response.html", context)

        long = '12.550343'
        lat = '55.665957'
        context = {'long': str(long), 'lat': str(lat)}
        return render(request, "response.html", {'details': details})

    long = '12.550343'
    lat = '55.665957'
    context = {'long': str(long), 'lat': str(lat)}
    return render(request, "response.html", context)