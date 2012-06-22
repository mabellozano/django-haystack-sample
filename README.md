## SearchBox.io Sample Django Haystack Application.

This example illustrates basic search features of SearchBox.io (ElasticSearch as service).

Each CRUD operation on documents is reflected to search index in real time.

To test SearchBox.io's search features, login as admin, create a new document and search it.

Sample application is using [Haystack](http://haystacksearch.org/) moduler search for Django and [pyelasticsearch (toastdriven fork)](https://github.com/toastdriven/pyelasticsearch) 
Python ElasticSearch client to integrate with SearchBox.io.

## Local Setup

Sample application requires a PostgreSQL database up and change 'URL': os.environ['SEARCHBOX_URL'], to 'URL': 'http://localhost:9200',

at settings.py pointing to your running ElasticSearch instance.

## Heroku Deployment

This sample can be deployed to Heroku with no change. With 2 steps application will be fully functional.

* Migrate database with `heroku run python manage.py syncdb`

* Install SearchBox ElasticSearch Addon.

Deploy sample application and experience real time search.
