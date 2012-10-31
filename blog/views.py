from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse

from blog.models import Post, Comment
from blog.forms import CommentForm

def main(request):
    """Main listing of all posts."""

    # Get the list of posts ordered by creation date (descending).
    post_list = Post.objects.all().order_by('-created')
    # Create the paginator configured paginate at 4 posts.
    paginator = Paginator(post_list, 3)

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render_to_response('blog/list.html', {"posts": posts},
                               RequestContext(request))

def post(request, post_id):
    """Single post with comments and comment form"""

    # Handle the case where a post_id doesn't exist in the database.
    post = get_object_or_404(Post, pk=post_id)
    return render_to_response('blog/post.html',
                              {"post": post, "user": request.user},
                               RequestContext(request))
