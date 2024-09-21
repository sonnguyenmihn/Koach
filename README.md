## Running the application

1. clone the repository
```bash
git clone https://github.com/sonnguyenmihn/Koach.git
cd Koach
```

2. install the required Python packages
```bash 
pip install django djangorestframework requests
```

3. Run migrations
```bash
python translation_tool/manage.py migrate
```

4. Run the development server on 0.0.0.0:8000
```bash
python translation_tool/manage.py runserver 0.0.0.0:8000
```

5. Testing the application
```bash
python test.py
```



