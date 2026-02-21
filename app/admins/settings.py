from starlette_admin.contrib.sqla import  Admin

from app.database import engine
from app.models import User
from .viwes import UserAdminViwe

admin=Admin(engine=engine,title="Admin panel",base_url="/admin")

admin.add_view(UserAdminViwe(User,icon="fa fa-user"))