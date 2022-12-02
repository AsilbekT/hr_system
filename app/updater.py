from apscheduler.schedulers.background import BackgroundScheduler
from .views import send_posts


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(send_posts, 'interval', seconds=60)
    scheduler.start()
