-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: library
-- ------------------------------------------------------
-- Server version	8.0.33

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `tbl_addaccount`
--

DROP TABLE IF EXISTS `tbl_addaccount`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_addaccount` (
  `name` varchar(255) DEFAULT NULL,
  `accountID` varchar(255) DEFAULT NULL,
  `phone` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `isAvail` tinyint(1) DEFAULT '1',
  `limit` int NOT NULL DEFAULT '5',
  KEY `accountID` (`accountID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_addaccount`
--

LOCK TABLES `tbl_addaccount` WRITE;
/*!40000 ALTER TABLE `tbl_addaccount` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_addaccount` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_addbook`
--

DROP TABLE IF EXISTS `tbl_addbook`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_addbook` (
  `title` varchar(255) DEFAULT NULL,
  `bookid` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `author` varchar(255) DEFAULT NULL,
  `publisher` varchar(255) DEFAULT NULL,
  `isAvail` tinyint(1) unsigned zerofill DEFAULT '1',
  KEY `bookid` (`bookid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_addbook`
--

LOCK TABLES `tbl_addbook` WRITE;
/*!40000 ALTER TABLE `tbl_addbook` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_addbook` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_issue`
--

DROP TABLE IF EXISTS `tbl_issue`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_issue` (
  `book_id` varchar(255) NOT NULL,
  `account_id` varchar(255) NOT NULL,
  `issueTime` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `renewCount` int DEFAULT '0',
  KEY `bookID` (`book_id`),
  KEY `accountID` (`account_id`),
  CONSTRAINT `accountID` FOREIGN KEY (`account_id`) REFERENCES `tbl_addaccount` (`accountID`),
  CONSTRAINT `bookID` FOREIGN KEY (`book_id`) REFERENCES `tbl_addbook` (`bookid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_issue`
--

LOCK TABLES `tbl_issue` WRITE;
/*!40000 ALTER TABLE `tbl_issue` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_issue` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-08-28 22:39:53
