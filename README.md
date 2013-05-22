---------------------------------------
django-phpbb - Django-PhpBB integration
---------------------------------------

In case of django-phpbb, using it means that when you're coding a Django
application, you have a set of classes and functions at your disposal, providing
a glue between phpBB3 and Django.

## Authentication ##

### A prerequisite: Django authentication ###

First, prerequisites. Make sure your [Django
authentication](http://docs.djangoproject.com/en/dev/topics/auth/#topics-auth)
is working. 

If your Django website uses authentication already, you probably have the
following lines in your `urls.py`.

    (r'^accounts/login/$', 'django.contrib.auth.views.login', ),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout', ),

If there are no such lines in your `urls.py`, your application probably doesn't
use authentication. Consult the Django documentation for instructions to get
your authentication to work.

## PYTHONPATH ##

The django-phpbb directory must be in PYTHONPATH (or sys.path).

## Adding phpbb3 authentication backend ##

Edit your `settings.py` and make sure the following lines are present:

    MIDDLEWARE_CLASSES = (
        ...
        'django.contrib.auth.middleware.AuthenticationMiddleware',
    )
    TEMPLATE_CONTEXT_PROCESSORS = (
        ...
        "django.core.context_processors.auth",
    )
    INSTALLED_APPS = (
        'django.contrib.auth',
        ...
        'phpbb',
    )
    AUTHENTICATION_BACKENDS = (
        'phpbb.backends.PhpbbBackend',
        'django.contrib.auth.backends.ModelBackend',
    )


Once you've done that, the authentication backend should be enabled and users
should be able to log in using not only Django passwords, but also passwords
checked against the phpbb3 database.

## phpBB3 classes ##

You can access phpBB3 forum objects using provided classes. Look up the source
code to see the details of the classes. (Sorry for not providing any better
documentation at this time.)

Fire up Django shell and try using django-phpbb classes:

    ./manage.py shell
    from django.contrib.phpbb import models as p3m
    forum = p3m.PhpbbForum.objects.get(pk=1)
    dir(forum)
    forum.forum_name
    forum.phpbbtopic_set.all()[:5]

## Predefined views ##

You need to have a `base.html` template that django-phpbb's template expect to
extend.

To enable predefined views, add this line to your `urls.py`:

    (r'^forum/', include('phpbb.urls')),

Also, make django-phpbb templates available:

    TEMPLATE_DIRS = (
        ...
        "/some-directory/django-phpbb/phpbb/templates",
    )

_The views currently contain bits and pieces of the original website they've
been cut from. The views are going to be reworked. Consider them more as a guide
to see how you can implement your own forum browsing rather than a complete
solution._

License
-------

Copyright (C) 2008 Maciej Bliziński <maciej.blizinski@gmail.com>  
Copyright (C) 2010 Olivier Le Thanh Duong <olivier@lethanh.be>

django-phpbb is free software; you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation; either version 2 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
this program; if not, write to the Free Software Foundation, Inc., 59 Temple
Place, Suite 330, Boston, MA 02111-1307 USA
