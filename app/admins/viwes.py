from starlette_admin.contrib.sqla import ModelView

class UserAdminViwe(ModelView):
    fields=[
        "id",
        "email",
        "password_hash",
        "first_name",
        "last_name",
        "profession_id",
        "bio",
        "post_count",
        "post_read_count",
        "is_active",
        "is_staff",
        "is_superuser",
        "is_deleted",
        "deleted_email",
        "created_at",
        "updated_at",
        
        
    ]
    exclude_fields_from_list=[
        "password_hash",
        "bio",
        "post_count",
        "posts_read_count",
        "is_deleted",
        "deleted_email"
    ]
    exclude_fields_from_create=[
        "id",
        "created_at",
        "updated_at",
        "post_count",
        "post_read_count"
    ]
    