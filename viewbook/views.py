from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import Context
from django.db.models import Q
from books.models import book

# Create your views here.
def renderviewbook(request, book_id):
  book_selected = book.objects.get(pk=book_id)
  related = book.objects.filter(Q(book_author__contains=book_selected.book_author) | Q(genre__contains=book_selected.genre)).exclude(pk=book_id)
  context = Context();
  context['user'] = request.user 
  context['book'] = book_selected
  context['related'] = related
  return render_to_response("viewbook/viewbook.html",context)

