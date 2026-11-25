# EECE2140 Final Project: Course Registration System

Menu-driven Python app for registering students in courses.

## Part 1: Alyssa (Courses & Students)

**Task 1: Display courses**
- [x] Course data: ID, name, credits, instructor, capacity, enrolled, meeting day/time, prereqs
- [x] Remaining seats = capacity - enrolled
- [x] Show courses as a table and mark the full ones

**Task 2: Students**
- [ ] Student data: name, ID, year, completed courses, registered courses, total credits
- [ ] Look up a student by ID and confirm they exist

**Task 3: Search & filter**
- [ ] Search by ID or name (partial match, ignore case)
- [ ] Filter: open seats, credits, meeting day

## Part 2: Dennis (Registration Rules)

**Task 4: Register**
- [ ] Reject if the course doesn't exist
- [ ] Reject if already registered or completed
- [ ] Reject if the course is full
- [ ] Reject if total credits > 13 (exactly 13 is allowed)
- [ ] Reject if prereqs are missing (Task 5)
- [ ] Reject on a time conflict (Task 6)
- [ ] Print the reason for each rejection
- [ ] On success, update the student (courses, credits) and the course (enrolled, seats)
- [ ] Match IDs ignoring case and spaces

**Task 5: Prereqs**
- [ ] Check that every prereq is completed (some courses have more than one)

**Task 6: Time conflicts**
- [ ] Store each schedule as `{"day", "start", "end"}`
- [ ] Convert times to minutes (don't compare strings)
- [ ] Conflict only if same day and `startA < endB and startB < endA`

**Task 7: Drop**
- [ ] Error if the student isn't registered for the course
- [ ] Remove the course, subtract its credits, free the seat
- [ ] Don't add it to completed courses
- [ ] Print a confirmation
