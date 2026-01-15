# Papermint - CRM & Sales Management System

A full-stack CRM and Sales Management system built with Django backend and React frontend. Manage users, leads, customers, deals, and tasks with role-based access control and a modern, responsive interface.

This project focuses on clean architecture, scalable data models, real-world CRM workflows, and seamless integration between frontend and backend.

---

## Tech Stack

### Backend

- **Framework**: Django 6.0+
- **API**: Django REST Framework (DRF)
- **Database**: SQLite (development)
- **Authentication**: JWT (JSON Web Tokens) with Simple JWT
- **ORM**: Django ORM
- **CORS**: django-cors-headers

### Frontend

- **Framework**: React 19+
- **Build Tool**: Vite 7+
- **Routing**: React Router DOM 7+
- **HTTP Client**: Axios
- **Styling**: CSS
- **Node Version**: 18+

---

## Project Structure

```
papermint/
├── crm-frontend/                 # React Frontend Application
│   ├── src/
│   │   ├── api/                  # API service layer
│   │   │   ├── auth.js           # Authentication API
│   │   │   ├── axios.js          # Axios configuration
│   │   │   ├── customers.js      # Customer API calls
│   │   │   ├── deals.js          # Deal API calls
│   │   │   └── leads.js          # Lead API calls
│   │   ├── auth/                 # Authentication components
│   │   │   ├── AuthContext.jsx   # Auth context provider
│   │   │   └── ProtectedRoute.jsx# Protected route wrapper
│   │   ├── components/           # Reusable components
│   │   │   ├── Navbar.jsx
│   │   │   └── Navbar.css
│   │   ├── pages/                # Page components
│   │   │   ├── Login.jsx
│   │   │   ├── Register.jsx
│   │   │   ├── Dashboard.jsx
│   │   │   ├── Customers.jsx
│   │   │   ├── Deals.jsx
│   │   │   ├── Leads.jsx
│   │   │   └── Tasks.jsx
│   │   ├── App.jsx               # Main app component
│   │   ├── main.jsx              # Entry point
│   │   ├── App.css
│   │   └── index.css
│   ├── package.json
│   ├── vite.config.js
│   ├── eslint.config.js
│   └── index.html
│
├── crm_backend/                  # Django Backend Application
│   ├── crm_backend/              # Project settings
│   │   ├── settings.py           # Django settings
│   │   ├── urls.py               # Main URL routing
│   │   ├── wsgi.py               # WSGI config
│   │   └── asgi.py               # ASGI config
│   │
│   ├── core/                     # Main app
│   │   ├── models/               # Data models
│   │   │   ├── base.py           # Base model with timestamps
│   │   │   ├── user.py           # Custom User model
│   │   │   ├── lead.py           # Lead model
│   │   │   ├── customer.py       # Customer model
│   │   │   ├── deal.py           # Deal model
│   │   │   ├── task.py           # Task model
│   │   │   ├── activity.py       # Activity/Log model
│   │   │   └── __init__.py
│   │   │
│   │   ├── api/                  # REST API
│   │   │   ├── urls.py           # API routes
│   │   │   ├── permissions.py    # Custom permissions
│   │   │   ├── views/            # API views
│   │   │   │   ├── auth.py       # Auth endpoints
│   │   │   │   ├── customer.py   # Customer endpoints
│   │   │   │   ├── lead.py       # Lead endpoints
│   │   │   │   ├── deal.py       # Deal endpoints
│   │   │   │   └── task.py       # Task endpoints
│   │   │   └── serializers/      # DRF serializers
│   │   │       ├── auth.py
│   │   │       ├── customer.py
│   │   │       ├── lead.py
│   │   │       ├── deal.py
│   │   │       └── task.py
│   │   │
│   │   ├── admin/                # Django Admin config
│   │   │   ├── user.py
│   │   │   ├── customer.py
│   │   │   ├── lead.py
│   │   │   ├── deal.py
│   │   │   ├── task.py
│   │   │   └── activity.py
│   │   │
│   │   ├── services/             # Business logic
│   │   │   ├── lead_service.py
│   │   │   ├── deal_service.py
│   │   │   └── task_service.py
│   │   │
│   │   ├── constants/            # Constants and choices
│   │   │   └── deal_pipeline.py  # Deal pipeline stages
│   │   │
│   │   ├── migrations/           # Database migrations
│   │   ├── apps.py
│   │   ├── exceptions.py         # Custom exceptions
│   │   ├── tests.py
│   │   └── __init__.py
│   │
│   ├── db.sqlite3                # SQLite database
│   ├── manage.py
│   └── requirements.txt           # Python dependencies
│
└── README.md
```

---

## Core Features

