from blog.models User,Blog
from django.utils import timezone

u1 = User(username="Jaley",password="abcdef",short_desc="turning nerdy stuff funky", created_on=timezone.now())
u2 = User(username="Awantik",password="aww",short_desc="motivating everyone", created_on=timezone.now())
u3 = User(username="Ashish",password="asus",short_desc="devops for all", created_on=timezone.now())

b1 = Blog(title="In the middle of the night", body="We are the champions, we are the one . . . wWo hoho. I am really happy that things went awesome.That too happening at the stroke of midnight",status="published" ,first_published=timezone.now(),last_edited=timezone.now(),user=u1)


b2 = Blog(title="Gentle Introduction to Machine learning", body="Machine Learning is one the sexiest jobs according to LinkedIn survey. And why not? It involves learning the patterns in the text and understanding the user behavior",status="published" ,first_published=timezone.now(),last_edited=timezone.now(),user=u2)

b3 = Blog(title="DevOps for everyone", body="Today knowledge of containers in docker is not an optional skill. It is very important skill which must be imbibed by every programmer",status="published" ,first_published=timezone.now(),last_edited=timezone.now(),user=u3)

b4 = Blog(title="We are the champions", body="We are the champions, we are the one . . . wWo hoho. I am really happy that things went awesome.That too happening at the stroke of midnight",status="published" ,first_published=timezone.now(),last_edited=timezone.now(),user=u1)

b5 = Blog(title="This is awesome", body="We are the champions, we are the one . . . wWo hoho. I am really happy that things went awesome.That too happening at the stroke of midnight",status="draft" ,first_published=timezone.now(),last_edited=timezone.now(),user=u1)


