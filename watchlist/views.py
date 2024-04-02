# from django.shortcuts import render
# from .models import WatchList
# from django.http import JsonResponse

# #Get all the movies from the data base
# def movie_list(request):
#     movies = Movie.objects.all()
#     data = {
#         'movies':list(movies.values())
#     }
#     return JsonResponse(data)

# #get a single movie base on id
# def movie_details(request, pk):
#     movie = Movie.objects.get(pk=pk)
#     data = {
#         'title': movie.title,
#         'description': movie.description,
#         'active': movie.active
#     }
#     print(movie)
#     return JsonResponse(data)