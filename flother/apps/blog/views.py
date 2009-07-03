from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.template import RequestContext

from flother.apps.blog.models import Entry


def entry_index(request):
    """Output the latest ten published blog entries."""
    entries = Entry.objects.published()[:10]
    context = {'entries': entries}
    return render_to_response('blog/entry_index.html', context,
        RequestContext(request))


def entry_archive_year(request, year):
    """Output the published blog entries for a given year."""
    entries = get_list_or_404(Entry.objects.published(), published_at__year=year)
    context = {
        'year': year,
        'entries': entries,
    }
    return render_to_response('blog/entry_archive_year.html', context,
        RequestContext(request))


def entry_detail(request, year, slug):
    """
    Output a full individual entry; this is the view for an entry's
    permalink.
    """
    entry = get_object_or_404(Entry.objects.published(), published_at__year=year,
        slug=slug)
    if not request.user:
        entry.number_of_views += 1
    entry.save()
    context = {'entry': entry}
    return render_to_response('blog/entry_detail.html', context,
        RequestContext(request))