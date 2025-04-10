from django.contrib.auth.models import User


# This class is meant to override Django’s default login behavior, which usually uses the username field.
# This method replaces the default behavior of matching by username — now users can log in using email + password.
class EmailAuthBackend:

    # This method is called by Django’s authentication system when someone logs in.
    def authenticate(self, username=None, password=None):
        try:
            user = User.objects.get(email=username)     # It treats the username field as an email address. Tries to fetch a user with that email from the database
            # Verifies the password using Django's built-in hashing/checking system
            if user.check_password(password):
                return user
            return None         # If no user is found with that email, it returns None (authentication fails).
        except User.DoesNotExist:
            return None

    # This method is required by Django to retrieve a user object based on their user ID, for session management.
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
        
        """_summary_
        authenticate()	Authenticates user using email and password
        get_user()	Retrieves user by ID for session handling
        
        While the method names must be fixed, the class name can be anything you want (e.g., EmailAuthBackend, MyAuth, etc.).
        These method names are part of Django’s authentication backend interface. Django internally calls these methods by name, so if you change their names (e.g., to my_authenticate() or fetch_user()), Django won’t recognize or use them, and authentication will fail silently or throw an error.
        
        How to Use It
        To use this backend, you must add it to your settings.py:
        AUTHENTICATION_BACKENDS = [
            'accounts.authenticate.EmailAuthBackend',
            'django.contrib.auth.backends.ModelBackend',  # keep default as fallback
            ]
        
        """