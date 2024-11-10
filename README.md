---

# QuickThoughts

QuickThoughts is a lightweight micro-sharing platform where users can post short thoughts, limited to 100 characters. The app allows for quick, straightforward sharing and interaction through reactions, fostering a minimalist social media experience. 

## Table of Contents

1. [Features](#features)
2. [Technology Stack](#technology-stack)
3. [Project Structure](#project-structure)
4. [Database Schema](#database-schema)
5. [Getting Started](#getting-started)
6. [Usage](#usage)
7. [Contributing](#contributing)
8. [License](#license)

## Features

- **User Authentication**: User registration and login using Firebase for secure authentication.
- **Post Thoughts**: Share short, concise posts (up to 100 characters).
- **React to Posts**: Users can react to posts with emojis.
- **Profile Management**: Edit profile information and view personal posts.
- **Admin Dashboard**: Manage users and moderate content to keep the platform safe and clean.
- **Real-time Feed**: Seamless updates for thoughts and reactions on the feed.

## Technology Stack

### Frontend
- **React** with TypeScript and Vite for a fast and type-safe development experience
- **Tailwind CSS** for a modern, responsive UI design

### Backend
- **Flask** for handling API requests
- **MySQL** for data storage and management
- **Firebase Authentication** for secure user authentication

## Project Structure

### Frontend (React with Vite, TypeScript, Tailwind CSS)
```
frontend/
├── public/
│   ├── index.html                    
│   ├── favicon.ico                  
│   └── manifest.json                
├── src/
│   ├── assets/                       
│   ├── components/                   
│   │   ├── Auth/                     
│   │   ├── Profile/                  
│   │   ├── Feed/                     
│   │   ├── Thought/                  
│   │   └── Admin/                    
│   ├── contexts/                     
│   ├── hooks/                        
│   ├── pages/                        
│   ├── services/                     
│   ├── styles/                       
│   ├── utils/                        
│   ├── App.tsx                       
│   ├── index.tsx                     
│   └── routes.tsx                    
├── tailwind.config.js                
├── tsconfig.json                     
└── package.json                      
```

### Backend (Flask with MySQL)
```
backend/
├── app/
│   ├── __init__.py                   
│   ├── auth.py                       
│   ├── config.py                     
│   ├── controllers/                  
│   ├── models/                       
│   ├── routes/                       
│   ├── schemas/                      
│   ├── services/                     
│   └── utils/                        
├── migrations/                       
├── config.py                         
├── requirements.txt                  
└── run.py                            
```

## Database Schema

1. **User Table**:
   - `user_id`: Primary key, unique identifier for each user.
   - `username`: User's display name.
   - `bio`: Short bio of the user.
   - `profile_picture`: URL to profile picture.
   - `firebase_uid`: Firebase unique identifier.

2. **Thought Table**:
   - `thought_id`: Primary key, unique identifier for each thought.
   - `user_id`: Foreign key, associated user.
   - `content`: Content of the thought (up to 100 characters).
   - `timestamp`: Timestamp of when the thought was posted.

3. **Reaction Table**:
   - `reaction_id`: Primary key, unique identifier for each reaction.
   - `user_id`: Foreign key, associated user.
   - `thought_id`: Foreign key, associated thought.
   - `reaction_type`: Type of reaction (e.g., emoji).

## Getting Started

### Prerequisites

- [Node.js](https://nodejs.org/) and [npm](https://www.npmjs.com/)
- [Python](https://www.python.org/) and [pip](https://pip.pypa.io/)
- [MySQL](https://www.mysql.com/)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/setab/QuickThough_app.git
   cd QuickThough_app
   ```

2. **Set up the Backend**:
   - Go to the `backend/` directory.
   - Install dependencies:
     ```bash
     pip install -r requirements.txt
     ```
   - Configure Firebase and MySQL connection in `config.py`.
   - Run migrations to set up the database schema:
     ```bash
     flask db upgrade
     ```
   - Start the Flask server:
     ```bash
     flask run
     ```

3. **Set up the Frontend**:
   - Go to the `frontend/` directory.
   - Install dependencies:
     ```bash
     npm install
     ```
   - Start the development server:
     ```bash
     npm run dev
     ```

4. **Access the Application**:
   - Frontend is available at `http://localhost:3000` (default Vite port).
   - Backend is available at `http://localhost:5000` (default Flask port).

## Usage

1. **Register** a new account and log in.
2. **Post a thought**: Share your thoughts (within 100 characters).
3. **React to thoughts**: Use emoji reactions on thoughts.
4. **Edit profile**: Update your bio, profile picture, and other details.
5. **Admin dashboard**: Access for admins to manage users and content.

## Contributing

We welcome contributions! To get started:

1. Fork the repository and create your branch: `git checkout -b feature/YourFeature`.
2. Commit your changes: `git commit -m 'Add some feature'`.
3. Push to the branch: `git push origin feature/YourFeature`.
4. Open a pull request.

Please make sure to update tests as appropriate and follow coding conventions.

## License
NO license its my personal project

---
