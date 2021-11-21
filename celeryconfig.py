broker_url = 'amqp://guest@localhost//'

task_routes = {
    'tasks.add': 'low-priority',
}
