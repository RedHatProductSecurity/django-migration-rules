from django.db import migrations, models

# Wrong, cannot be removed both for database and state in a single version
class Migration(migrations.Migration):
    operations = [
        # ruleid: django-migration-remove-field
        migrations.RemoveField(
            bar='baz',
            model_name='foo',
            name='bar',
            foo='bar',
        ),
    ]

# Correct, deleted at the state-level only
class Migration(migrations.Migration):
    operations = [
        migrations.SeparateDatabaseAndState(
            # ok: django-migration-remove-field
            state_operations=[
                migrations.RemoveField(
                    bar='baz',
                    model_name='foo',
                    name='bar',
                    foo='bar',
                ),
            ],
        ),
    ]

