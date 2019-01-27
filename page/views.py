from django.shortcuts import render
from .models import Banner
from item.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from pytils.translit import slugify
import os
from PIL import Image

import csv
from django.core.files.storage import FileSystemStorage


def about_us(request):
    return render(request, 'page/about_us.html', locals())

def contacts(request):
    return render(request, 'page/contacts.html', locals())

def dostavka(request):
    return render(request, 'page/dostavka.html', locals())

def new(request):
    items = Item.objects.filter(is_new=True)
    return render(request, 'page/new.html', locals())

def index(request):
    banners = Banner.objects.filter(is_active=True).order_by('-order')
    collections = Collection.objects.filter(show_at_homepage=True)
    main_category = Category.objects.all()

    # ItemImage.objects.create(item_id=1,image='items/1/1201.jpg')
    return render(request, 'page/index.html', locals())


def category(request, cat_slug):
    try:
        cat = Category.objects.get(name_slug=cat_slug)
        subcats = SubCategory.objects.filter(category=cat)
    except:
        return render(request, '404.html', locals())


    return render(request, 'page/category.html', locals())

def subcategory(request, subcat_slug):
    try:
        subcat = SubCategory.objects.get(name_slug=subcat_slug)
        all_items = Item.objects.filter(subcategory_id=subcat.id).order_by('name')
    except:
        return render(request, '404.html', locals())
    data = request.GET
    print(request.GET)
    search = data.get('search')
    filter = data.get('filter')
    order = data.get('order')
    page = request.GET.get('page')
    search_qs = None
    filter_sq = None
    if search:
        items = all_items.filter(name__contains=search)
        search_qs = items
        print(items)
        param_search = search



    if filter == 'new':
        print('Поиск по фильтру туц')
        if search_qs:
            items = search_qs.filter(is_new=True)
            filter_sq = items
            param_filter = filter
        else:
            items = all_items.filter(is_new=True)
            filter_sq = items
            param_filter = filter

        param_filter = 'new'


    if filter and filter != 'new':
        print('Поиск по фильтру')

        if search_qs:
            items = search_qs.filter(filter__name_slug=filter)
            filter_sq = items
            param_filter = filter
        else:
            items = all_items.filter(filter__name_slug=filter)
            filter_sq = items
            param_filter = filter

    if order:
        if search_qs and filter_sq:
            items = filter_sq.order_by(order)
        elif filter_sq:
            items = filter_sq.order_by(order)
        elif search_qs:
            items = search_qs.order_by(order)
        else:
            items = all_items.order_by(order)


        param_order = order


    if not search and not order and not filter:
        items = all_items
        param_order = 'name'


    items_paginator = Paginator(items, 12)

    try:
        items = items_paginator.get_page(page)
    except PageNotAnInteger:
        items = items_paginator.page(1)
    except EmptyPage:
        items = items_paginator.page(items_paginator.num_pages)



    return render(request, 'page/subcategory.html', locals())