from django.shortcuts import render,  get_object_or_404
from .models import MicroVsPlants, Plants, Microorganisms
from django.db.models import Count
# Create your views here.


def main_page(request):
    return render(request, 'main/main.html')


from django.shortcuts import render
from django.db.models import Count
from .models import MicroVsPlants


def plant_page(request):
    # Get filter parameters from the request (query string)
    common_name = request.GET.get('common_name', '').strip()
    scientific_name = request.GET.get('scientific_name', '').strip()
    microorganism_name = request.GET.get('microorganism_name', '').strip()

    # Start with the full queryset
    data = MicroVsPlants.objects.values(
        'plant__id',
        'plant__common_name',
        'plant__scientific_name',
        'micro__id',
        'micro__name'
    )

    # Apply filters if values are provided
    if common_name:
        data = data.filter(plant__common_name__icontains=common_name)
    if scientific_name:
        data = data.filter(plant__scientific_name__icontains=scientific_name)
    if microorganism_name:
        data = data.filter(micro__name__icontains=microorganism_name)

    # Annotate with the count of records for each plant/microorganism combination
    data = data.annotate(record_count=Count('id'))

    context = {
        'data': data,
        'common_name': common_name,
        'scientific_name': scientific_name,
        'microorganism_name': microorganism_name
    }

    return render(request, 'main/plant.html', context)


def plant_view_page(request, plant_id, micro_id):
    tests = MicroVsPlants.objects.filter(plant_id=plant_id, micro_id=micro_id)
    context = {'tests': tests}
    return render(request, 'main/plant_view.html', context)


def detail_view(request, test_id):
    test_detail = get_object_or_404(MicroVsPlants, pk=test_id)
    return render(request, 'main/plant_view_info.html', {'detail': test_detail})


def compounds_page(request):
    return render(request, 'main/compounds.html')