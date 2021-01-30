from django.shortcuts import render
from BRMapp.forms import NewbookForm, SearchForm
from django.http import HttpResponse , HttpResponseRedirect
from BRMapp import models

def searchbook(request):
    form=SearchForm()
    res=render(request,'BRMapp/search_book.html',{'form':form})
    return res
def search(request):
    form=SearchForm(request.POST)
    books=models.Book.objects.filter(title=form.data['title'])
    res=render(request,'BRMapp/search_book.html',{'form':form,'books':books})
    return res
def deletebook(request):
    bookid=request.GET['bookid']
    book=models.Book.objects.filter(id=bookid)
    book.delete()
    return HttpResponseRedirect('BRMapp/view-books')
def editbook(request):
    book=models.Book.objects.get(id=request.GET['bookid'])
    fields={'title':book.title,'price':book.price,'author':book.author,'publisher':book.publisher}
    form=NewbookForm(initial=fields)
    res=render(request,'BRMapp/edit_book.html',{'form':form,'book':book})
    return res
def edit(request):
    if request.method=='POST':
        form=NewbookForm(request.POST)
        book=models.Book()
        book.id=request.POST['bookid']
        book.title=form.data['title']
        book.price=form.data['price']
        book.author=form.data['author']
        book.publisher=form.data['publisher']
        book.save()
        return HttpResponseRedirect('BRMapp/view-books')
def viewbooks(request):
    books=models.Book.objects.all()
    res=render(request,'BRMapp/view_book.html',{'books':books})
    return res
def newbook(request):
    form=NewbookForm()
    res=render(request,'BRMapp/new_book.html',{'form':form})
    return res
def add(request):
    if request.method=='POST':
        form=NewbookForm(request.POST)
        book=models.Book()
        book.title=form.data['title']
        book.price=form.data['price']
        book.author=form.data['author']
        book.publisher=form.data['publisher']
        book.save()
    #s="Record Stored<br><a href='/BRMapp/view-books'> View all Books</a>"
    return HttpResponseRedirect('BRMapp/view-books')
