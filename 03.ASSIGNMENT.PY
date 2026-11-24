# Assignment Management System

assignment = ['python', 'java', 'c++', 'javascript', 'html', 'css']
print('Assignment:', assignment)

new_assignment = input('Enter new assignment: ')
assignment.append(new_assignment)
print('Updated Assignment:', assignment)

completed_assignment = input('Enter completed assignment: ')
assignment.remove(completed_assignment)
print('Updated Assignment:', assignment)