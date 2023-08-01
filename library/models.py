from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    username = models.CharField(max_length=200, null=True, unique=True)
    email = models.EmailField(unique=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    friends = models.ManyToManyField("User", blank=True)
    image = models.ImageField(null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    @property 
    def readBooks(self):
        userbooks = self.userbook_set.all()
        count = 0
        for book in userbooks:
            if book.book_status == "Read":
                count += 1
        return count
    
    @property 
    def wtrBooks(self):
        userbooks = self.userbook_set.all()
        count = 0
        for book in userbooks:
            if book.book_status == "Want to Read":
                count += 1
        return count

    @property 
    def crBooks(self):
        userbooks = self.userbook_set.all()
        count = 0
        for book in userbooks:
            if book.book_status == "Currently Reading":
                count += 1
        return count

class FriendRequest(models.Model):
    from_user = models.ForeignKey(User, related_name="from_user", on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name="to_user", on_delete=models.CASCADE)


class Genre(models.Model):
    name = models.CharField(max_length=100, null=True)
    # books = models.ManyToManyField(Book, related_name="books")

    @property
    def listGenres(self):
        genres = Genre.objects.all()
        return genres 

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200, null=True) 
    description = models.TextField()

    @property 
    def getBookCount(self):
        authorBooks = self.book_set.all()
        count = 0
        for i in authorBooks:
            count += 1
        return count
    
    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=200, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    description = models.TextField()
    genres = models.ManyToManyField(Genre, related_name="books")
    image = models.ImageField(null=True, blank=True)
    date_added = models.DateTimeField(null=True, auto_now=True)
    users = models.ManyToManyField(User, blank=True, related_name="books")
    
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    def __str__(self):
        return self.name

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, blank=True, null=True)
    body = models.TextField(null=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    
    # def __str__(self):
    #     return self.book


class userBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date_added = models.DateTimeField(auto_now=True)
    # BOOK_STATUS = [
    #     ("R", "Read"),
    #     ("WR", "Want to Read"),
    #     ("CR", "Currently Reading")
    # ]
    book_status = models.CharField(max_length=100, null=True)
    RATING_RANGE = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    ]
    rating = models.IntegerField(choices=RATING_RANGE, null=True, blank=True)

    @property
    def avgRating(self):
        total = 0
        ratings = self.rating.all()
        for rating in ratings:
            total += rating
        return total//len(ratings)
    
    
    def __str__(self):
        return self.book.name

class bookShelf(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Group(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=500, null=True)
    participants = models.ManyToManyField(
        User, related_name="participants", blank=True)
    image = models.ImageField(null=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated', '-created']
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    def __str__(self):
        return self.name

class NewsArticle(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    headline = models.CharField(max_length=500, null=True)
    running_head = models.TextField(null=True, blank=True)
    published = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField(null=True)
    image = models.ImageField(null=True)

    class Meta:
        ordering = ['-updated', '-created']

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    
    @property
    def excerpt(self):
        return self.body[0:500]
    
    @property 
    def blurb(self):
        return self.body[0:100]
    
    def __str__(self):
        return self.headline[0:50]

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    body = models.TextField()
    article = models.ForeignKey(NewsArticle, on_delete=models.CASCADE, null=True, blank=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.body[0:50]



