from django.db import migrations


def create_categories(apps, schema_monitor):
    Category = apps.get_model("api", "Category")

    Category.objects.create(name="Novo Produto")
    Category.objects.create(name="Troca de Fornecedor")
    Category.objects.create(name="Reformulação de Produto")


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_categories),
    ]
