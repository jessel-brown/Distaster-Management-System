CREATE DATABASE DISASTER_MANAGEMENT_SYSTEM;
-- DROP DATABASE DISASTER_MANAGEMENT_SYSTEM;
USE DISASTER_MANAGEMENT_SYSTEM;
CREATE TABLE ACCOUNTS(AccountID int, FirstName varchar(50), LastName varchar(50), EmailAddress varchar(50), Password varchar(50), Role varchar(10), UserName  varchar(50), Zipcode int, PRIMARY KEY( AccountID));
ALTER TABLE DISASTER_MANAGEMENT_SYSTEM.ACCOUNTS ADD CONSTRAINT CK_Table_Role
    CHECK (Role IN ('Admin', 'Responder', 'RequestCenter'));

INSERT INTO ACCOUNTS(AccountID, FirstName, LastName, EmailAddress, Password, Role, UserName, Zipcode) VALUES(1, 'Jane', 'Doe', 'jane.doe@gmail.com', 'Password1', 'Responder', 'jdoe1', 52241);

-- CREATE TABLE REQUESTS(RequestorID int, Requestor varchar(50), ItemID int, ItemTitle varchar(50), ExpireDate date, RequestOn date, Quantity int, Category varchar(50));
-- ALTER TABLE DISASTER_MANAGEMENT_SYSTEM.REQUESTS ADD CONSTRAINT CK_Category
--     CHECK (Category IN ('Food', 'Volunteer', 'Supplies'));
--     
-- CREATE TABLE DONATIONS(DonatorID int, Donator varchar(50), ItemID int, DonationTitle varchar(50), ExpireDate date, Quantity int, Category varchar(50));
-- ALTER TABLE DISASTER_MANAGEMENT_SYSTEM.DONATIONS ADD CONSTRAINT CK_Category
--     CHECK (Category IN ('Food', 'Volunteer', 'Supplies'));

CREATE TABLE TRANSACTIONS(RequestorID int, DonatorID int, ItemID int, Quantity int, Category varchar(50), ExpireDate date, RequestOn date, RequestFufilled date, TransactionTYPE char);
ALTER TABLE DISASTER_MANAGEMENT_SYSTEM.TRANSACTIONS ADD CONSTRAINT CK_Category
    CHECK (Category IN ('Food', 'Volunteer', 'Supplies'));
    
CREATE TABLE DISASTERS(DisasterID int, Title varchar(50), ZipCode int, Location varchar(50), StartDate date, PRIMARY KEY( DisasterID));

SELECT FirstName, LastName FROM ACCOUNTS;

CREATE TABLE ITEMS(ItemID int, Title char, Category char, PRIMARY KEY(ItemID));
ALTER TABLE DISASTER_MANAGEMENT_SYSTEM.ITEMS ADD CONSTRAINT CK_Category
    CHECK (Category IN ('Food', 'Volunteer', 'Supplies'));