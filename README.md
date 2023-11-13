# Real-time-Notification-Service
Developed a real-time notification service using the Nameko microservices framework to enhance user engagement and communication within a web application.



## Overview

The Real-time Notification Service is a microservices-based application built using Nameko, a microservices framework for Python. It provides real-time notifications to users through WebSocket communication, enabling seamless updates and engagement within a web application.

## Features

- **WebSocket Communication:** Utilizes WebSocket to enable real-time bidirectional communication between the server and connected clients.
- **Periodic Notifications:** Demonstrates sending periodic notifications to users using the Nameko microservices architecture.
- **MongoDB Integration:** Stores and retrieves user-specific notification data in MongoDB.

## Prerequisites

Before running the project, ensure you have the following installed:

- [Python](https://www.python.org/downloads/)
- [Nameko](https://nameko.readthedocs.io/en/stable/)
- [MongoDB](https://www.mongodb.com/try/download/community)
- [RabbitMQ](https://www.rabbitmq.com/download.html)

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/amiiirm8/real-time-notification-service.git
    cd real-time-notification-service
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Start RabbitMQ:

    ```bash
    # On Ubuntu
    sudo service rabbitmq-server start

    # On macOS with Homebrew
    brew services start rabbitmq
    ```

4. Start MongoDB:

    ```bash
    mongod
    ```

5. Run the Nameko services:

    ```bash
    nameko run notification_service --config config.yaml
    nameko run websocket_service --config config.yaml
    nameko run database_service --config config.yaml
    ```

## Configuration

The configuration file `config.yaml` contains settings such as the AMQP URI for RabbitMQ. Modify it if needed.

## Usage

Open the `index.html` file in a web browser to establish a WebSocket connection and receive real-time updates.

## Contributing

Feel free to contribute to the project. Fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

---

Feel free to customize this README based on additional features, instructions, or specific details of your project. Add any relevant information that will help users understand and use your Real-time Notification Service.
