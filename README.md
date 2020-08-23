# we-Learn
Turning e-Learning challenges into we-Learning opportunities!
Our MHacks 20 Beta Project

## Inspiration

Everyone's lives got overturned when COVID-19 hit, and students are no exception. As students ourselves, we've had to get used to the new normal of online learning, which brings about several challenges.

- Being able to refer back to your notes or handouts to search for a concept is pretty easy, but what about video lectures where there's a lot of information in the spoken word?

- Pointing out concepts in your notes to that nerdy friend who can explain it to you isn't exactly possible anymore, so what now?

- Being in class and hearing responses to your classmates' questions is a valuable source of learning, so how can you benefit from those targeted discussions?

## What it does

- we-Learn aims to bring back some of these missing aspects of in-person learning to the remote learning experience.

- With we-Learn, you can review important concepts in your lectures without a struggle. Simply search for keywords or phrases, and you'll be able to watch segments of the lesson where these concepts show up.

- Want to hear what your classmates and instructors are saying about a certain part of the lesson? we-Learn helps you do that too! When you start a video segment after a search, you can engage in discussions about that section all in one place. 

## How we built it

- Back-end

We used Python on the back-end with aiohttp to send and receive requests. We integrated the Google Cloud API, specifically Google Cloud Storage and Speech-to-Text. Storage buckets in Google Cloud Storage represented classes and with lecture videos in them. We used additional libraries (pytube, pydub) to access and manipulate the audio content of the videos, which was then processed using Google Cloud's Speech-to-Text Service. We then used the results to respond to requests from the front-end with aiohttp in Python.

- Front-end

The front-end of we-Learning was put together using Angular and Bootstrap for a clean, intuitive user interface.

## Challenges we ran into

- Making cross-origin requests was difficult until we could figure out how to set certain HTTP headers.
- Processing long audio segments via the Google Cloud API didn't behave the way we expected, so we had to find ways to split segments and still make sure the timestamps were mapped to correctly.
- Spending hours navigating large amounts of documentation to find answers was tough at times but very rewarding!

## Accomplishments that we're proud of

- An extremely beautiful UI!
- Building something that we'd find useful ourselves.
- Creating something that we think would foster connectivity in a socially disconnected time.
- Learning to use tools and technologies that some of us were completely unfamiliar with to make something cool.
- Managing to collaborate together well virtually!

## What we learned

- Google Cloud can do some seriously amazing things. 
- Challenges can be opportunities, perspective matters!

## What's next for we-Learn

- Adding the capability to also process text information embedded in the video visually, such as in slides, would be the main next step.
- Extending on the commenting by segment time for ease of collaboration, also being able to sort discussions by topic area would further foster social connection in the learning process.
