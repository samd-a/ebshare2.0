from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import Context
from django.db.models import Q
from books.models import book, review

# Create your views here.
def renderviewbook(request,book_id):
    book_selected = book.objects.get(pk=book_id)
    related = book.objects.filter(Q(book_author__contains=book_selected.book_author) | Q(genre__contains=book_selected.genre)).exclude(pk=book_id)
    context = {'book': book_selected,'related':related}
    return render(request, "viewbook/viewbook.html", context)

def add_review(request,book_id):
	book_selected = book.objects.get(pk=book_id)
	review(user=request.user,book_review=book_selected,content=request.POST['review'])
	return HttpResponseRedirect('/viewbook/book_id')