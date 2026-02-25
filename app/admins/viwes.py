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
    

    
    
class PostAdminView(ModelView):
    fields = [
        "id",
        "title",
        "slug",
        "body",
        "user_id",
        "category_id",
        "views_count",
        "likes_count",
        "comments_count",
        "mins_read",
        "created_at",
        "updated_at",
    ]

    exclude_fields_from_list = [
        "body",
    ]

    exclude_fields_from_create = [
        "id",
        "views_count",
        "likes_count",
        "comments_count",
        "created_at",
        "updated_at",
    ]

    exclude_fields_from_edit = [
        "id",
        "views_count",
        "likes_count",
        "comments_count",
        "created_at",
        "updated_at",
    ]

    exclude_fields_from_detail = []
    
    
class CommentAdminView(ModelView):
    fields = [
        "id",
        "user_id",
        "post_id",
    ]
    
    
class ProfessionAdminView(ModelView):
    fields = [
        "id",
        "name",
    ]

    exclude_fields_from_create = ["id"]
    exclude_fields_from_edit = ["id"]
    
    
class TagAdminView(ModelView):
    fields = [
        "id",
        "name",
        "slug",
    ]

    exclude_fields_from_create = ["id"]
    exclude_fields_from_edit = ["id"]
