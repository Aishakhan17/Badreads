from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import Q
from .models import *
from .forms import MyUserCreationForm, GroupForm, PictureForm
from random import sample
from django.http import JsonResponse, HttpResponse
import json

# Create your views here.

def loginUser(request):
    page = "login"
    if request.user.is_authenticated:
        return redirect('feed')
    
    if request.method == "POST":
        email = request.POST.get("email").lower()
        password = request.POST.get("password")

        try: 
            user = User.objects.get(email=email)
        except:
            messages.error(request, "User does not exist")
            return redirect('register')
        
        user = authenticate(request, email=email, password=password)
        
        if user is not None: 
            login(request, user)
            print("login successfull")
            messages.error(request, "login successfull")
            return redirect('feed')
        else: 
            print("login unsuccessfull")
            messages.error(request, "Username OR Password is incorrect")

    books = Book.objects.all()
    counter = 5
    carouselBooks = sample(list(books), counter)
    context = {"books": books, "carouselBooks": carouselBooks, "page": page}
    return render(request, "library/login.html", context)

def registerUser(request):
    if request.user.is_authenticated:
        return redirect('feed')
    else:
        form = MyUserCreationForm()

        if request.method == "POST":
            form = MyUserCreationForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.name = user.name
                user.email = user.email.lower()
                user.save()
                login(request, user)
                print("User created successfully")
                return redirect('feed')
            else:
                print("unsuccessful registration")
                messages.error(request, "An error occured during registration, please try again")
    
    context = {"form": form}
    return render(request, "library/register.html", context)

@login_required
def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required
def feed(request):
    user = request.user
    friends = user.friends.all()
    userbooks = userBook.objects.filter(user=user)
    f_userbooks = userBook.objects.all()
    newsarticles = NewsArticle.objects.all()
    # books = Book.objects.all()
    genres = Genre.objects.all()
    context = {"userbooks": userbooks, "genres": genres, "newsarticles": newsarticles, "friends": friends, "f_userbooks": f_userbooks}
    return render(request, "library/feed.html", context)

@login_required
def book(request, pk):
    book = Book.objects.get(id=pk)
    bookshelves = bookShelf.objects.all()
    genres =Genre.objects.all()
    review = Review.objects.all()
    reviews = book.review_set.all()
    rating = userBook.avgRating 
    context = {"book": book, "bookshelves": bookshelves, "genres": genres, "rating": rating, "reviews": reviews, "review": review}
    return render(request, "library/book.html", context)

@login_required
def trending(request):
    books = Book.objects.all()
    bookshelves = bookShelf.objects.all()
    genres = Genre.objects.all()
    context = {"genres": genres, "books": books,"bookshelves": bookshelves}
    return render(request, "library/trending.html", context)

@login_required
def groups(request):
    genres = Genre.objects.all()
    groups = Group.objects.all()
    context = {"genres": genres, "groups": groups}
    return render(request, "library/community.html", context)


def group(request, pk):
    genres = Genre.objects.all()
    group = Group.objects.get(id=pk)
    participants = group.participants.all()
    messages = group.message_set.all()
    context = {"group": group, "messages": messages, "genres": genres, "participants": participants}
    return render(request, "library/group.html", context)

@login_required
def addToShelf(request):
    data = json.loads(request.body)
    bookID = data["bookID"]
    action = data["action"] 
    print("Item was added")
    # print("bookID", bookID, "action", action)
    # print(data)

    user = request.user
    book = Book.objects.get(id=bookID)
    user_book, created = userBook.objects.get_or_create(user=user, book=book)

    if action == "Read":
        user_book.book_status = "Read"
    elif action == "Want to Read":
        user_book.book_status = "Want to Read"
    elif action == "Currently Reading":
        user_book.book_status = "Currently Reading"
    
    user_book.save()
    return JsonResponse('Item was added', safe=False) 

@login_required 
def myBooks(request):
    user = request.user
    userbooks = userBook.objects.filter(user=user)
    genres = Genre.objects.all()
    context = {"genres": genres, "user": user, "userbooks": userbooks}
    return render(request, "library/myBooks.html", context)

def addReview(request):
    data = json.loads(request.body)
    bookID = data["bookID"]
    review = data["review"] 

    user = request.user
    book = Book.objects.get(id=bookID)
    body = review
    review = Review.objects.create(user=user, book=book, body=body)
    review.save()
    return JsonResponse('Review was added', safe=False)

def addMessage(request):
    data = json.loads(request.body)
    user = request.user
    group = Group.objects.get(id=data["groupID"])
    body = data["msg"]
    newMsg = Message.objects.create(user=user, group=group, body=body)
    group.participants.add(user)
    newMsg.save()
    return JsonResponse('Review was added', safe=False)

