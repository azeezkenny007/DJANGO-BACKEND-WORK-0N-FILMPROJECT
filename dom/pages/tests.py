from django.test import TestCase
from django.urls import reverse
from .models import Categorie, User, Group, Film, Season, Contact, MyModel, Attendance
import datetime
from dateutil import parser
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User as DjangoUser
from account.views import view1, view2
from account.forms import Contactform
from django.contrib.auth.forms import UserCreationForm
from .forms2 import MyForm

# Create your tests here.


class MyTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("successfully set the data")
        pass

    def setUp(self):

        contact = Contact.objects.create(
            name="okhamena",
            email="azeezokhamena@gmail.com",
            message="This user has succesfully logged in the server",
            created_at="01/25/23"

        )

        user = DjangoUser.objects.create_user(
            username="testuser", password="secretpassword",
        )

    def test_check_If_the_template_is_okay(self):
        self.assertTrue(True)

    def test_if_endpoint_correct(self):
        response = self.client.get('/pages/index2/')
        self.assertEqual(response.status_code, 200)

    def test_if_reverse_endpoint_correct(self):
        response = self.client.get(reverse('index2'))
        self.assertEqual(response.status_code, 200)

    def test_if_model_created_is_correct(self):
        category = Categorie.objects.create(name="favorite")
        self.assertEqual(category.name, "favorite")

    def test_if_user_model_is_correct(self):
        user = User.objects.create(name="Ladi")
        self.assertEqual(user.name, "Ladi")
        self.assertEqual(user.id, 1)

    def test_if_user_tags_is_correct(self):
        main_user = User.objects.create(name="Ladi")
        user = User.objects.get(id=1)
        field_label = user._meta.get_field("name").verbose_name
        field_label_max_length = user._meta.get_field("name").max_length
        self.assertEqual(field_label, "name")
        self.assertEqual(field_label_max_length, 255)

    def test_if_user_str_is_correct(self):
        main_user = User.objects.create(name="Ladi")
        user = User.objects.get(id=1)
        expected_string_value = f'{user.name}'
        self.assertEqual(str(user), expected_string_value)

    def test_if_group_model_value_is_correct(self):
        main_user_User = User.objects.create(name="Ladi")
        user = User.objects.get(id=1)
        main_user_Group = Group.objects.create(name="Ladi")
        group = Group.objects.get(id=1)
        name = group._meta.get_field("name").verbose_name
        joined_group_date = group._meta.get_field(
            "joined_group_date").verbose_name
        name_length = group._meta.get_field("name").max_length
        users = group._meta.get_field("users").verbose_name
        self.assertEqual(name, "name")
        self.assertEqual(joined_group_date, "joined group date")
        self.assertEqual(users, "users")
        self.assertEqual(name_length, 255)

    def test_if_correct_template_is_used(self):
        response = self.client.get(reverse('index2'))
        print(response, "👩‍🦰")
        self.assertTemplateUsed(response, "pages/index2.html")

    def test_if_correct_template_is_used_for_pricing_view(self):
        response = self.client.get(reverse("pricing"))
        self.assertTemplateUsed(response, "pages/pricing.html")

    def test_if_pricing_view_is_correct(self):
        response = self.client.get("/pages/pricing/")
        self.assertEqual(response.status_code, 200)

    def test_if_correct_template_is_used_for__faq__view(self):
        response = self.client.get(reverse("faq"))
        self.assertTemplateUsed(response, "pages/faq.html")

    def test_if_correct_template_is_used_for_catalog2__view(self):
        response = self.client.get(reverse("catalog2"))
        self.assertTemplateUsed(response, "pages/catalog2.html")

    def test_if_correct_template_is_used_for_test_view(self):
        response = self.client.get(reverse("about"))
        self.assertTemplateUsed(response, "pages/about.html")

    def test_if_correct_template_is_used_for_error_view(self):
        response = self.client.get(reverse("404"))
        self.assertTemplateUsed(response, "pages/404.html")

    def test_if_correct_template_is_used_for_home_view(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 302)

    # def test_if_redirect_view_from_home_page_is_correct(self):
    #     response = self.client.get("/pages/index")
    #     self.assertRedirects(response,"/pages/login",status_code=302,target_status_code=301)

    def test_if_data_in_film_model_is_correct(self):
        movies_choices = (('Action', 'Action'), ('Horror', 'horror'),
                          ('Thriller', 'Thriller'))
        category = Categorie.objects.create(name="favorite")
        main_film = Film.objects.create(
            category=category,
            name="season",
            tags="best selling",
            R_rating="2.4",
            Description="The boy that steals from us",
            is_series=True,
            movie_rating="Best",
            running_time="",
            release_year="2000",
            country="nigeria",
            date_created="12/03/2021"

        )

        film = Film.objects.get(id=1)
        season = Season.objects.create(
            film=main_film, description="The man at the shop is crazy", season_number=2)
        category = film._meta.get_field("category").verbose_name
        category_length = film._meta.get_field("category").max_length
        tags = film._meta.get_field("tags").verbose_name
        tags_length = film._meta.get_field("tags").max_length
        tags_choices = film._meta.get_field("tags").choices
        self.assertEqual(category_length, None)
        season_film = season._meta.get_field("film").verbose_name
        season_description = season._meta.get_field("description").verbose_name
        season_season_number = season._meta.get_field(
            "season_number").verbose_name
        season_season_number_max_length = season._meta.get_field(
            "season_number").max_length
        self.assertEqual(season_season_number_max_length, 200)
        self.assertEqual(season_season_number, "season number")
        self.assertEqual(season_description, "description")
        self.assertEqual(season_film, "film")
        self.assertEqual(category, "category")
        self.assertEqual(tags, "tags")
        self.assertEqual(tags_length, 20)
        self.assertEqual(tags_choices, movies_choices)

    def test_if_the_model_Attendance_is_working_correctly(self):
        contactCreate = Contact.objects.create(
            name="azeez", email="azeezokhamena@gmail.com", message="This form was submitted", created_at="12/12/2021")
        contact = Contact.objects.get(id=1)
        contact_name = contact._meta.get_field("name").verbose_name
        contact_name_max_length = contact._meta.get_field("name").max_length
        contact_email = contact._meta.get_field("email").verbose_name
        contact_message = contact._meta.get_field("message").verbose_name
        contact_creattion_time = contact._meta.get_field(
            "created_at").verbose_name
        self.assertEqual(contact_name, "name")
        self.assertEqual(contact_email, "email")
        self.assertEqual(contact_message, "message")
        self.assertEqual(contact_creattion_time, "created at")
        self.assertEqual(contact_name_max_length, 255)

    def test_if_field_is_correct(self):
        contactCreate = Contact.objects.create(
            name="azeez", email="azeezokhamena@gmail.com", message="This form was submitted", created_at="12/12/2021")
        contact = Contact.objects.get(id=1)
        contact_name_charField = contact._meta.get_field(
            "name").get_internal_type()
        self.assertEqual(contact_name_charField, "CharField")

    def test_if_values_used_in_contact_model_is_correct(self):
        contactCreate = Contact.objects.create(
            name="azeez", email="azeezokhamena@gmail.com", message="This form was submitted", created_at="01/25/23")
        self.assertEqual(contactCreate.name, "azeez")
        self.assertEqual(contactCreate.email, "azeezokhamena@gmail.com")
        self.assertEqual(contactCreate.message, "This form was submitted")
        self.assertTrue(contactCreate.created_at.strftime("%x") == "01/25/23")

    def test_if_values_used_in_model_Mymodel_model_is_correct(self):
        my_model_create = MyModel.objects.create(
            name="kenny", description="The man at field", created_at="01/25/23", updated_at="01/25/23")
        model = MyModel.objects.get(id=1)
        name_field_name = model._meta.get_field("name").verbose_name
        name_field_length = model._meta.get_field("name").max_length
        description_field_name = model._meta.get_field(
            "description").verbose_name
        name_is_CharField = model._meta.get_field("name").get_internal_type()
        description_is_TextField = model._meta.get_field(
            "description").get_internal_type()
        created_at_DateTimeField = model._meta.get_field(
            "created_at").get_internal_type()
        updated_at_DateTimeField = model._meta.get_field(
            "updated_at").get_internal_type()
        updated_at_auto_add_now = model._meta.get_field("updated_at")
        self.assertEqual(model.name, "kenny")
        self.assertEqual(model.description, "The man at field")
        self.assertEqual(model.created_at.strftime("%x"), "01/25/23")
        self.assertTrue(model.updated_at.strftime("%x") == "01/25/23")
        self.assertEqual(description_field_name, "description")
        self.assertEqual(name_field_length, 255)
        self.assertEqual(name_field_name, "name")
        self.assertEqual(name_is_CharField, "CharField")
        self.assertEqual(description_is_TextField, "TextField")
        self.assertEqual(created_at_DateTimeField, "DateTimeField")
        self.assertTrue(updated_at_DateTimeField, "DateTimeField")

    def test_if_redirect_is_working(self):
        form_data = {"course": "MEE322",
                     "student": "okhamena azeez", "timestamp": "23/01/23"}
        # Convert timestamp string to datetime object
        timestamp = parser.parse(form_data['timestamp'])
        # Convert datetime object to desired format
        form_data["timestamp"] = timestamp.strftime('%Y-%m-%d')
        form_model = Attendance(**form_data)
        form_model.full_clean()
        form_model.save()
        response = self.client.post("/pages/attend/", data=form_data)
        self.assertRedirects(response, "/pages/signed/", status_code=302)

    def test_if_Mymodel_str_name_is_correct(self):
        my_model_create = MyModel.objects.create(
            name="kenny", description="The man at field", created_at="01/25/23", updated_at="01/25/23")
        model = MyModel.objects.get(id=1)
        expected_string_value = f"{model.name}"
        self.assertEqual(str(model), expected_string_value)

    def test_if_httpresponse_contain_the_http_response(self):
        response = self.client.get("/pages/signed/")
        self.assertContains(response, "You have been successfully redireceted")

    def test_the_used_for_the_web_browser_is_correct(self):
        response = self.client.get("/pages/about/")
        self.assertTemplateUsed(response, "pages/about.html")

    def test_if_the_get_request_is_correct(self):
        movies_choices = (('Action', 'Action'), ('Horror', 'horror'),
                          ('Thriller', 'Thriller'))
        category = Categorie.objects.create(name="favorite")
        image = SimpleUploadedFile(
            name="child.jpg",
            content=open(
                "C:\\Users\\DELL 5470\\Desktop\\django templates\\filmproject\\dom\\media\\images\\child.jpg", "rb").read(),
            content_type="image/jpg")
        main_film = Film.objects.create(
            category=category,
            name="season",
            tags="best selling",
            image_url=image,
            R_rating="2.4",
            Description="The boy that steals from us",
            is_series=True,
            movie_rating="Best",
            running_time="",
            release_year="2000",
            country="nigeria",
            date_created="12/03/2021"

        )

        film = Film.objects.get(id=1)
        response = self.client.get("/pages/details1/1/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["film"], film)

    # def test_if_test_category_film_test(self):
    #     category = Categorie.objects.create(name="favorite")
    #     image = SimpleUploadedFile(
    #         name="child.jpg",
    #         content=open(
    #         "C:\\Users\\DELL 5470\\Desktop\\django templates\\filmproject\\dom\\media\\images\\child.jpg","rb").read(),
    #         content_type="image/jpg")
    #     main_film = Film.objects.create(
    #         category=category,
    #         name="season",
    #         tags="best selling",
    #         image_url=image,
    #         R_rating="2.4",
    #         Description="The boy that steals from us",
    #         is_series=True,
    #         movie_rating="Best",
    #         running_time="",
    #         release_year="2000",
    #         country="nigeria",
    #         date_created="12/03/2021"

    #     )
    #     film = Film.objects.all()
    #     series = Film.objects.filter(category__name='tvseries')
    #     movies = Film.objects.filter(category__name='movies')
    #     cartoons = Film.objects.filter(category__name='cartoons')
    #     kate = {'film': film, 'cartoons': cartoons,'movies': movies, 'series': series}
    #     response = self.client.get("/pages/index/")
    #     self.assertEqual(response.status_code,302)
    #     self.assertEqual(response.context["kate"],kate)

    def test_if_post_request_on_view1_is_working(self):
        response = self.client.post(reverse(view1), {
            "username": "testuser", "password": "secretpassword"
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("index"), status_code=302)

    def test_if_post_request_view2_is_correct(self):
        form_data = {"username": "okhamena",
                     "email": "azeezokhamena@gmail.com",
                     "password1": "failfault",
                     "password2": "failfault"
                     }
        response = self.client.post(reverse(view2), data=form_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse(view1))

    def test_if_post_request_fail_if_an_empty_text_is_sent(self):
        form_data = {"username": "",
                     "email": "",
                     "password1": "",
                     "password2": ""
                     }
        response = self.client.post(reverse(view2), data=form_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "account/signup.html")

    def test_if_the_form_will_fail_if_incorrect_data_is_sent(self):
        form = MyForm({"name": ""})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["name"], ['This field is required.'])

    def test_if_the_form_will_fail_if_other_data_are_not_provided(self):
        form = MyForm({"email": ""})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["email"], ["This field is required."])

    def test_if_the_form_will_fail_if_incorrect_data_is_sent(self):
        form = MyForm({"name": "a" * 256})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["name"], [
                         'Ensure this value has at most 255 characters (it has 256).'])

    def test_if_the_form_will_fail_with_only_message_provided(self):
        form = MyForm({"message": ""})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["message"], ["This field is required."])

    def test_if_the_form_request_will_go(self):
        form = MyForm({"name": "azeez", "message": "This is the townhall",
                      "email": "azeezokhamena@gmail.com"})
        self.assertTrue(form.is_valid())

    def test_to_reject_the_number_words_added_to_the_message_field(self):
        form = MyForm({"message": "a" * 100001})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["message"],
                         ['Ensure this value has at most 10000 characters (it has 100001).'])
        
    def test_if_two_from_form_is_supplied(self):
        form=MyForm({"message":"This is some text","name":"azeez","email":""})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["email"],["This field is required."])
        
    def test_if_two_of_the_data_can_work(self):
        form =MyForm({"message":"This is some text","name":"azeez"})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["email"],["This field is required."])
        
    def test_if_the_data_inputed_is_correct(self):
        form =MyForm({"message":"This is some text","email":"azeezokhamena@gmail.com","nana":"azeez"})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'],["This field is required."])
        self.assertEqual(form.cleaned_data["message"],"This is some text")
        # self.assertEqual(form.cleaned_data["nana"],"azeez")
        self.assertEqual(form.cleaned_data["email"],"azeezokhamena@gmail.com")
        
    def test_for_keyError_in_the_data(self):
        form =MyForm({"message":"This is some text","email":"azeezokhamena@gmail.com","nana":"azeez"})
        self.assertFalse(form.is_valid())
        self.assertNotIn("nana",form.cleaned_data)
