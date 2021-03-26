import unittest

from ..project.student import Student


class StudentTests(unittest.TestCase):
    def setUp(self) -> None:
        self.student = Student('Pesho')

    def test_init__when_courses_none__expect_empty(self) -> None:
        self.assertEqual(self.student.name, 'Pesho')
        self.assertEqual(self.student.courses, {})

    def test_init__when_courses_not_none__expect_valid_attributes(self) -> None:
        student = Student('Pesho', {"math": ['algebra', 'geometry']})
        self.assertEqual(student.name, 'Pesho')
        self.assertEqual(student.courses, {"math": ['algebra', 'geometry']})

    def test_enroll__when_add_course_notes_no__expect_course_added(self) -> None:
        self.assertEqual(self.student.enroll('math', ['algebra', 'geometry'], 'no'), 'Course has been added.')
        self.assertEqual(self.student.courses, {'math': []})

    def test_enroll__when_add_course_notes_yes__expect_notes_added_1(self) -> None:
        self.assertEqual(self.student.enroll('math', ['algebra', 'geometry'], ''),
                         'Course and course notes have been added.')
        self.assertEqual(self.student.courses, {'math': ['algebra', 'geometry']})

    def test_enroll__when_add_course_notes_yes__expect_notes_added_2(self) -> None:
        self.assertEqual(self.student.enroll('math', ['algebra', 'geometry'], 'Y'),
                         'Course and course notes have been added.')
        self.assertEqual(self.student.courses, {'math': ['algebra', 'geometry']})

    def test_enroll__when_course_already_in_courses__expect_notes_updated(self) -> None:
        self.student.courses = {"math": ['algebra']}
        self.assertEqual(self.student.enroll('math', ['geometry'], ''),
                         "Course already added. Notes have been updated.")
        self.assertEqual(self.student.courses, {'math': ['algebra', 'geometry']})

    def test_add_notes__when_course_not_in_courses__expect_exception(self) -> None:
        with self.assertRaises(Exception) as context:
            self.student.add_notes('math', ['algebra', 'geometry'])
        self.assertEqual(context.exception.args[0], "Cannot add notes. Course not found.")

    def test_add_notes__when_course_in_courses__expect_notes_updated(self) -> None:
        self.student.courses = {'math': []}
        self.assertEqual(self.student.add_notes('math', 'geometry'), "Notes have been updated")
        self.assertEqual(self.student.courses, {'math': ['geometry']})

    def test_leave_course__when_course_not_in_courses__expect_exception(self) -> None:
        with self.assertRaises(Exception) as context:
            self.student.leave_course('math')
        self.assertEqual(context.exception.args[0], 'Cannot remove course. Course not found.')

    def test_leave_course__when_course_in_courses__expect_course_removed(self) -> None:
        self.student.enroll('math', ['algebra', 'geometry'], '')
        self.assertEqual(self.student.leave_course('math'), 'Course has been removed')
        self.assertEqual(self.student.courses, {})


if __name__ == '__main__':
    unittest.main()
