# Getting Things Done

## Project Description

Getting Things Done is a task management kanban board web application. It allows users to manage their tasks in a visual and intuitive way. The application is synchronized online, allowing for real-time updates and collaboration.

## Features

- User signup: Users can create an account to manage their tasks.
- Customizable Kanban board: The board defaults to Draft-Task-Action-Project-Commission-Done, but users can modify it to suit their needs.
- Tagging: Users can tag items in the Kanban board with #, allowing for easy organization and searchability.
- Search: Users can search by the name of the tag or task.

## Local Setup

1. Clone the repository: `git clone https://github.com/ryankwondev/getting-things-done.git`
2. Navigate to the project directory: `cd getting-things-done`
3. Install the dependencies: `npm install`
4. Start the application: `npm start`

## Deployment

The application can be deployed using Docker-compose. Here are the steps:

1. Build the Docker image: `docker build -t getting-things-done .`
2. Run the Docker-compose file: `docker-compose up`
