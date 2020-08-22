import json
from aiohttp import web
from google.cloud import storage


# client = storage.Client.from_service_account_json('classroom-test-ffd25d8801b2.json')
# classrooms_bucket = client.get_bucket('classroom_1')
# print(list(classrooms_bucket.list_blobs()))


class ClassroomsApp:
    def __init__(self, client):  # classroom list - list of classroom objects
        try:
            self.client = client
        except:
            print("Bucket doesn't exist")

    async def fail_route(self):
        raise Exception("Raised test exception")

    async def get_classrooms(self):
        classrooms = self.client.list_buckets()
        classroom_names = [classroom.name for classroom in classrooms]
        json.dumps(classroom_names)
        return web.json_response(data=classroom_names)

    async def get_classroom_videos(self, req):
        bucket_name = req.query['classroom_number']
        classroom_names = json.loads(self.get_classrooms())
        if bucket_name in classroom_names:
            classroom_bucket = self.client.get_bucket(bucket_name)
            blobs = classroom_bucket.list_blobs()
            classroom_videos = [blobs.name for blob in blobs]
            return web.json_response(data=classroom_videos)
        else:
            print("Not a legit classroom bucket")

    async def get_a_classroom_video(self, req):
        pass
        # content = await req.content.read()
        # decoded_content = content.decode()
        # self.pager_duty_key_store.add_key(json.loads(decoded_content))
        # return web.Response(text="Successfully added pager duty key")

    async def search_video(self, _):
        pass
        # all_keys = self.pager_duty_key_store.all_keys()
        # return web.json_response(data=obfuscate_keys(all_keys))

    async def root_index(self, _):
        return web.FileResponse("web/index.html")


async def on_prepare(_, response):
    response.headers['cache-control'] = 'no-cache'


def create_app():
    app = web.Application()
    app.on_response_prepare.append(on_prepare)
    app.classroom_service = ClassroomsApp(
        client=storage.Client.from_service_account_json('classroom-test-ffd25d8801b2.json'))
    app.add_routes([web.get('/', app.classroom_service.root_index),
                    web.get('/fail', app.classroom_service.fail_route),
                    web.get('/classrooms', app.classroom_service.get_classrooms),
                    web.get('/classrooms/{classroom_number}', app.classroom_service.get_classroom_videos),
                    web.get('/classrooms/{classroom_number}/{video_number}',
                            app.classroom_service.get_a_classroom_video),
                    web.post('/classrooms/{classroom_number}/{video_number}/{search_term}',
                             app.classroom_service.search_video),
                    web.static('/', "web"),
                    # This must be the last route
                    ])
    return app
