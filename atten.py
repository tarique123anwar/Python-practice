class AttendanceSystem:
    def __init__(self):
        self.attendance_records = {}

    def mark_attendance(self, student_name, status="Present"):
        """
        Mark attendance for a student.

        Parameters:
        - student_name (str): Name of the student
        - status (str): Attendance status, default is "Present"
        """
        if student_name in self.attendance_records:
            self.attendance_records[student_name].append(status)
        else:
            self.attendance_records[student_name] = [status]

    def view_attendance(self, student_name=None):
        """
        View attendance for all students or a specific student.

        Parameters:
        - student_name (str): Name of the student to view attendance for, default is None (view all)

        Returns:
        - list or dict: Attendance records for all students or a specific student
        """
        if student_name:
            return {student_name: self.attendance_records.get(student_name, [])}
        else:
            return self.attendance_records

# Example Usage:
attendance_system = AttendanceSystem()

# Mark attendance for students
attendance_system.mark_attendance("John")
attendance_system.mark_attendance("Alice")
attendance_system.mark_attendance("Bob")
attendance_system.mark_attendance("John", "Absent")
attendance_system.mark_attendance("Alice", "Late")

# View attendance for all students
print("All Students Attendance:")
print(attendance_system.view_attendance())

# View attendance for a specific student
student_name_to_view = "Alice"
print(f"\nAttendance for {student_name_to_view}:")
print(attendance_system.view_attendance(student_name_to_view))
