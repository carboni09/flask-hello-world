from flask import Flask
app = Flask(__name__)

#from apscheduler.schedulers.background import BackgroundScheduler
#from apscheduler.triggers.interval import IntervalTrigger


#scheduler = BackgroundScheduler()
#scheduler.start()


def job_function():
    print("Hello, World!")


# scheduler.add_job(
#     func=job_function,
#     trigger=IntervalTrigger(seconds=15),
#     id='my_job_id',
#     name='Print "Hello, World!" every minute',
#     replace_existing=True)




# @app.before_first_request
# def initialize():
#     # ... other initialization code ...
#     print('init')
#     #scheduler.start()

# @app.teardown_appcontext
# def shutdown_scheduler(exception=None):
#     scheduler.shutdown()

@app.route('/')
def hello_world():
    return 'Hello, World!!!!!!'
    
app.run(host='0.0.0.0')
