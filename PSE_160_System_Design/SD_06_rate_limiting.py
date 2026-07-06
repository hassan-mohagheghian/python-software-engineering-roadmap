# System Design - Message Queue
# -----------------------------------------------------------------------------
# A Message Queue (MQ) is a communication mechanism that enables services to
# exchange messages asynchronously.
#
# Instead of one service calling another directly, it sends a message to a
# queue. Another service consumes the message whenever it is ready.
#
# -----------------------------------------------------------------------------
# Why use a Message Queue?
#
# - Decouples services
# - Improves scalability
# - Handles traffic spikes
# - Supports asynchronous processing
# - Increases reliability
#
# -----------------------------------------------------------------------------
# High-Level Architecture
#
#           Producer
#               │
#               ▼
#         Message Queue
#               │
#               ▼
#           Consumer
#
# -----------------------------------------------------------------------------
# Real-world examples
#
# - Order processing
# - Sending emails
# - Image/video processing
# - Payment processing
# - Notification systems
#
# Common technologies:
# - RabbitMQ
# - Apache Kafka
# - Amazon SQS
# - Redis Streams
# -----------------------------------------------------------------------------


from collections import deque

# -----------------------------------------------------------------------------
# Message
# -----------------------------------------------------------------------------


class Message:
    def __init__(self, content: str):
        self.content = content


# -----------------------------------------------------------------------------
# Message Queue
# -----------------------------------------------------------------------------


class MessageQueue:
    """
    FIFO (First In, First Out) queue.
    """

    def __init__(self):
        self.queue = deque()

    def publish(self, message: Message):
        self.queue.append(message)
        print(f"[Queue] Message published: {message.content}")

    def consume(self):
        if not self.queue:
            print("[Queue] No messages available.")
            return None

        return self.queue.popleft()


# -----------------------------------------------------------------------------
# Producer
# -----------------------------------------------------------------------------


class OrderService:
    """
    Produces messages.
    """

    def __init__(self, queue: MessageQueue):
        self.queue = queue

    def create_order(self, order_id: int):
        print(f"[OrderService] Order {order_id} created.")

        self.queue.publish(Message(f"Process Order #{order_id}"))


# -----------------------------------------------------------------------------
# Consumer
# -----------------------------------------------------------------------------


class WorkerService:
    """
    Consumes messages.
    """

    def __init__(self, queue: MessageQueue):
        self.queue = queue

    def process_next_message(self):
        message = self.queue.consume()

        if message:
            print(f"[Worker] Processing: {message.content}")


# -----------------------------------------------------------------------------
# Usage
# -----------------------------------------------------------------------------


def main():
    queue = MessageQueue()

    order_service = OrderService(queue)
    worker = WorkerService(queue)

    # Producer publishes messages
    order_service.create_order(1001)
    order_service.create_order(1002)
    order_service.create_order(1003)

    print()

    # Consumer processes messages later
    worker.process_next_message()
    worker.process_next_message()
    worker.process_next_message()
    worker.process_next_message()


if __name__ == "__main__":
    main()
