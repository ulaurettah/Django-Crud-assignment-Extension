from django contrib.admin import get_user_model().objects.create_user
from django.test import TestCase
from django.urls  import reverse

from.models import Post


# Create your tests here.
class BlogTests(Testcae):
   def setup(self):
       self.user = get_user_model().objects.create_user (
          username='testuser',
          email='test@gmail.com',
          password= 'secret'
        )


       self.post=Post.objects.create(
           title ='A good title',
            body ='Nice body'
            author = self.user
        )

   def test_string-representation(self):
       post = Post(title ='A simple title')
       self.assertEqual(str(post), post.title)

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'A good tittle')
        self.assertEqual(f'{self.post.author}', 'testuser')
        self.assertEqual(f'{self.post.body}', 'Nice body')

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContain(response, 'Nice body')
        self.assertTemplateUsed(response,'home.html')

    def test_post_detail_views(self):
        response =self.client.get('/post/1/')
        no_response =self.client.get('/post/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status-code, 404)
        self.assertContain(response, 'A good title')
        self.assertTemplateUsed(response,'post_detail.html')


    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200) 
        self.assertTemplateUsed(response,'post_about.html')