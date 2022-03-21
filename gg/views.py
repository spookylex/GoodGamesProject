from django.shortcuts import render, redirect

from gg.models import Room, Message, Profile, Review
from django.http import HttpResponse, JsonResponse

def profile(request):
    user_details = Profile.objects.get(name=request.user)
    playsOn = user_details.playsOn.strip('[]').replace('\'', '').split(",")
    socialMediaLinks = user_details.socialMediaLinks.strip('[]').replace('\'', '').split(",")
    favoriteGames = user_details.favoriteGames.strip('[]').replace('\'', '').split(",")
    players = Profile.objects.all().count()+1
    return render(request,'profile.html', {
        'username':user_details.username,
        'socialMediaLinks': socialMediaLinks,
        'playsOn': playsOn,
        'favoriteGames': favoriteGames,
        'players':players
    })

def reviews(request): 
    return render(request, 'reviews.html')

def addReview(request):
    username = request.POST.get('username', False)
    gameTitle = request.POST.get('gameTitle', False)
    reviewTitle = request.POST.get('reviewTitle', False)
    reviewBody = request.POST.get('reviewBody', False)
    rating = request.POST.get('rating', False)

    new_room = Review.objects.create(username=username,gameTitle=gameTitle,reviewTitle=reviewTitle,reviewBody=reviewBody, rating=rating)
    new_room.save()

    return render(request, 'profile.html', {'username' : username, 'gameTitle' : gameTitle, 'reviewTitle': reviewTitle, 'reviewBody':reviewBody,  'rating':rating})

def makeReview(request):
    return render(request, 'makeReview.html')

def homepage(request):
    return render(request, 'homepage.html')

def games(request):
    return render(request, 'games.html')

def games_classic(request):
    return render(request, 'games_classic.html')

def games_fps(request):
    return render(request, 'games_fps.html')

def games_rpg(request):
    return render(request, 'games_rpg.html')

def games_adventure(request):
    return render(request, 'games_adventure.html')

def userCreation(request):
    return render(request, 'makeProfile.html')

def addProfile(request):
    username = request.POST.get('username', False)
    socialMediaLinks = request.POST.get('socialMediaLinks', False).split(",")
    playsOn = request.POST.get('playsOn', False).split(",")
    favoriteGames = request.POST.get('favoriteGames', False).split(",")
    players = Profile.objects.all().count()+1

    new_room = Profile.objects.create(name=request.user,username=username,socialMediaLinks=socialMediaLinks,playsOn=playsOn,favoriteGames=favoriteGames)
    new_room.save()

    return render(request, 'profile.html', {'username' : username, 'socialMediaLinks' : socialMediaLinks, 'playsOn': playsOn, 'favoriteGames':favoriteGames, 'players':players})

def makeProfile(request):
    return render(request, 'makeProfile.html')

def deleteProfile(request):
    profile = Profile.objects.get(name=request.user)
    profile.delete()
    return render(request, 'index.html')

def chat(request):
    return render(request, 'chat.html')
    
def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request,'room.html', {
        'username':username,
        'room': room,
        'room_details': room_details
    })

def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('chat/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('chat/'+room+'/?username='+username)

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()

def getMessages(request, room):
    room_details = Room.objects.get(name=room)
    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})

