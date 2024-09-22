from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name="Blog Title", help_text="Enter the title of the blog")
    slug = models.CharField(max_length=100, verbose_name="Blog Slug", null=True, blank=True)
    content = models.TextField(blank=True, null=True, verbose_name="Blog Content", help_text="Enter the content of the blog")
    preview = models.ImageField(upload_to="blogs/photo", blank=True, null=True, verbose_name="Blog Preview", help_text="Upload the preview of the blog")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date of Creation", help_text="Enter the date of creation of the blog")
    is_published = models.BooleanField(default=True, verbose_name="Is Published", help_text="Enter the is published of the blog")
    views = models.IntegerField(default=0, verbose_name="Blog Views")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"
        ordering = ["title"]


