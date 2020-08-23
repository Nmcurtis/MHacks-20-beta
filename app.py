import json
from aiohttp import web
from google.cloud import storage


class ClassroomsApp:
    def __init__(self, client):  # classroom list - list of classroom objects
        self.client = client

    async def fail_route(self, _):
        raise Exception("Raised test exception")

    async def get_classroom_names(self, _):
        classrooms = self.client.list_buckets()
        classroom_names = [classroom.name for classroom in classrooms]
        json.dumps(classroom_names)
        return web.json_response(data=classroom_names)

    async def get_classroom_video_names(self, req):
        print(req)
        bucket_name = req.match_info.get('classroom_name')
        print(bucket_name)
        classrooms = self.client.list_buckets()
        classroom_names = [classroom.name for classroom in classrooms]
        if bucket_name in classroom_names:
            classroom_bucket = self.client.get_bucket(bucket_name)
            blobs = classroom_bucket.list_blobs()
            classroom_videos = [blob.name for blob in blobs]
            return web.json_response(data=classroom_videos)
        else:
            print("Not a legit classroom bucket")

    async def get_a_classroom_video_url(self, req):
        bucket_name = req.match_info.get('classroom_name')
        video_number = req.match_info.get('video_number')
        classrooms = self.client.list_buckets()
        classroom_names = [classroom.name for classroom in classrooms]
        if bucket_name in classroom_names:
            classroom_bucket = self.client.get_bucket(bucket_name)
            blobs = classroom_bucket.list_blobs()
            classroom_video_links = [blob.name for blob in blobs]
            requested_video = classroom_video_links[int(video_number)]
            return web.Response(text=requested_video)
        else:
            print("Not a legit classroom bucket")

    async def search_video(self, req): # send search term to function?
        class_name = req.match_info.get('classroom_name')
        lec_num = req.match_info.get('video_number')
        #search_string = req.match_info.get('search_term')
        #timestamp = theProcessingFunction(classroom_name, video_number, search_string)

        f = open("classroom_video_urls.txt", "r")
        content = f.read()
        content = json.loads(content)
        url = content["Poliical Science 227"]['Lecture 1']
        return web.Response(text=url)

    async def root_index(self, _):
        return web.FileResponse("angular/src/index.html")


async def on_prepare(_, response):
    response.headers['cache-control'] = 'no-cache'


def create_app():
    app = web.Application()
    app.on_response_prepare.append(on_prepare)
    app.classroom_service = ClassroomsApp(
        client=storage.Client.from_service_account_json('C:\\Users\\Sonali\\Downloads\\classroom-test-ffd25d8801b2.json'))
    app.add_routes([web.get('/', app.classroom_service.root_index),
                    web.get('/fail', app.classroom_service.fail_route),
                    web.get('/classrooms', app.classroom_service.get_classroom_names),
                    web.get('/classrooms/{classroom_name}', app.classroom_service.get_classroom_video_names),
                    web.get('/classrooms/{classroom_name}/{video_number}',
                            app.classroom_service.get_a_classroom_video_url),
                    web.post('/classrooms/{classroom_name}/{video_number}/{search_term}',
                             app.classroom_service.search_video),
                    web.static('/', ""),
                    # This must be the last route
                    ])
    return app
