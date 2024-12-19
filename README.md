# MusicMatch

A web application that recommends personalized songs based on user preferences using AI.

## Project Structure

```
musicmatch/
├── frontend/           # Vue.js frontend application
│   ├── src/
│   │   ├── components/ # Reusable Vue components
│   │   ├── views/      # Page components
│   │   ├── services/   # API and business logic services
│   │   ├── types/      # TypeScript type definitions
│   │   ├── utils/      # Utility functions
│   │   ├── hooks/      # Custom Vue composables
│   │   └── constants/  # Constants and enums
│   └── ...
│
└── backend/            # Django backend application
    ├── users/          # User management app
    ├── recommendations/# Music recommendations app
    ├── musicmatch/     # Project settings
    └── ...
```

## Development Setup

1. Clone the repository
2. Set up the frontend:
   ```bash
   cd frontend
   cp .env.example .env  # Configure environment variables
   npm install
   ```

3. Set up the backend:
   ```bash
   cd backend
   cp .env.example .env  # Configure environment variables
   poetry install
   poetry run python manage.py migrate
   ```

4. Start development servers:
   ```bash
   # From project root
   npm run dev  # Starts both frontend and backend
   ```

## Environment Variables

### Frontend (.env)
- `VITE_API_URL`: Backend API URL
- `VITE_GEMINI_API_KEY`: Google Gemini API key

### Backend (.env)
- `DJANGO_SECRET_KEY`: Django secret key
- `DEBUG`: Debug mode flag
- `MONGODB_URI`: MongoDB connection URI
- `MONGODB_NAME`: MongoDB database name
- `JWT_SECRET_KEY`: JWT signing key
- `GEMINI_API_KEY`: Google Gemini API key# MusicMood
