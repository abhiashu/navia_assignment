# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from django.contrib.postgres.search import TrigramDistance, TrigramSimilarity

from .models import *

# Create your views here.
def search(request):
    # print("in search function")
    ctx = {}
    query_param = str(request.GET.get("q1"))
    search_cat = str(request.GET.get("q2", 'all')).lower()
    if query_param not in [None, "", " "]:
        query_param = str(query_param.strip())
        if (search_cat in ['all', 'search_options']):
            # medicines = medicineDetail.objects.annotate(search=SearchVector('sku_name', 'manufacturer_name', 'salt_name')).filter(
            #     search=query_param)
            vector = SearchVector('sku_name', weight='A') + SearchVector('manufacturer_name',weight='B')+SearchVector('salt_name',weight='C')
            query = SearchQuery(query_param)

            medicines = medicineDetail.objects.annotate(
                # similarity=TrigramSimilarity(
                #     'sku_name', query_param
                # )*0.5 + TrigramSimilarity(
                #     'manufacturer_name', query_param
                # )*0.4 + TrigramSimilarity(
                #     'salt_name', query_param
                # )*0.1,
                distance=TrigramDistance(
                    'sku_name', query_param
                )*0.5 + TrigramDistance(
                    'manufacturer_name', query_param
                )*0.4 + TrigramDistance(
                    'salt_name', query_param
                )*0.1,
                rank=SearchRank(
                vector,
                query
                )
            ).order_by(
                   'distance'
            )[:20]
            print(medicines)
        elif search_cat == 'product_name':
            medicines = medicineDetail.objects.annotate(distance=TrigramDistance('sku_name', query_param)) \
                .order_by('distance')[:20]
            # print(medicines)
        elif search_cat == 'manufacturer_name':
            # print("in manu fac")
            medicines = medicineDetail.objects.annotate(distance=TrigramDistance('manufacturer_name', query_param)).order_by('distance')[:20]
            # print(medicines)
        elif search_cat == 'salt_name':
            medicines = medicineDetail.objects.annotate(distance=TrigramDistance('salt_name', query_param)) \
                .order_by('distance')[:20]
    else:
        medicines = medicineDetail.objects.none()

    ctx["medicines"] = medicines
    # print(ctx)
    if request.is_ajax():
        html = render_to_string(
            template_name="navia_home/medicines-results-partial.html", context={"medicines": medicines}
        )
        data_dict = {"html_from_view": html}
        # print(data_dict)
        return JsonResponse(data=data_dict, safe=False)

    return render(request, "navia_home.html", context=ctx)


    # if query_param:
    #     query = query_param.strip()
    #     # print("in if")
    #     medicines = medicineDetail.objects.filter(sku_name__icontains=query_param)
    # else:
    #     # print("in else")
    #     medicines = medicineDetail.objects.none()
    #
    # ctx["medicines"] = medicines
    # print(ctx)
    # if request.is_ajax():
    #     html = render_to_string(
    #         template_name="navia_home/medicines-results-partial.html", context={"medicines": medicines}
    #     )
    #     data_dict = {"html_from_view": html}
    #     # print(data_dict)
    #     return JsonResponse(data=data_dict, safe=False)
    #
    # return render(request, "navia_home.html", context=ctx)
