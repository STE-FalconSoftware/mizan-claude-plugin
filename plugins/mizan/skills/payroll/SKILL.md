---
name: payroll
description: Payroll and HR in Mizan — employees, leave (congés), attendance (présence), the monthly payroll preview and run, CNSS and IRPP parameters. Use when the user asks about salaries, payslips (bulletins de paie), leave balances or attendance.
---

# Payroll and HR (paie, congés, présence)

## Monthly payroll
1. `payroll_params` to read the rates in force (CNSS, the IRPP barème, the divisor, maintien de salaire).
2. `attendance_summary` and `list_leave` for the month. Unpaid leave (sans solde) and sick leave
   without maintien reduce the salary.
3. `payroll_preview`, shown as a table per employee: brut, CNSS salariale, IRPP, net.
4. Once the user confirms, `run_payroll`. `list_payroll_runs` shows past runs.
5. `accounting_controls` once the payroll entries are posted.
Payslips are downloaded as PDF from the app.

## Employees
`create_employee` and `update_employee` (dry-run, then confirm). Bank details (RIB) are changed by a
human in the app.

## Leave and attendance
- Balance: `find_employee` → `leave_balance`.
- Book leave: `request_leave` → `set_leave_status(approved)`, each confirmed.
- Attendance: `record_attendance` over a range of days. Weekends and `list_public_holidays` are
  handled for you.

Salary data is personal: show only what the user asked for.
