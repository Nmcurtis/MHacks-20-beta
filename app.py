import json
from aiohttp import web
from google.cloud import storage
import aiohttp_cors


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
        # classrooms = self.client.list_buckets()
        # classroom_names = [classroom.name for classroom in classrooms]
        # if bucket_name in classroom_names:
        #     classroom_bucket = self.client.get_bucket(bucket_name)
        #     blobs = classroom_bucket.list_blobs()
        #     classroom_video_links = [blob.name for blob in blobs]
        #     requested_video = classroom_video_links[int(video_number)]
        #     return web.Response(text=requested_video)
        # else:
        #     print("Not a legit classroom bucket")
        f = open("classroom_video_urls.txt", "r")
        content = f.read()
        content = json.loads(content)
        url = {"url": content['Political Science 227']['Lecture 1']}
        return web.json_response(url)

    async def search_video(self, req):  # send search term to function?
        class_name = req.match_info.get('classroom_name')
        lec_num = req.match_info.get('video_number')
        search_string = req.match_info.get('search_term')
        # timestamp = theProcessingFunction(classroom_name, video_number, search_string)
        # timestamp = search_transcript(search_string)
        # f = open("classroom_video_urls.txt", "r")
        # content = f.read()
        # content = json.loads(content)
        # new_url = content['Political Science 227']['Lecture 1']['url'] + "?start=" + str(timestamp)
        timestamps = get_all_occurrences(search_string)
        url = {"url": timestamps}
        return web.json_response(url)

    async def root_index(self, _):
        return web.FileResponse("angular/src/index.html")


async def on_prepare(_, response):
    response.headers['cache-control'] = 'no-cache'


def search_transcript(words, word_num_offset, search_phrase):  # return all occurrences
    f = open("transcripts/Political_Science_227/Introduction_Crash_Course_US_Government_and_Politics.json", "r")
    content = f.read()
    content = json.loads(content)

    if search_phrase in words:
        i = words.find(search_phrase)
        #print(i)
        prev_words = words[:i]
        #print(prev_words)
        num = len(prev_words.split(" ")) - 1 + word_num_offset
        print("word num", num)
        print(content["words"][num]["word"])
        timestamp = content["words"][num]['startTime']
        print("timestamp", timestamp)
    else:
        return '0', 0, 0, 0
    return timestamp[0], timestamp, i, num


def get_all_occurrences(search_phrase):
    len_phrase = len(search_phrase)
    timestamps = []
    word_num_offset = 0
    f = open("transcripts/Political_Science_227/Introduction_Crash_Course_US_Government_and_Politics.json", "r")
    content = f.read()
    content = json.loads(content)
    words = content['transcript']

    print("OG transcript", words)
    while True:
        url_timestamp, timestamp, char_num, word_num = search_transcript(words, word_num_offset, search_phrase)
        if url_timestamp == '0':
            break
        timestamps.append(url_timestamp)
        word_list = words.split(" ")
        less_words_list = word_list[(word_num+1):]
        separator = ' '
        words = separator.join(less_words_list)
        word_num_offset += word_num + 1
        print("next search phrase", words)
    return timestamps

print(get_all_occurrences("asskdjfg"))

def create_app():
    app = web.Application()
    app.on_response_prepare.append(on_prepare)
    app.classroom_service = ClassroomsApp(
        client=storage.Client.from_service_account_json(
            'C:\\Users\\Sonali\\Downloads\\classroom-test-ffd25d8801b2.json'))

    app.add_routes([web.get('/', app.classroom_service.root_index),
                    web.get('/fail', app.classroom_service.fail_route),
                    web.get('/classrooms', app.classroom_service.get_classroom_names),
                    web.get('/classrooms/{classroom_name}', app.classroom_service.get_classroom_video_names),
                    web.get('/classrooms/{classroom_name}/{video_number}',
                            app.classroom_service.get_a_classroom_video_url),
                    web.get('/classrooms/{classroom_name}/{video_number}/{search_term}',
                            app.classroom_service.search_video),
                    # This must be the last route
                    ])

    # Configure default CORS settings.
    cors = aiohttp_cors.setup(app, defaults={
        "*": aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            expose_headers="*",
            allow_headers="*",
        )
    })

    # Configure CORS on all routes.
    for route in list(app.router.routes()):
        cors.add(route)

    return app
