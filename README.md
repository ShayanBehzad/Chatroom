# Shayan's Chatroom

A real-time chat application built with Django, Channels, WebSockets, JavaScript, Daphne, and Docker.

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
2. Install dependencies: `pip install -r requirements.txt`
3. Create and apply database migrations: `python manage.py migrate`
4. Start the development server: `python manage.py runserver`

## Features

- Real-time chat functionality using WebSockets
- Authentication system
- Private and global chat rooms
- User profiles for editing and visualizing information
- Contact management system
- Automatic email notifications on registration (using Redis and Celery)
- Docker containerization for easy deployment

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

The application will be available at `http://www.shayanbehzad.ir/chatroom/` (assuming you're running on localhost).

## Contributing

Contributions are welcome! Please fork the repository and submit pull requests.


# 

 * [x] Set the register app with login-register-logout and sending welcome mail tec
 * [x] Build a simple message sending system with websokecket protocol
 * [x] Build PV chatroom, profile and the ability to add user to contacts
 * [x] Front-End
 * [x] Dockerize 
 * [ ] Adding features like 'is typing'
