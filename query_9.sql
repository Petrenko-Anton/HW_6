SELECT students.fullname, subjects.name
FROM subjects
JOIN grades ON subjects.id = grades.subject_id
JOIN students ON grades.student_id = students.id
WHERE students.id = ?
group by subjects.name





