CREATE DATABASE student_tracker;
USE student_tracker;

CREATE TABLE students (
    roll_no INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE marks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    roll_no INT,
    subject VARCHAR(50),
    marks INT,
    FOREIGN KEY (roll_no) REFERENCES students(roll_no) ON DELETE CASCADE
);
select * from students;
SELECT students.name
FROM students
JOIN marks ON students.roll_no = marks.roll_no
WHERE marks.marks > 8 AND marks.subject = 'maths';
