// Mock data for demonstration purposes
const expenses = [
    { id: 1, name: 'Groceries', amount: 50, category: 'Food' },
    { id: 2, name: 'Rent', amount: 1000, category: 'Housing' },
    { id: 3, name: 'Electricity Bill', amount: 80, category: 'Utilities' },
];

const budgets = [
    { id: 1, name: 'Monthly Budget', amount: 2000 },
    { id: 2, name: 'Savings Budget', amount: 500 },
];

const reminders = [
    { id: 1, name: 'Pay Rent', dueDate: '2023-06-01' },
    { id: 2, name: 'Pay Electricity Bill', dueDate: '2023-06-15' },
];

// Add event listeners and functionality for user interactions
const addExpenseBtn = document.querySelector('.add-expense-btn');
const expenseList = document.querySelector('.expense-list');
const budgetList = document.querySelector('.budget-list');
const reminderList = document.querySelector('.reminder-list');
const addBudgetBtn = document.querySelector('.add-budget-btn');
const addReminderBtn = document.querySelector('.add-reminder-btn');

addExpenseBtn.addEventListener('click', () => {
    const newExpense = {
        id: expenses.length + 1,
        name: prompt('Enter expense name:'),
        amount: parseFloat(prompt('Enter expense amount:')),
        category: prompt('Enter expense category:'),
    };

    expenses.push(newExpense);
    renderExpenses();
});

const renderExpenses = () => {
    expenseList.innerHTML = '';
    expenses.forEach((expense) => {
        const expenseItem = document.createElement('div');
        expenseItem.classList.add('expense-item');
        expenseItem.innerHTML = `
            <h3>${expense.name}</h3>
            <p>Amount: $${expense.amount.toFixed(2)}</p>
            <p>Category: ${expense.category}</p>
            <button class="edit-btn">Edit</button>
            <button class="delete-btn">Delete</button>
        `;

        const editBtn = expenseItem.querySelector('.edit-btn');
        const deleteBtn = expenseItem.querySelector('.delete-btn');

        editBtn.addEventListener('click', () => {
            const editForm = document.createElement('div');
            editForm.classList.add('edit-form');
            editForm.innerHTML = `
                <input type="text" placeholder="Name" value="${expense.name}">
                <input type="number" placeholder="Amount" value="${expense.amount}">
                <select>
                    <option value="Food" ${expense.category === 'Food' ? 'selected' : ''}>Food</option>
                    <option value="Housing" ${expense.category === 'Housing' ? 'selected' : ''}>Housing</option>
                    <option value="Utilities" ${expense.category === 'Utilities' ? 'selected' : ''}>Utilities</option>
                </select>
                <button class="save-btn">Save</button>
                <button class="cancel-btn">Cancel</button>
            `;

            expenseItem.appendChild(editForm);

            const saveBtn = editForm.querySelector('.save-btn');
            const cancelBtn = editForm.querySelector('.cancel-btn');

            saveBtn.addEventListener('click', () => {
                const nameInput = editForm.querySelector('input[placeholder="Name"]');
                const amountInput = editForm.querySelector('input[placeholder="Amount"]');
                const categorySelect = editForm.querySelector('select');

                expense.name = nameInput.value;
                expense.amount = parseFloat(amountInput.value);
                expense.category = categorySelect.value;

                expenseItem.removeChild(editForm);
                renderExpenses();
            });

            cancelBtn.addEventListener('click', () => {
                expenseItem.removeChild(editForm);
            });
        });

        deleteBtn.addEventListener('click', () => {
            const confirmed = confirm(`Are you sure you want to delete "${expense.name}"?`);
            if (confirmed) {
                expenses.splice(expenses.indexOf(expense), 1);
                renderExpenses();
            }
        });

        expenseList.appendChild(expenseItem);
    });
};

const renderBudgets = () => {
    budgetList.innerHTML = '';
    budgets.forEach((budget) => {
        const budgetItem = document.createElement('div');
        budgetItem.classList.add('budget-item');
        budgetItem.innerHTML = `
            <h3>${budget.name}</h3>
            <p>Amount: $${budget.amount.toFixed(2)}</p>
            <button class="edit-btn">Edit</button>
            <button class="delete-btn">Delete</button>
        `;

        const editBtn = budgetItem.querySelector('.edit-btn');
        const deleteBtn = budgetItem.querySelector('.delete-btn');

        editBtn.addEventListener('click', () => {
            const newName = prompt('Enter new budget name:', budget.name);
            const newAmount = parseFloat(prompt('Enter new budget amount:', budget.amount));

            if (newName) budget.name = newName;
            if (!isNaN(newAmount)) budget.amount = newAmount;

            renderBudgets();
        });

        deleteBtn.addEventListener('click', () => {
            const confirmed = confirm(`Are you sure you want to delete "${budget.name}"?`);
            if (confirmed) {
                budgets.splice(budgets.indexOf(budget), 1);
                renderBudgets();
            }
        });

        budgetList.appendChild(budgetItem);
    });
};

const renderReminders = () => {
    reminderList.innerHTML = '';
    reminders.forEach((reminder) => {
        const reminderItem = document.createElement('div');
        reminderItem.classList.add('reminder-item');
        reminderItem.innerHTML = `
            <h3>${reminder.name}</h3>
            <p>Due Date: ${reminder.dueDate}</p>
            <button class="edit-btn">Edit</button>
            <button class="delete-btn">Delete</button>
        `;

        const editBtn = reminderItem.querySelector('.edit-btn');
        const deleteBtn = reminderItem.querySelector('.delete-btn');

        editBtn.addEventListener('click', () => {
            const newName = prompt('Enter new reminder name:', reminder.name);
            const newDueDate = prompt('Enter new due date:', reminder.dueDate);

            if (newName) reminder.name = newName;
            if (newDueDate) reminder.dueDate = newDueDate;

            renderReminders();
        });

        deleteBtn.addEventListener('click', () => {
            const confirmed = confirm(`Are you sure you want to delete "${reminder.name}"?`);
            if (confirmed) {
                reminders.splice(reminders.indexOf(reminder), 1);
                renderReminders();
            }
        });

        reminderList.appendChild(reminderItem);
    });
};

addBudgetBtn.addEventListener('click', () => {
    const newBudget = {
        id: budgets.length + 1,
        name: prompt('Enter budget name:'),
        amount: parseFloat(prompt('Enter budget amount:')),
    };

    budgets.push(newBudget);
    renderBudgets();
});

addReminderBtn.addEventListener('click', () => {
    const newReminder = {
        id: reminders.length + 1,
        name: prompt('Enter reminder name:'),
        dueDate: prompt('Enter due date:'),
    };

    reminders.push(newReminder);
    renderReminders();
});

renderExpenses();
renderBudgets();
renderReminders();