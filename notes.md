#### dev notes

-   Lean MVP

    -   time box your spec
    -   write the spec
    -   cut your spec
    -   Don't fall in love with your MVP

-   tech

    -   use flask to implement a JSON API

        -   make flask render JSON, instead of having Flask render HTML

    -   frontend client consumes this API

    -   serve the static client from nginx proxy, and route api requests to uwsgi/gunicorn

-   learn more about NEXTJS

    -   TODO

-   setup the proj structure - flask + ~~nextjs~~

    -   flask

        -   Flask backend is strictly an API server, we will never be serving complete pages

        > source l2env/bin/activate
        > python3 app.py

    -   reactJS lib

        -   Django Rest Framework and react using axios to make api calls
            REST is the most mainstream and easiest to find info on
            I deploy the react inside django(transfer build files into django) but can be deployed seperately as well.

    -   deploy on cloudflare

    -   block-party

        -   Our browser extension product, Privacy Party, is built in React.js and SCSS, with core automations primarily in JavaScript. The application backend is handled by a Python Flask service with a GraphQL API and persistent data backed by a Postgres database via SQLAlchemy/Alembic. Our cloud infrastructure is hosted on Render and AWS.

    -   dash or taipy

    -   LLM Applications with LangChain Tutorial
        -   llama-cpp-python

#### business ideas

-   anonymous peer support community

    -   competitors

        -   togetherall
        -   koko
        -   mindhk
        -   timelycare
        -   CanChat – Cantonese Empathetic Chatbot for Secondary School Student

    -   tech

-   speech studio 发音评估

-   2books

    -   free old books

-   turn data into insights, superfast and at scale

    -   sundial

-   rootd

-   过期知名域名

    -   使用 AI 向这些网站提供内容

-   其实你有了 idea, 可以立马做个原型，自己同时做为开发者和用户，找找感觉。无论多粗糙都没关系，关键是能用起来。这样几次下来，就有感觉了，知道怎么把一个东西做成了。市场是否接受，是在这基础之上。你要是一开始不知道怎么启动第一个，可以把你的点子告诉我，我带你做一下。以后就可以自己开拓了。

#### reference

-   [python+JS](https://vercel.com/guides/how-to-use-python-and-javascript-in-the-same-application)

-   [CS142: Web Applications (Spring 2023)](https://web.stanford.edu/class/cs142/lectures.html)
-   [react-tutorial](https://www.runoob.com/react/react-tutorial.html)
-   [react](https://react.dev/learn)
