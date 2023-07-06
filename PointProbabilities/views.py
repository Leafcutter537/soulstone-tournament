from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .soulstonesample import get_points_for_n_trials
from .histogrambins import create_histogram_bins

num_trials = 1000

# Create your views here.
def index(request):
        return render(request, 'calculator.html')
    
def results(request):
     try:
          mortal = max(int(request.GET['mortal']),0)
     except:
          mortal = 0 
     try:
          immortal = max(int(request.GET['immortal']),0)
     except:
          immortal = 0
     try:
          eternal = max(int(request.GET['eternal']),0)
     except:
          eternal = 0
     if mortal == 0 and immortal == 0 and eternal == 0:
          messages.info(request, 'You must have at least one soulstone.')
          return redirect('index')
     desired_points = int(request.GET['desiredpoints'])
     points = get_points_for_n_trials(1000, mortal, immortal, eternal)
     more_than_desired = [point for point in points if point >= desired_points]
     percentage_desired = len(more_than_desired) / num_trials * 100
     histogram_bins = create_histogram_bins(points, 11, desired_points)
     context = {'mortal': mortal, 'immortal': immortal, 'eternal': eternal, 'num_trials': num_trials,
                    'percentage_desired': percentage_desired, 'desired_points' : desired_points,
                    'bin_range_0': histogram_bins['bin_ranges'][0], 'bin_count_0' : histogram_bins['bin_counts'][0],
                    'bin_range_1': histogram_bins['bin_ranges'][1], 'bin_count_1' : histogram_bins['bin_counts'][1],
                    'bin_range_2': histogram_bins['bin_ranges'][2], 'bin_count_2' : histogram_bins['bin_counts'][2],
                    'bin_range_3': histogram_bins['bin_ranges'][3], 'bin_count_3' : histogram_bins['bin_counts'][3],
                    'bin_range_4': histogram_bins['bin_ranges'][4], 'bin_count_4' : histogram_bins['bin_counts'][4],
                    'bin_range_5': histogram_bins['bin_ranges'][5], 'bin_count_5' : histogram_bins['bin_counts'][5],
                    'bin_range_6': histogram_bins['bin_ranges'][6], 'bin_count_6' : histogram_bins['bin_counts'][6],
                    'bin_range_7': histogram_bins['bin_ranges'][7], 'bin_count_7' : histogram_bins['bin_counts'][7],
                    'bin_range_8': histogram_bins['bin_ranges'][8], 'bin_count_8' : histogram_bins['bin_counts'][8],
                    'bin_range_9': histogram_bins['bin_ranges'][9], 'bin_count_9' : histogram_bins['bin_counts'][9],
                    'bin_range_10': histogram_bins['bin_ranges'][10], 'bin_count_10' : histogram_bins['bin_counts'][10]}
     return render(request, 'results.html', context)