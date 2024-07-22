backend/
│
├── controllers/
│   ├── AuthController.py
│   │   - register_user()
│   │   - login_user()
│   │   - logout_user()
│   ├── UserController.py
│   │   - get_user_profile()
│   │   - update_user_profile()
│   │   - delete_user()
│   ├── ExpenseController.py
│   │   - add_expense()
│   │   - get_expenses()
│   │   - update_expense()
│   │   - delete_expense()
│   ├── BudgetController.py
│   │   - set_budget()
│   │   - get_budget_summary()
│   │   - update_budget()
│   │   - delete_budget()
│   └── ReminderController.py
│       - set_reminder()
│       - get_reminders()
│       - delete_reminder()
│
├── services/
│   ├── AuthService.py
│   │   - create_user()
│   │   - authenticate_user()
│   │   - authenticateUser(credentials: object): Promise
│   │   - generateJWT(payload: object, expiresIn: string): string
│   │   - refreshJWT(token: string): Promise
│   │   - logout_user()
│   ├── UserService.py
│   │   - get_user_profile()
│   │   - update_user_profile()
│   │   - delete_user()
│   │   - trackLoginAttempts(userId: string): Promise
│   ├── ExpenseService.py
│   │   - add_expense()
│   │   - get_expenses()
│   │   - update_expense()
│   │   - delete_expense()
│   ├── BudgetService.py
│   │   - set_budget()
│   │   - get_budget_summary()
│   │   - update_budget()
│   │   - delete_budget()
│   └── ReminderService.py
│       - set_reminder()
│       - get_reminders()
│       - delete_reminder()
│
├── models/
│   ├── UserModel.py
│   │   - _save()
│   │   - _delete()
│   │   - _update_profile()
│   ├── ExpenseModel.py
│   │   - _save()
│   │   - _delete()
│   │   - _update_details()
│   ├── BudgetModel.py
│   │   - _save()
│   │   - _delete()
│   ├── ReminderModel.py
│   │   - _save()
│   │   - _delete()
│
├── database/
│   ├── UserDB.py
│   │   - _create_user()
│   │   - _get_user_by_email()
│   │   - _update_user_profile()
│   ├── ExpenseDB.py
│   │   - _add_expense()
│   │   - _get_expenses()
│   │   - _update_expense()
│   │   - _delete_expense()
│   ├── BudgetDB.py
│   │   - _set_budget()
│   │   - _get_budget_summary()
│   │   - _update_budget()
│   │   - _delete_budget()
│   ├── ReminderDB.py
│   │   - _set_reminder()
│   │   - _get_reminders()
│   │   - _delete_reminder()
│
├── middleware/
│   └── InputValidator.py
│       - validate_user_input()
│       - validate_expense_input()
│       - validate_budget_input()
│       - validate_reminder_input()
│       - validateJWT(token: string): Promise
│       - implementRateLimiting(userId: string): boolean
│
├── utils/
│   └── JWTUtils.py
│       - checkJWTExpiration(token: string): boolean
│
└── tests/
    ├── TestAuth.py
    │   - test_register_user()
    │   - test_login_user()
    │   - test_logout_user()
    │   - test_authenticate_user()
    │   - test_generate_jwt()
    │   - test_refresh_jwt()
    ├── TestUser.py
    │   - test_get_user_profile()
    │   - test_update_user_profile()
    │   - test_delete_user()
    │   - test_track_login_attempts()
    ├── TestExpense.py
    │   - test_add_expense()
    │   - test_get_expenses()
    │   - test_update_expense()
    │   - test_delete_expense()
    ├── TestBudget.py
    │   - test_set_budget()
    │   - test_get_budget_summary()
    │   - test_update_budget()
    │   - test_delete_budget()
    ├── TestReminder.py
    │   - test_set_reminder()
    │   - test_get_reminders()
    │   - test_delete_reminder()
    ├── TestIntegration.py
    ├── TestUI.py
    └── TestJWT.py
        - test_validate_jwt()
        - test_check_jwt_expiration()
        - test_implement_rate_limiting()

frontend/
├── public
│   ├── index.html
│   ├── favicon.ico
│   └── assets
│       ├── images
│       │   └── logo.png
│       └── styles
│           └── global.css
│
├── src
│   ├── index.js
│   ├── App.js
│   ├── components
│   │   ├── Header.js
│   │   ├── Footer.js
│   │   ├── AuthForm.js
│   │   │   ├── LoginForm
│   │   │   └── RegisterForm
│   │   ├── UserProfile.js
│   │   ├── ExpenseTracker.js
│   │   │   ├── AddExpense
│   │   │   ├── ExpenseList
│   │   │   └── ExpenseChart
│   │   ├── BudgetManager.js
│   │   │   ├── SetBudget
│   │   │   ├── BudgetSummary
│   │   │   └── BudgetChart
│   │   └── ReminderManager.js
│   │       ├── AddReminder
│   │       └── ReminderList
│   ├── services
│   │   ├── auth.service.js
│   │   ├── user.service.js
│   │   ├── expense.service.js
│   │   ├── budget.service.js
│   │   └── reminder.service.js
│   ├── utils
│   │   ├── api.js
│   │   ├── auth.js
│   │   └── formatters.js
│   │       - checkJWTExpiration(token: string): boolean
│   ├── styles
│   │   ├── index.css
│   │   ├── app.css
│   │   ├── header.css
│   │   ├── footer.css
│   │   ├── auth.css
│   │   ├── profile.css
│   │   ├── expenses.css
│   │   ├── budget.css
│   │   └── reminders.css
│   └── assets
│       ├── images
│       │   └── logo.png
│       └── icons
│           ├── home.svg
│           ├── profile.svg
│           ├── expenses.svg
│           ├── budget.svg
│           └── reminders.svg

theme/
├── landingPage
│   ├── index.html
│   ├── styles.css
│   └── assets
│       └── images
│           └── landing-page-image.jpg
│
└── comingSoonPage
    ├── index.html
    ├── styles.css
    └── assets
        └── images
            └── coming-soon-image.jpg
