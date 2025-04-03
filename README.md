# Destination Review App with Session-based Authentication

## Description

This application allows users to create, edit, and manage reviews of destinations they have visited. Users can share their reviews publicly or keep them private. The app implements session-based authentication to ensure users own and control their data.

## Features

- **User Authentication:** Users can create an account, log in, and manage their sessions securely.
- **Destination Management:** Users can add, edit, and delete reviews for destinations they've visited.
- **Public/Private Sharing:** Users can choose to share their reviews publicly or keep them private.
- **Session-based Authentication:** Keeps track of logged-in users and manages access to sensitive data.

### General Routes

- **GET /**: Renders a page displaying the 5 most recent publicly shared destinations and their information. Includes links to the /users/new and /sessions/new pages. If the user is logged in, they see a link to the /destinations page instead.

- **GET /users/new**: Renders a page with a form to create a new user account. After account creation, the user is logged in and redirected to the /destinations page.

- **GET /sessions/new**: Renders a page with a form to sign in to an existing account. Upon login, the user is redirected to the /destinations page.

### User Authentication Routes

- **POST /users**: Accepts form data to create a new user. Performs validation checks on email and password. If successful, the user is created, a session is established, and the user is redirected to the /destinations page.

- **POST /sessions**: Accepts form data for login, finds the user by email, and validates their password. Upon successful login, a session is created, and the user is redirected to the /destinations page.

- **POST /sessions/destroy**: Destroys the current user’s session and redirects them to the / page.

### Destination Routes

- **GET /destinations**: Renders a list of all destinations belonging to the logged-in user. Each destination has a link to its detailed page.

- **GET /destinations/new**: Renders a form to add a new destination. Submitting the form creates the destination and redirects to the /destinations page.

- **POST /destinations**: Accepts form data for a new destination, creates the destination in the database, and associates it with the current user. Redirects to the /destinations page.

- **GET /destinations/:id**: Displays a page with a form to edit the details of a destination. The user can also delete the destination from this page. If the destination does not belong to the user or doesn't exist, a 404 error is returned.

- **POST /destinations/:id**: Accepts form data to update an existing destination. If the destination belongs to the user, it is updated; otherwise, a 404 error is returned.

- **POST /destinations/:id/destroy**: Deletes a destination if it belongs to the current user. If the user does not own the destination, a 404 error is returned.

## Authentication

The application uses **session-based authentication**, and sessions are managed using session tokens stored in cookies.

### Middleware

- **Session Middleware**: Reads the session token from the cookie, finds the associated session, and attaches the corresponding user to the request. If no session is found and the route requires authentication, the user is redirected to the /sessions/new page.

### Session-based Authentication

- **User Registration:** A user is created only if their email is unique and their password meets minimum requirements (at least 8 characters and contains a number).
- **User Login:** A user can log in using their email and password. The session token is then stored in the user's cookie.
- **Session Destruction:** Users can log out, which will destroy their session and remove the session token from the cookie.

## Installation

### Prerequisites

Ensure that you have the following installed:

- Node.js
- A relational database (e.g., PostgreSQL, MySQL)

### Steps to Run the Application

1. Clone the repository:
   ```
   git clone https://github.com/your-repo/destination-review-app.git
   ```
2. Install dependencies:
   ```
   npm install
   ```
3. Set up your database and apply migrations (e.g., using Sequelize or another ORM):
   ```
   npm run migrate
   ```
4. Start the application:
   ```
   npm start
   ```
5. Access the app in your browser at `http://localhost:3000`.

## Conclusion

This application provides a simple, user-friendly interface to manage reviews for destinations. With session-based authentication and basic CRUD operations, users can easily manage their own data while having control over sharing it publicly or privately.
