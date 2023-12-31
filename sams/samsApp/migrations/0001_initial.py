# Generated by Django 4.2.2 on 2023-06-28 16:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('is_active', models.BooleanField(default=True)),
                ('is_teacher', models.BooleanField(default=False)),
                ('is_student', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('approved', models.BooleanField(default=False, verbose_name='Approved')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Assign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='AttendanceRange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('section', models.CharField(max_length=100)),
                ('sem', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'classes',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('shortname', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('USN', models.CharField(max_length=100, primary_key='True', serialize=False)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=50)),
                ('date_of_birth', models.DateField(null=True)),
                ('batch', models.CharField(default='B1', max_length=50)),
                ('class_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='samsApp.class')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=50)),
                ('date_of_birth', models.DateField(null=True)),
                ('dept', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='samsApp.dept')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=50)),
                ('date_of_birth', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TeacherNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='samsApp.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='StudentNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='samsApp.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='samsApp.student')),
            ],
        ),
        migrations.CreateModel(
            name='NotificationTeacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='samsApp.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='NotificationStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='samsApp.student')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='dept',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='samsApp.dept'),
        ),
        migrations.AddField(
            model_name='class',
            name='dept',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='samsApp.dept'),
        ),
        migrations.CreateModel(
            name='AttendanceClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('status', models.IntegerField(default=0)),
                ('assign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='samsApp.assign')),
            ],
            options={
                'verbose_name': 'Attendance',
                'verbose_name_plural': 'Attendance',
            },
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('status', models.BooleanField()),
                ('attendanceclass', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='samsApp.attendanceclass')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='samsApp.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='samsApp.student')),
            ],
        ),
        migrations.CreateModel(
            name='AssignTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.CharField(choices=[('9:00 - 11:00', '9:00 - 11:00'), ('9:00 - 1:00', '9:00 - 1:00'), ('9:00 - 12:00', '9:00 - 12:00'), ('2:00 - 4:00', '2:00 - 4:00'), ('2:00 - 5:00', '2:00 - 5:00')], max_length=50)),
                ('day', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday')], max_length=15)),
                ('assign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='samsApp.assign')),
            ],
        ),
        migrations.AddField(
            model_name='assign',
            name='class_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='samsApp.class'),
        ),
        migrations.AddField(
            model_name='assign',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='samsApp.course'),
        ),
        migrations.AddField(
            model_name='assign',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='samsApp.teacher'),
        ),
        migrations.CreateModel(
            name='StudentCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='samsApp.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='samsApp.student')),
            ],
            options={
                'verbose_name_plural': 'Marks',
                'unique_together': {('student', 'course')},
            },
        ),
        migrations.CreateModel(
            name='AttendanceTotal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='samsApp.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='samsApp.student')),
            ],
            options={
                'unique_together': {('student', 'course')},
            },
        ),
        migrations.AlterUniqueTogether(
            name='assign',
            unique_together={('course', 'class_id', 'teacher')},
        ),
    ]
