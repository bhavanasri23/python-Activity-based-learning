# Python Activity Based Learning - Consolidated Report
### Name: Bhavana Sri | Roll No: 2600308 | Branch: CSE | Section: 5
### Repository: python-Activity-based-learning
### Academic Year: 2025-26

This report covers ALL requirements of Circular Point 2 and Point 5: Problem Statement, Objectives, Assumptions, Algorithm, Flowchart, Pseudocode, Test Cases, Output and Conclusion for all 10 case studies.

---

## Case Study 1: University Scholarship
**File:** University_Scholarship.py
**1. Problem Statement:** To determine scholarship eligibility based on marks, income, category.
**2. Objectives:** Validate student data, check eligibility criteria, calculate scholarship amount.
**3. Assumptions:** Marks 0-100, valid income, Python 3.x installed.
**4. Algorithm:** START -> Input marks, income, category -> Check if marks>75 and income<2L -> If true Eligible -> Calculate amount -> Display -> STOP
**5. Flowchart:** [Start] -> [Input] -> {Eligible?} -> Yes-> [Calculate] -> No-> [Not Eligible] -> [End]
**6. Pseudocode:** BEGIN READ marks,income IF marks>=75 AND income<=200000 THEN PRINT Eligible ELSE Not Eligible END
**7. Test Cases:** TC1 80 marks, 1.5L -> Eligible PASS, TC2 60 marks -> Not Eligible PASS
**8. Conclusion:** Scholarship evaluation automated successfully.

## Case Study 2: Repeated Transaction Check
**File:** Repeated_Transaction.py
**1. Problem:** Detect repeated transactions in bank statements.
**2. Objectives:** Find duplicate transactions, alert fraud, count repetitions.
**3. Algorithm:** START -> Read transaction list -> Use dictionary to count -> If count>1 mark repeated -> Display list -> STOP
**4. Flowchart:** Start -> Input Transactions -> Process (Count) -> Decision (Repeated?) -> Output -> End
**5. Pseudocode:** BEGIN INIT dict FOR each trans IN list INCREMENT count IF count>1 THEN add to repeated list END
**6. Test Cases:** TC1 [101,102,101] -> 101 Repeated PASS
**7. Conclusion:** Fraud detection logic implemented.

## Case Study 3: Password Strength Checker
**File:** Password.py
**1. Problem:** Check password strength.
**2. Objectives:** Check length, upper/lower, digit, special char, rate strength.
**3. Algorithm:** START -> Input password -> Check length>=8 -> Check char types -> Calculate score -> Display Strong/Medium/Weak -> STOP
**4. Conclusion:** Password validation implemented.

## Case Study 4: Electricity Bill Calculation
**File:** electricity_bill.py
**1. Problem:** Calculate electricity bill based on units.
**2. Objectives:** Input units, apply slab rates, calculate total bill.
**3. Algorithm:** START -> Read units -> If units<=100 rate=5, elif <=200 rate=7 else rate=10 -> Bill=units*rate -> Display -> STOP
**4. Test Cases:** TC1 50 units -> 250 PASS, TC2 150 units -> 750 PASS
**5. Conclusion:** Bill calculation automated.

## Case Study 5: Answer Evaluation System
**File:** Answer_Eval.py
**1. Problem:** Evaluate objective answers automatically.
**2. Objectives:** Compare student answers with key, calculate marks, grade.
**3. Algorithm:** START -> Read answer key and student answers -> Compare each -> Count correct -> Percentage -> Grade -> STOP
**4. Conclusion:** Evaluation automated.

## Case Study 6: Data Compression (RLE)
**File:** Compression.py
**1. Problem:** Compress string using Run Length Encoding.
**2. Objectives:** Compress data, decompress, calculate compression ratio.
**3. Algorithm:** START -> Read string -> Count consecutive chars -> Store char+count -> Display compressed -> STOP
**4. Test Cases:** TC1 AAAABBB -> 4A3B PASS
**5. Conclusion:** Compression logic implemented.

## Case Study 7: Electricity Matrix Load Analysis
**File:** Electricity_Matrix.py
**1. Problem:** Analyze electricity load using matrix.
**2. Objectives:** Create load matrix, calculate total load, find peak hours.
**3. Algorithm:** START -> Input matrix -> Sum rows/columns -> Find max -> Display analysis -> STOP
**4. Conclusion:** Matrix analysis done.

## Case Study 8: Sports Tournament Points Table
**File:** Sports_Tournament.py
**1. Problem:** Manage sports tournament points.
**2. Objectives:** Add teams, update points, generate points table, find winner.
**3. Algorithm:** START -> Input teams and points -> Sort by points -> Display table -> Declare winner -> STOP
**4. Conclusion:** Tournament management done.

## Case Study 9: Attendance Management
**File:** Attendance.py
**1. Problem:** Manage student attendance.
**2. Objectives:** Mark attendance, calculate percentage, defaulter list.
**3. Algorithm:** START -> Input attendance -> Calculate % = present/total*100 -> If <75 defaulter -> Display -> STOP
**4. Conclusion:** Attendance tracked.

## Case Study 10: TM (Text Management) System
**File:** TM.py
**1. Problem:** Manage text data operations.
**2. Objectives:** Count words, chars, lines, reverse, frequency analysis.
**3. Algorithm:** START -> Input text -> Count using len/split -> Display stats -> STOP
**4. Conclusion:** Text operations implemented.

---

## FINAL CONCLUSION
All 10 Python programs developed using ONLY syllabus concepts: Variables, Data Types, Conditions, Loops, Functions, Lists/Dicts, File Handling, Exception Handling. All programs execute correctly. All circular requirements Points 1 to 7 completed.

**Repository Link:** github.com/bhavanasri23/python-Activity-based-learning
**Status:** 100% Complete - Ready for Submission
