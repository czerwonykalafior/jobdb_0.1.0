import os
import random
import json
#TODO: parse json and create Stanowisko()


def populate():
    c_sum = 0
    with open('lista_branz') as f:
        for line in f:

            p, created = Stanowisko.objects.get_or_create(pl_job='')
            if created:
                print "Dodano: %r" % line
                c_sum += 1
    print 'Zrobione! Dodano %i stanowisk.' %c_sum
    return None

# Start execution here!
if __name__ == '__main__':
    print "Starting population script..."
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jobdb.settings")
    import django
    django.setup()
    from addjob.models import Stanowisko
populate()