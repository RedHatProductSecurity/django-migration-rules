from django.db import migrations, models


# This is essentially a no-op at the database-level
class Migration(migrations.Migration):

    # ok: django-migration-rename-field
    operations = [
        migrations.RenameField(
            model_name='foo',
            old_name='bar',
            new_name='baz',
        ),
        migrations.AlterField(
            model_name='foo',
            name='baz',
            field=models.TextField(blank=True, db_column='bar'),
        ),
    ]


class Migration(migrations.Migration):

    # ruleid: django-migration-rename-field
    operations = [
        migrations.RenameField(
            model_name='foo',
            old_name='bar',
            new_name='baz',
        ),
    ]


# The model, old and new column names in the AlterField operation must match the
# same attributes in the RenameField operation
class Migration(migrations.Migration):

    # ruleid: django-migration-rename-field
    operations = [
        migrations.RenameField(
            model_name='foo',
            old_name='bar',
            new_name='baz',
        ),
        migrations.AlterField(
            model_name='baz',
            name='bar',
            field=models.TextField(blank=True, db_column='foo'),
        ),
    ]


# This is an even better solution as Django outputs 0 SQL statements.
class Migration(migrations.Migration):

    # ok: django-migration-rename-field
    migrations.SeparateDatabaseAndState(
        state_operations = [
            migrations.RenameField(
                model_name='foo',
                old_name='bar',
                new_name='baz',
            ),
            migrations.AlterField(
                model_name='baz',
                name='bar',
                field=models.TextField(blank=True, db_column='foo'),
            ),
        ],
    )
