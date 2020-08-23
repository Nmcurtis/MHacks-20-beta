from aiohttp import web
import app

webapp = app.create_app()
web.run_app(webapp)

# import json
#
# a_0 = {"id": 0, "title": "Why So Many People Want to be Writers", "url": "https://youtu.be/axXn_Vn2vYo"}
# a_1 = {"id": 1, "title": "How to Write Descriptively", "url": "https://youtu.be/RSoRzTtwgP4"}
# a_2 = {"id": 2, "title": "How to Build a Fictional World", "url": "https://youtu.be/ZQTQSbjecLg"}
#
# b_0 = {"id": 0, "title": "Why Study the Government?", "url": "https://youtu.be/lrk4oY7UxpQ"}
# b_1 = {"id": 1, "title": "The Bicameral Congress", "url": "https://youtu.be/n9defOwVWS8"}
# b_2 = {"id": 2, "title": "Congressional Elections", "url": "https://youtu.be/qxiD9AEX4Hc"}
#
# c_0 = {"id": 0, "title": "Early Programming", "url": "https://youtu.be/nwDq4adJwzM"}
# # c_1 = {"id": 1, "title": "", "url": ""}
# # c_2 = {"id": 2, "title": "a lesson", "url": "a url"}
#
# classes = {"College Writing 101": {"Lecture 1": a_0, "Lecture 2": a_1, "Lecture 3": a_2},
#            "Political Science 227": {"Lecture 1": b_0, "Lecture 2": b_1, "Lecture 3": b_2}}
# print(json.dumps(classes))
# f = open("classroom_video_urls.txt", "w")
# f.write(json.dumps(classes))
# f.close()
# f = open("classroom_video_urls.txt", "r")
# content = f.read()
#
# print(json.loads(content))
# print(json.loads(content)["Political Science 227"]['Lecture 1'])
