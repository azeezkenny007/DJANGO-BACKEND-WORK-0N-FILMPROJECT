from django.test import TestCase
from django.urls import reverse
from .models import Categorie, User, Group, Film, Season,Contact

# Create your tests here.


class MyTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("successfully set the data")
        pass

    def setUp(self):
        print("set to run everytime")
        pass

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
        season_season_number = season._meta.get_field("season_number").verbose_name
        season_season_number_max_length = season._meta.get_field("season_number").max_length
        self.assertEqual(season_season_number_max_length,200)
        self.assertEqual(season_season_number,"season number")
        self.assertEqual(season_description,"description")
        self.assertEqual(season_film,"film")
        self.assertEqual(category, "category")
        self.assertEqual(tags, "tags")
        self.assertEqual(tags_length, 20)
        self.assertEqual(tags_choices, movies_choices)

    def test_if_the_model_Attendance_is_working_correctly(self):
        contactCreate = Contact.objects.create(name="azeez",email="azeezokhamena@gmail.com",message="This form was submitted",created_at="12/12/2021")
        contact = Contact.objects.get(id=1)
        contact_name = contact._meta.get_field("name").verbose_name
        contact_name_max_length = contact._meta.get_field("name").max_length
        contact_email =contact._meta.get_field("email").verbose_name
        contact_message = contact._meta.get_field("message").verbose_name
        contact_creattion_time = contact._meta.get_field("created_at").verbose_name
        self.assertEqual(contact_name,"name")
        self.assertEqual(contact_email,"email")
        self.assertEqual(contact_message,"message")
        self.assertEqual(contact_creattion_time,"created at")
        self.assertEqual(contact_name_max_length,255)
        
    
    def test_if_field_is_correct(self):
         contactCreate = Contact.objects.create(name="azeez",email="azeezokhamena@gmail.com",message="This form was submitted",created_at="12/12/2021")
         contact = Contact.objects.get(id=1)
         contact_name_charField = contact._meta.get_field("name").get_internal_type()
         self.assertEqual(contact_name_charField,"CharField")
         
    if isinstance()
