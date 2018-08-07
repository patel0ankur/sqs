import boto3

#Client connection for aws services
sqs = boto3.resource('sqs', region_name='us-east-1')

#Variables used to create servioe
queue_name = "atomwise_queue"



# Function to create some sample messages to queue
def create_sqs_messages(queue_name):
    queue = sqs.get_queue_by_name(QueueName=queue_name)
    for i in range(0, 5000):
        queue_response = queue.send_message(MessageBody='This is test message #' + str(i))
        print(queue_response['MessageId'])

create_sqs_messages(queue_name)
