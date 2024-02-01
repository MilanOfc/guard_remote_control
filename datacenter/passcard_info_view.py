import datacenter.utils as utils
from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.shortcuts import get_object_or_404



def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard.objects, passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []
    for visit in visits:
        duration = utils.get_duration(visit)
        this_passcard_visits.append(
            {
                'entered_at': str(visit.entered_at.strftime("%d %h %Y %H:%M")),
                'duration': utils.format_duration(duration),
                'is_strange': utils.is_visit_long(visit)
            },
        )
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
