from django.contrib.auth import get_user_model

import factory

User = get_user_model()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    password = factory.PostGenerationMethodCall('set_password', 'pi3.1415')
