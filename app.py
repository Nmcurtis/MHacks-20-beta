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

    async def get_a_classroom_video(self, req):
        bucket_name = req.match_info.get('classroom_name')
        video_number = req.match_info.get('video_number')
        classroom_names = json.loads(self.get_classroom_names())
        if bucket_name in classroom_names:
            classroom_bucket = self.client.get_bucket(bucket_name)
            blobs = classroom_bucket.list_blobs()
            classroom_videos = [blob.name for blob in blobs]
            requested_file = classroom_videos[int(video_number)]
            return web.FileResponse()
        else:
            print("Not a legit classroom bucket")

    async def search_video(self, req): # send search term to function?
        search_string = req.query['search_term']
        return 0

    async def root_index(self, _):
        return web.Response(text="testing")
        #return web.FileResponse("index.html")


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
                            app.classroom_service.get_a_classroom_video),
                    web.post('/classrooms/{classroom_name}/{video_number}/{search_term}',
                             app.classroom_service.search_video),
                    #web.static('/', ),
                    # This must be the last route
                    ])
    return app