def deleteMessage(request, pk):
    message = Message.objects.get(id=pk) 
    if request.user == message.user:
        message.delete()
        return redirect('group')
    return JsonResponse('Message Deleted', safe=False)
    
def userProfile(request, pk):
    user = User.objects.get(id=pk)
    genres = Genre.objects.all()
    bookshelves = bookShelf.objects.all()
    friends = user.friends.all()
    userbooks = userBook.objects.filter(user=user)
    newsarticles = NewsArticle.objects.filter(author=user)
    groups = user.group_set.all()
    # form = PictureForm()
    # if request.method == "POST": 
    #     form = PictureForm(request.FILES)
    #     if form.is_valid():
    #         user = request.user
    #         form = form.save(commit=False)
    #         user.image = form.image
    #         form.save()
    #         return redirect('')
    context = {"genres": genres, "user": user, "friends": friends, "userbooks": userbooks, "bookshelves": bookshelves, "newsarticles": newsarticles, "groups": groups}
    return render(request, "library/profile.html", context)

def newsarticles(request):
    genres = Genre.objects.all()
    newsarticles = NewsArticle.objects.all()
    context = {"genres": genres, "newsarticles": newsarticles}
    return render(request, "library/newsarticles.html", context)

def newsarticle(request, pk):
    newsarticle = NewsArticle.objects.get(id=pk)
    genres = Genre.objects.all()
    comments = newsarticle.message_set.all()
    context = {"newsarticle": newsarticle, "genres": genres, "comments": comments}
    return render(request, "library/newsarticle.html", context)

def newsArticleForm(request):
    context = {}
    return render(request, "library/newsArticleForm.html", context)

def createArticle(request):     
    if request.method == "POST":
        image = request.FILES.get("image")
        headline = request.POST.get("headline")
        running_head = request.POST.get("running_head")
        body = request.POST.get("body")
        user = request.user.id
        author = User.objects.get(id=user)
        article = NewsArticle.objects.create(author=author, headline=headline, running_head=running_head, body=body, image=image)
        article.save()
    return JsonResponse('Article was added', safe=False)

def createGroup(request):
    form = GroupForm()

    if request.method == "POST":
        form = GroupForm(request.POST, request.FILES)
        if form.is_valid():
            group = form.save(commit=False)
            user = request.user.id
            group.host = User.objects.get(id=user)
            group.name = group.name
            group.description = group.description
            group.image = group.image
            group.save()
            print("Group created successfully")
            return redirect('community')
        else:
            print("unsuccessful registration")
            messages.error(request, "An error occured during group creation, please try again")
    context = {"form": form}
    return render(request, "library/createGroup.html", context)

@login_required
def sendFriendRequest(request, pk):
    from_user = request.user
    to_user = User.objects.get(id=pk)
    friend_request, created = FriendRequest.objects.get_or_create(from_user=from_user, to_user=to_user)
    if created:  
        return HttpResponse("Friend Request Sent")
    else:
        return HttpResponse("Friend request already sent, waiting user response")
    
@login_required
def acceptFriendRequest(request):
    data = json.loads(request.body)
    requestID = data["requestID"]
    action = data["action"]
    friend_request = FriendRequest.objects.get(id=requestID)
    if friend_request.to_user == request.user:
        if action == "Accept":
            friend_request.to_user.friends.add(friend_request.from_user)
            friend_request.from_user.friends.add(friend_request.to_user)
            friend_request.delete()
            # return redirect('notifications')
            id = request.user.id
            return redirect('notifications')
        elif action == "Reject":
            friend_request.delete()
            return HttpResponse("Friend Request Rejected")
        else:
            return HttpResponse("There was an error")
    

@login_required
def notifications(request):
    user = request.user.id
    to_user = User.objects.get(id=user)            
    friend_requests = FriendRequest.objects.filter(to_user=to_user)
    context = {"friend_requests": friend_requests}
    return render(request, "library/notifications.html", context)

def search(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    books = Book.objects.filter(
        Q(name__icontains=q) |
        Q(description__icontains=q) |
        Q(author__name__icontains=q)
    )
    users = User.objects.filter(
        Q(name__icontains=q)
    )
    groups = Group.objects.filter(
        Q(name__icontains=q) |
        Q(host__name__icontains=q) |
        Q(description__icontains=q)
    )
    newsarticles = NewsArticle.objects.filter(
        Q(headline__icontains=q) |
        Q(running_head__icontains=q) |
        Q(author__name__icontains=q)
    )
    context = {"books": books, "users": users, "groups": groups, "newsarticles": newsarticles}
    return render(request, "library/searchResult.html", context)

def filterGenre(request, pk):
    genres = Genre.objects.all()
    genre = Genre.objects.get(id=pk)
    books = Book.objects.filter(genres=genre)
    context = {"genre": genre, "books": books, "genres": genres}
    return render(request, "library/trending.html", context)