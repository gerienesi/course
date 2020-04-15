# Course APP

#### Run migrations
```
python manage.py migrate
```


#### Synchronize students with items from `fixture/students.json`:
```
python manage.py sync-students
```

#### Synchronize courses with items from `fixture/courses.json`:
```
python manage.py sync-courses
```

#### Start Django server:
``` 
python manage.py runserver
```

#### Courses API endpoint
```
List or create courses:
    http://127.0.0.1:8000/api/course/

Update or delete course:
    http://127.0.0.1:8000/api/course/{pk}/
```

#### Students API endpoint
```
List or create students:
    http://127.0.0.1:8000/api/student/

Update or delete student:
    http://127.0.0.1:8000/api/student/{pk}/
```