import datacenter.utils as utils
from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):
    open_visits = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []
    for visit in open_visits:
        duration = utils.get_duration(visit)
        non_closed_visits.append(
            {
                'who_entered': visit.passcard.owner_name,
                'entered_at': str(visit.entered_at.strftime("%d %h %Y %H:%M")),
                'duration': utils.format_duration(duration),
                'is_strange': utils.is_visit_long(visit)
            }
        )
    context = {
        'non_closed_visits': non_closed_visits
    }
    return render(request, 'storage_information.html', context)
