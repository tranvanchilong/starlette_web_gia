from starlette.routing import Mount, Route
import views, views_iframe
from starlette.staticfiles import StaticFiles
routes=[
        Mount('/static', StaticFiles(directory='static'), name='static'),
        Route('/', endpoint=views.home_page, methods=["GET", "POST"]),
        # Route('/iframe/home', endpoint=views_iframe.home_page, methods=["GET", "POST"]),
        Route('/time', endpoint=views.time_page, methods=["GET", "POST"]),
        Route("/blog", endpoint=views.blog),
        Route("/tygia", endpoint=views.tygia),
        Route("/{path}/{name}", endpoint=views.language_page, methods=["GET", "POST"]),
        # Route("/{language}/{father}/{page:int}", endpoint=views.language_lib_page),
        # Route('/html/{language}/{father}/{id}', endpoint=views.single_page)
        # Route("/iframe/{path}/{name}", endpoint=views_iframe.language_page, methods=["GET", "POST"]),
    ]
