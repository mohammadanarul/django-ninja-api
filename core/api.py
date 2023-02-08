from ninja import NinjaAPI
from blog.api.api import router as blog_router
from reports.api.api import router as report_router
api = NinjaAPI()

api.add_router('/blog/', blog_router)
api.add_router('/reports/', report_router)