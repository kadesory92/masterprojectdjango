import os
import django
import random
from faker import Faker

from core.models import CustomUser, Student, Teacher, Parent

django.setup()

fake = Faker()


def populate_data(num_entries=10):
    for _ in range(num_entries):
        # Create a custom user
        user = CustomUser.objects.create(
            username=fake.user_name(),
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email(),
            gender=random.choice(['M', 'F']),
            role=random.choice(['admin', 'teacher', 'student', 'parent']),
            address=fake.address(),
            phone_number=fake.phone_number()
        )

        # Create a student associated with the user
        if user.role == 'student':
            Student.objects.create(
                user=user,
                date_of_birth=fake.date_of_birth(),
                photo='student_photos/default.png'
                # Specify the default image path or use faker to generate images
            )

        # Create a teacher associated with the user
        elif user.role == 'teacher':
            Teacher.objects.create(
                user=user,
                date_of_birth=fake.date_of_birth(),
                photo='teacher_photos/default.png'
            )

        # Create a parent associated with the user
        elif user.role == 'parent':
            Parent.objects.create(
                user=user,
                date_of_birth=fake.date_of_birth(),
                photo='parent_photos/default.png'
            )


if __name__ == "__main__":
    populate_data()
