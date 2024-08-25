# Shayan's Chatroom

Welcome to the **Chatroom** project! This application is a feature-rich chat platform built using Django, Django Channels, WebSocket, JavaScript, Daphne, and it is fully Dockerized. The project is designed to offer real-time messaging with a variety of features, including private and global chatrooms, user profile management, contact lists, and automatic email notifications.

## Table of Contents

1. [Getting Started](#getting-started)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Deployment](#deployment)
6. [Contributing](#contributing)

## Getting Started

To get started with this chat application:

1. Clone the repository: `git clone https://github.com/ShayanBehzad/Chatroom.git`
2. Install dependencies: `docker-compose build`
3. Start the development server: `docker-compose up -d`


## Features

- **User Authentication**: Secure user registration, login, and logout functionalities.
- **Private Chatrooms**: Users can create and join private chatrooms for personal conversations.
- **Global Chatroom**: A public chatroom where all registered users can communicate.
- **Profile Section**: Users can view and edit their profile information.
- **Contacts Management**: Users can add and manage contacts.
- **Real-time Messaging**: Leveraging Django Channels and WebSockets for real-time message delivery.
- **Email Notifications**: Automatic email sending upon registration, powered by Redis and Celery.
- **Dockerized Setup**: The entire application is containerized using Docker for easy deployment and scalability.

## Installation

To install this application:

1. Install Django: `pip install django`
2. Install Channels: `pip install channels`
3. Install Daphne: `pip install daphne`
4. Install Redis: `docker run -p 6379:6379 -d redis:latest` (or use your local Redis instance)

## Usage

### Authentication

- Users can register and log in to access chat features
- The authentication system uses Django's built-in auth system

### Chat Rooms

- Private chat rooms: Users can create private rooms for specific conversations
- Global chat room: A public space for all users

### User Profiles

- Users can edit their profiles
- Profile information is displayed on the chat interface

### Contacts

- Users can add contacts to their list
- Contacts are displayed on the chat interface for quick access

### Email Notifications

- New user registration triggers an automatic email notification
- This feature is implemented using Redis and Celery

## Deployment

The application is available at http://www.shayanbehzad.ir/chatroom/.

## Contributing

Contributions are welcome! Please fork the repository and submit pull requests.


# 

 * [x] Set the register app with login-register-logout and sending welcome mail tec
 * [x] Build a simple message sending system with websokecket protocol
 * [x] Build PV chatroom, profile and the ability to add user to contacts
 * [x] Front-End
 * [x] Dockerize 
 * [ ] Adding features like 'is typing'