- ✅ **User Authentication** - JWT-based login/register with role-based access
- ✅ **Lead Management** - Create, update, and track sales leads
- ✅ **Customer Management** - Convert leads to customers and manage customer data
- ✅ **Deal Tracking** - Manage sales opportunities with pipeline stages
- ✅ **Task Management** - Create tasks linked to leads, customers, or deals
- ✅ **Activity Logging** - Track all changes and interactions
- ✅ **Role-Based Access Control** - Admin, Manager, and Sales roles with different permissions
- ✅ **Dashboard** - Overview of key metrics and data
- ✅ **Responsive UI** - Mobile-friendly React frontend
- ✅ **RESTful API** - Complete API with proper error handling

---

## User Roles & Permissions

| Role    | Description                      | Permissions                          |
| ------- | -------------------------------- | ------------------------------------ |
| Admin   | Full system access               | All CRUD operations, user management |
| Manager | Assign leads, deals, and tasks   | View all, assign to sales team       |
| Sales   | Work on assigned leads and tasks | View assigned, create tasks/deals    |

---

## API Documentation

### Authentication Endpoints

- `POST /api/auth/register/` - Register new user
- `POST /api/auth/login/` - Login user (returns JWT tokens)
- `POST /api/auth/logout/` - Logout user
- `POST /api/auth/token/refresh/` - Refresh JWT token
- `GET /api/auth/me/` - Get current user info

### Resource Endpoints

- `GET/POST /api/leads/` - List/create leads
- `GET/PUT/DELETE /api/leads/{id}/` - Get/update/delete lead
- `GET/POST /api/customers/` - List/create customers
- `GET/PUT/DELETE /api/customers/{id}/` - Get/update/delete customer
- `GET/POST /api/deals/` - List/create deals
- `GET/PUT/DELETE /api/deals/{id}/` - Get/update/delete deal
- `GET/POST /api/tasks/` - List/create tasks
- `GET/PUT/DELETE /api/tasks/{id}/` - Get/update/delete task

### Request/Response Format

All endpoints accept and return JSON:

**Example Login Request:**

```json
{
  "username": "sales1",
  "password": "StrongPass123"
}
{
    "username": "admin1",
    "password": "Admin@123"
}
{
  "username": "sales2",
  "password": "sales2@123"
}
```

**Example Login Response:**

```json
{
  "user": {
    "id": 1,
    "email": "user@example.com",
    "full_name": "John Doe",
    "role": "manager"
  },
  "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

---

## Data Models Overview

### User

- Custom Django model extending AbstractUser
- Fields: email, full_name, phone, role, is_active
- Roles: admin, manager, sales

### Lead

- Represents a potential customer
- Fields: name, email, phone, company, status, assigned_to, created_by
- Status options: new, contacted, qualified, unqualified
- Can be converted to Customer or Deal

### Customer

- Represents a confirmed client
- Fields: name, email, phone, company, industry
- Created after successful lead conversion
- Tracks customer relationship details

### Deal

- Represents a business opportunity
- Fields: name, value, stage, assigned_to, customer
- Stages: prospecting, qualification, proposal, negotiation, closed_won, closed_lost
- Tracks deal progress and revenue

### Task

- Action items and follow-ups
- Fields: title, description, assigned_to, related_to (lead/customer/deal), due_date, priority, status
- Priority: low, medium, high, urgent
- Status: pending, in_progress, completed, cancelled
- **Constraint**: Can be linked to exactly ONE of: Lead, Customer, or Deal

### Activity

- Logs all changes and interactions
- Fields: user, content_type, object_id, action, timestamp
- Used for audit trail and history tracking

---

## Task Design Decision

The system uses a **Multiple ForeignKey approach** for tasks:

```
task.lead (optional ForeignKey to Lead)
task.customer (optional ForeignKey to Customer)
task.deal (optional ForeignKey to Deal)
```

Only one relationship is allowed per task, enforced using model-level validation:

```python
def clean(self):
    relationships = [self.lead, self.customer, self.deal]
    if sum(1 for r in relationships if r is not None) != 1:
        raise ValidationError("Task must be linked to exactly one of: Lead, Customer, or Deal")
```

**Rationale:**

- ✅ Better readability and cleaner code
- ✅ Easier and faster queries
- ✅ Cleaner admin interface
- ✅ Strong data integrity enforcement
- ✅ Prevents data inconsistencies

---

## Deal Pipeline

The deal pipeline follows these stages:

1. **Prospecting** - Initial lead qualification
2. **Qualification** - Lead meets criteria
3. **Proposal** - Proposal sent to customer
4. **Negotiation** - Terms being discussed
5. **Closed Won** - Deal successfully completed
6. **Closed Lost** - Deal unsuccessful

---

## Setup Instructions

### Prerequisites

- Python 3.10+
- Node.js 18+
- npm or yarn
- Git

### Backend Setup

1. **Navigate to backend directory**

```bash
cd crm_backend
```

2. **Create virtual environment**

```bash
python -m venv venv
```

3. **Activate virtual environment**

   - On Windows:

   ```bash
   venv\Scripts\activate
   ```

   - On macOS/Linux:

   ```bash
   source venv/bin/activate
   ```

4. **Install dependencies**

```bash
pip install -r requirements.txt
```

5. **Apply migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```

