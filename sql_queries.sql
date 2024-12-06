-- Update queries
UPDATE Admissions 
SET attending_doctor_id = 29 
WHERE attending_doctor_id = 3;

UPDATE Admissions 
SET patient_id = 4 
WHERE patient_id = 35;

-- Query 1: Select Doctors who have Admissions
SELECT DISTINCT d.* 
FROM Doctors d
JOIN Admissions a ON d.doctor_id = a.attending_doctor_id;

-- Query 2: Select Doctors who do not have Admissions
SELECT * 
FROM Doctors 
WHERE doctor_id NOT IN (SELECT attending_doctor_id FROM Admissions);

-- Query 3: Select Patients whose Admission can't be completed due to missing doctor details
SELECT * 
FROM Patients 
WHERE patient_id IN (
    SELECT patient_id 
    FROM Admissions 
    WHERE attending_doctor_id IS NULL
);