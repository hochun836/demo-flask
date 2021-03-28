from app import app, scheduler


@scheduler.task('interval', id='do_job_1', seconds=10, misfire_grace_time=900)
def job1():
    app.logger.debug('Job 1 executed')
