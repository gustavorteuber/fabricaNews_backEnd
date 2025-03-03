# Generated by Django 4.2.1 on 2023-06-20 23:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0016_remove_news_category_remove_news_project_and_more"),
        ("project", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comments",
            name="news",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="comments",
                to="project.news",
            ),
        ),
        migrations.AlterField(
            model_name="favorites",
            name="news",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="project.news"
            ),
        ),
        migrations.AlterField(
            model_name="newsfeel",
            name="news",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="news_feels",
                to="project.news",
            ),
        ),
        migrations.AlterField(
            model_name="savetoread",
            name="news",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="SaveToReads",
                to="project.news",
            ),
        ),
        migrations.DeleteModel(
            name="News",
        ),
    ]