6. **Create superuser (admin account)**

```bash
python manage.py createsuperuser
```

You'll be prompted to enter:

- Username
- Email
- Password
- Password confirmation

7. **Run development server**

```bash
python manage.py runserver
```

The backend will be available at: `http://localhost:8000`

### Frontend Setup

1. **Navigate to frontend directory**

```bash
cd crm-frontend
```

2. **Install dependencies**

```bash
npm install
```

3. **Start development server**

```bash
npm run dev
```

The frontend will be available at: `http://localhost:5173`

4. **Build for production**

```bash
npm run build
```

5. **Preview production build**

```bash
npm run preview
```

### Environment Variables

Create a `.env` file in the `crm-frontend` directory:

```
VITE_API_BASE_URL=http://localhost:8000
```

For backend, environment variables can be configured in `crm_backend/settings.py`

---

## Running the Application

### Run Both Frontend and Backend (Recommended)

**Terminal 1 - Backend:**

```bash
cd crm_backend
source venv/bin/activate  # or venv\Scripts\activate on Windows
python manage.py runserver
```

**Terminal 2 - Frontend:**

```bash
cd crm-frontend
npm run dev
```

Then open your browser and navigate to: `http://localhost:5173`

### Accessing Admin Panel

- URL: `http://localhost:8000/admin`
- Use the superuser credentials created during setup

---

## Development Workflow

1. **Backend Development**

   - Models are defined in `core/models/`
   - API views in `core/api/views/`
   - Serializers in `core/api/serializers/`
   - Business logic in `core/services/`

2. **Frontend Development**

   - Page components in `src/pages/`
   - Reusable components in `src/components/`
   - API calls in `src/api/`
   - Styling with CSS in respective directories

3. **Making Changes**

   - Backend: No server restart needed for model changes, run migrations
   - Frontend: Auto-refresh on file save with Vite

4. **Database Changes**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

---

## Testing

Backend tests are located in `core/tests.py`. Run tests with:

```bash
python manage.py test
```

Frontend testing can be set up with jest or vitest.

---

## Common Issues & Troubleshooting

### Backend Issues

**CORS Error:**

- Ensure `CORS_ALLOWED_ORIGINS` in settings.py includes your frontend URL
- Default: `http://localhost:5173`

**Database Issues:**

- Delete `db.sqlite3` and run migrations again
- ```bash
  rm db.sqlite3
  python manage.py migrate
  ```

**Port Already in Use:**

- Run on different port: `python manage.py runserver 8001`

### Frontend Issues

**Port 5173 Already in Use:**

- Change port in `vite.config.js` or run: `npm run dev -- --port 5174`

**API Connection Issues:**

- Check `.env` file has correct `VITE_API_BASE_URL`
- Ensure backend is running on correct port

**Module Not Found:**

- Reinstall dependencies: `npm install`
- Clear cache: `rm -rf node_modules && npm install`

---

## Security Considerations

- ⚠️ **SECRET_KEY** in settings.py should be changed for production
- ⚠️ **DEBUG** should be set to `False` in production
- ⚠️ Use environment variables for sensitive data
- ⚠️ Implement HTTPS in production
- ⚠️ Set secure CORS origins in production
- ⚠️ Use strong passwords for superuser account
- ⚠️ Implement rate limiting on API endpoints
- ⚠️ Add CSRF tokens for state-changing operations

---

## Future Improvements

- [ ] Email notifications for tasks and reminders
- [ ] Calendar integration for tasks and deals
- [ ] File upload capability for leads/customers
- [ ] Advanced reporting and analytics
- [ ] Bulk import of leads from CSV
- [ ] Email sync integration (Gmail, Outlook)
- [ ] Mobile app (React Native)
- [ ] Real-time notifications (WebSockets)
- [ ] Advanced search and filtering
- [ ] Export data to PDF/Excel
- [ ] AI-powered lead scoring
- [ ] SMS notifications
- [ ] API documentation (Swagger/OpenAPI)
- [ ] Comprehensive test suite

---

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## License

This project is open source and available under the MIT License.

---

## Support

For issues, questions, or suggestions, please open an issue on GitHub or contact the development team.

---

## Project Status

**Current Version:** 1.0.0 (Beta)

**Last Updated:** January 2026

The project is actively under development with new features being added regularly.
