import os

def populate():
    c_sum = 0
    with open('lista_branz') as f:
        for line in f:
            p, created = Branza.objects.get_or_create(name=line)
            if created:
                print "Dodano: %r" % line
                c_sum += 1
    print 'Zrobione! Dodano %i branz.' %c_sum
    return None

# Start execution here!
if __name__ == '__main__':
    print "Starting population script..."
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jobdb.settings")
    import django
    django.setup()
    from addjob.models import Branza
    populate()