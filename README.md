# 📚 EBookStore Django Application

![Django](https://img.shields.io/badge/Django-4.2.22-green.svg)
![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen.svg)

A full-featured e-commerce web application built with Django, featuring user authentication, shopping cart functionality, order management, and integrated payment processing with Stripe and PayPal.

## 🌟 Features

### 👨‍💼 Admin Features
- **Dashboard Management**: Comprehensive admin interface for managing the entire store
- **Order Management**: View, process, and track customer orders
- **Product Management**: Add, edit, and manage product catalog
- **User Management**: Manage customer accounts and permissions
- **Analytics**: Track sales and customer behavior

### 🛍️ Customer Features
- **User Authentication**: Secure registration, login, and logout
- **Product Browsing**: Browse products by categories with search functionality
- **Shopping Cart**: Add/remove items, update quantities
- **Wishlist**: Save favorite products for later
- **Order Management**: Place orders, track status, view order history
- **Account Management**: Edit profile details, manage shipping addresses
- **Payment Processing**: Secure payments via Stripe and PayPal
- **Email Notifications**: Order confirmations and account updates

## 🏗️ Project Architecture

```mermaid
graph TB
    A[User Interface] --> B[Django Views]
    B --> C[Models]
    C --> D[SQLite Database]
    
    B --> E[Templates]
    E --> F[Static Files]
    
    B --> G[Payment Processing]
    G --> H[Stripe API]
    G --> I[PayPal API]
    
    J[Authentication] --> K[Custom User Model]
    K --> C
    
    L[Shopping Cart] --> M[Session Management]
    M --> B
    
    subgraph "Django Apps"
        N[Store App]
        O[Account App]
        P[Basket App]
        Q[Orders App]
        R[Checkout App]
        S[Core App]
    end
```

## 📁 Project Structure

```
EBookStore-Django-App/
├── 📁 account/              # User authentication and management
│   ├── models.py           # Custom user model
│   ├── views.py            # Authentication views
│   ├── forms.py            # User forms
│   └── urls.py             # Account URLs
├── 📁 basket/               # Shopping cart functionality
│   ├── basket.py           # Cart logic
│   ├── context_processors.py
│   └── views.py            # Cart views
├── 📁 checkout/             # Payment processing
│   ├── models.py           # Payment models
│   ├── views.py            # Checkout views
│   └── paypal.py           # PayPal integration
├── 📁 core/                 # Project settings and configuration
│   ├── settings/           # Environment-specific settings
│   ├── urls.py             # Main URL configuration
│   └── wsgi.py             # WSGI configuration
├── 📁 orders/               # Order management
│   ├── models.py           # Order models
│   └── views.py            # Order views
├── 📁 store/                # Product catalog
│   ├── models.py           # Product models
│   ├── views.py            # Store views
│   └── context_processors.py
├── 📁 static/               # Static files (CSS, JS, Images)
├── 📁 templates/            # HTML templates
├── 📁 tests/                # Test files
├── manage.py               # Django management script
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## 🛠️ Technology Stack

| Technology | Version | Purpose |
|------------|---------|---------|
| **Python** | 3.8+ | Backend programming language |
| **Django** | 4.2.22 | Web framework |
| **SQLite** | Default | Database (development) |
| **Stripe** | 9.8.0 | Payment processing |
| **PayPal** | SDK | Alternative payment method |
| **Pillow** | 10.3.0 | Image processing |
| **django-countries** | 7.6.1 | Country field support |
| **pytest** | Latest | Testing framework |
| **Coverage** | 7.3.2 | Code coverage analysis |

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/AAdewunmi/EBookStore-Django-App.git
   cd EBookStore-Django-App
   ```

2. **Create and activate virtual environment**
   ```bash
   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   
   # Windows
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables** (Optional)
   ```bash
   # Create .env file for production settings
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. **Run database migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create superuser account**
   ```bash
   python manage.py createsuperuser
   ```

7. **Load sample data** (Optional)
   ```bash
   python manage.py loaddata fixtures/sample_data.json
   ```

8. **Start development server**
   ```bash
   python manage.py runserver
   ```

9. **Access the application**
   - **Frontend**: http://127.0.0.1:8000/
   - **Admin Panel**: http://127.0.0.1:8000/admin/

### Default Login Credentials

```
Username: a@a.com
Password: djangoapp
```

## ⚙️ Configuration

### Payment Integration

#### Stripe Setup
1. Create a Stripe account at [stripe.com](https://stripe.com)
2. Get your API keys from the Stripe dashboard
3. Add to your environment variables:
   ```bash
   STRIPE_PUBLISHABLE_KEY=pk_test_your_key_here
   STRIPE_SECRET_KEY=sk_test_your_key_here
   STRIPE_ENDPOINT_SECRET=whsec_your_webhook_secret
   ```

#### PayPal Setup
1. Create a PayPal developer account
2. Create a new application
3. Configure your PayPal credentials in settings

### Email Configuration

For production, update email settings in `core/settings/base.py`:
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'your-smtp-server.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@example.com'
EMAIL_HOST_PASSWORD = 'your-password'
```

## 🧪 Testing

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=.

# Run specific app tests
pytest store/tests/

# Run with Django settings
pytest --ds=core.settings.base
```

### Test Structure

```
tests/
├── test_models.py          # Model tests
├── test_views.py           # View tests
├── test_forms.py           # Form tests
└── fixtures/               # Test data
```

## 📊 Database Schema

```mermaid
erDiagram
    Customer ||--o{ Order : places
    Customer ||--o{ Product : wishlists
    Order ||--o{ OrderItem : contains
    Product ||--o{ OrderItem : ordered_in
    Product }o--|| Category : belongs_to
    Product }o--|| ProductType : has_type
    Product ||--o{ ProductImage : has_images
    Product ||--o{ ProductSpecificationValue : has_specs
    
    Customer {
        int id PK
        string email
        string first_name
        string last_name
        boolean is_active
        datetime created_at
    }
    
    Product {
        int id PK
        string title
        text description
        decimal regular_price
        decimal discount_price
        boolean is_active
        datetime created_at
    }
    
    Order {
        int id PK
        string order_key
        decimal total_paid
        datetime created_at
        boolean billing_status
    }
```

## 🚀 Deployment

### Production Checklist

- [ ] Set `DEBUG = False` in production settings
- [ ] Configure proper database (PostgreSQL recommended)
- [ ] Set up static file serving (WhiteNoise or CDN)
- [ ] Configure email backend
- [ ] Set up SSL/HTTPS
- [ ] Configure payment gateway credentials
- [ ] Set up monitoring and logging
- [ ] Configure backup strategy

### Environment Variables

```bash
# Production settings
DEBUG=False
SECRET_KEY=your-secret-key-here
DATABASE_URL=postgresql://user:pass@localhost/dbname
STRIPE_PUBLISHABLE_KEY=pk_live_your_key
STRIPE_SECRET_KEY=sk_live_your_key
EMAIL_HOST=smtp.your-provider.com
EMAIL_HOST_USER=your-email@domain.com
EMAIL_HOST_PASSWORD=your-password
```

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Make your changes**
4. **Run tests**
   ```bash
   pytest
   ```
5. **Commit your changes**
   ```bash
   git commit -m 'Add amazing feature'
   ```
6. **Push to the branch**
   ```bash
   git push origin feature/amazing-feature
   ```
7. **Open a Pull Request**

### Code Style

- Follow PEP 8 guidelines
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Write tests for new features

## 🐛 Troubleshooting

### Common Issues

**Issue**: `ModuleNotFoundError: No module named 'django'`
**Solution**: Ensure virtual environment is activated and dependencies are installed

**Issue**: Database migration errors
**Solution**: 
```bash
python manage.py makemigrations --empty appname
python manage.py migrate --fake-initial
```

**Issue**: Static files not loading
**Solution**: Run `python manage.py collectstatic`

**Issue**: Payment integration not working
**Solution**: Verify API keys are correctly set in environment variables

### Getting Help

- Check the [Django documentation](https://docs.djangoproject.com/)
- Review existing [GitHub issues](https://github.com/AAdewunmi/EBookStore-Django-App/issues)
- Create a new issue with detailed description

## 📸 Screenshots

### Django Application Homepage
![Screenshot 2024-08-24 at 09 41 02](https://github.com/user-attachments/assets/5745f3df-fc78-4985-bbfa-a4ca11293a1c)

### User Login Interface
![Screenshot 2024-08-24 at 09 41 54](https://github.com/user-attachments/assets/2a925e75-454c-40a8-88f9-6addfb689623)

### Admin Dashboard
![Screenshot 2024-08-24 at 09 42 18](https://github.com/user-attachments/assets/df29478a-6677-4907-b17d-fbfe008d254e)

### Customer Dashboard
![Screenshot 2024-08-24 at 09 42 36](https://github.com/user-attachments/assets/1bbe7f2f-071a-40e5-9e8b-4dc7828b2dfe)

### Order Management
![Screenshot 2024-08-24 at 09 42 58](https://github.com/user-attachments/assets/36b6bd31-2855-426a-83cc-081cf2c27736)

### Profile Management
![Screenshot 2024-08-24 at 09 43 20](https://github.com/user-attachments/assets/1fa27053-d26b-4375-9f42-eb9e6ea49bf6)

### Address Management
![Screenshot 2024-08-24 at 09 43 41](https://github.com/user-attachments/assets/2d97e20c-1c00-4588-9a47-9792122d20d0)

### Wishlist Management
![Screenshot 2024-08-24 at 09 43 58](https://github.com/user-attachments/assets/cb051b70-14f0-46e6-b232-2d5182c20091)

## 🗺️ Roadmap

### Upcoming Features

- [ ] **Enhanced Search**: Elasticsearch integration for better product search
- [ ] **Reviews & Ratings**: Customer product reviews and rating system
- [ ] **Inventory Management**: Stock tracking and low inventory alerts
- [ ] **Multi-vendor Support**: Allow multiple sellers on the platform
- [ ] **Mobile App**: React Native mobile application
- [ ] **Advanced Analytics**: Detailed sales and customer analytics
- [ ] **Internationalization**: Multi-language support
- [ ] **Social Login**: OAuth integration with Google, Facebook, etc.

### Version History

- **v1.0.0** - Initial release with core e-commerce functionality
- **v1.1.0** - Added payment integration and order management
- **v1.2.0** - Enhanced user dashboard and wishlist features

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

This project was adapted from the excellent Django E-commerce tutorial series by **Very Academy**.

- **Original Project**: Django Ecommerce Project v1 2021
- **Created by**: [Very Academy](https://github.com/veryacademy)
- **YouTube Tutorial**: [Django E-commerce Series](https://www.youtube.com/watch?v=UqSJCVePEWU&list=PLOLrQ9Pn6caxY4Q1U9RjO1bulQp5NDYS_)
- **Original Repository**: [django-ecommerce-project](https://github.com/veryacademy/django-ecommerce-project)

Special thanks to the Django community and all contributors who have helped improve this project.

## 📞 Support

If you find this project helpful, please consider:

- ⭐ Starring the repository
- 🐛 Reporting bugs
- 💡 Suggesting new features
- 🤝 Contributing to the codebase

---

**Made with ❤️ using Django**
