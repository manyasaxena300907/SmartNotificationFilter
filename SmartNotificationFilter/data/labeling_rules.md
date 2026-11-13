# Labeling rules (write once, follow always)

## Label 1 - Important
- Exams, tests, viva, practicals: dates, timings, venue changes
- Fee payment, scholarship, forms, registration deadlines
- Assignment or project submission deadlines
- Timetable changes, class cancelled or rescheduled
- Results, admit card, attendance warnings
- Placement or internship notices with deadlines

## Label 0 - Not important
- Greetings, thanks, congratulations
- Jokes, memes, forwards, casual chat
- Opinions and general chit-chat
- Promotions or social messages with no action needed

## Tricky cases (about 15-20 in the dataset)
- Academic word but not important: "Exam stress is killing me, let's get chai" -> 0
- Important with no obvious keyword: "Be at the seminar hall by 8, doors close sharply" -> 1
- Deadline-like word but not important: "Last date to vote for best meme" -> 0

## Privacy
Remove all names, phone numbers, and timestamps from messages.
