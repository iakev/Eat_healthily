-- MySQL dump 10.13  Distrib 8.0.33, for Linux (x86_64)
--
-- Host: localhost    Database: ehdevdb
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
-- Current Database: `ehdevdb`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `ehdevdb` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `ehdevdb`;

--
-- Table structure for table `consumers`
--

DROP TABLE IF EXISTS `consumers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `consumers` (
  `id` varchar(64) NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `consumers_ibfk_1` FOREIGN KEY (`id`) REFERENCES `users` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `consumers`
--

LOCK TABLES `consumers` WRITE;
/*!40000 ALTER TABLE `consumers` DISABLE KEYS */;
INSERT INTO `consumers` VALUES ('69c4e892-274e-4a08-a595-47ad8c45fc08'),('829a6712-e294-484e-b795-f005fb2016ad'),('88ec9bb6-0721-4a99-a06b-5ace2a963d35'),('cf2db828-a610-427a-ba9f-05c2e0837fbd');
/*!40000 ALTER TABLE `consumers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `farm_operation`
--

DROP TABLE IF EXISTS `farm_operation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `farm_operation` (
  `farm_id` varchar(64) NOT NULL,
  `operation_id` varchar(64) NOT NULL,
  `operation_date` datetime DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `id` varchar(64) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `farm_id` (`farm_id`),
  KEY `operation_id` (`operation_id`),
  CONSTRAINT `farm_operation_ibfk_1` FOREIGN KEY (`farm_id`) REFERENCES `farms` (`id`) ON DELETE CASCADE,
  CONSTRAINT `farm_operation_ibfk_2` FOREIGN KEY (`operation_id`) REFERENCES `operations` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `farm_operation`
--

LOCK TABLES `farm_operation` WRITE;
/*!40000 ALTER TABLE `farm_operation` DISABLE KEYS */;
/*!40000 ALTER TABLE `farm_operation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `farm_operation_input`
--

DROP TABLE IF EXISTS `farm_operation_input`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `farm_operation_input` (
  `farm_operation_id` varchar(64) DEFAULT NULL,
  `input_id` varchar(64) DEFAULT NULL,
  KEY `farm_operation_id` (`farm_operation_id`),
  KEY `input_id` (`input_id`),
  CONSTRAINT `farm_operation_input_ibfk_1` FOREIGN KEY (`farm_operation_id`) REFERENCES `farm_operation` (`id`) ON DELETE CASCADE,
  CONSTRAINT `farm_operation_input_ibfk_2` FOREIGN KEY (`input_id`) REFERENCES `inputs` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `farm_operation_input`
--

LOCK TABLES `farm_operation_input` WRITE;
/*!40000 ALTER TABLE `farm_operation_input` DISABLE KEYS */;
/*!40000 ALTER TABLE `farm_operation_input` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `farm_produce`
--

DROP TABLE IF EXISTS `farm_produce`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `farm_produce` (
  `farm_id` varchar(64) NOT NULL,
  `produce_id` varchar(64) NOT NULL,
  `planting_date` datetime NOT NULL,
  `image_file` varchar(128) DEFAULT NULL,
  `harvest_date` datetime DEFAULT NULL,
  `id` varchar(64) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `farm_id` (`farm_id`),
  KEY `produce_id` (`produce_id`),
  CONSTRAINT `farm_produce_ibfk_1` FOREIGN KEY (`farm_id`) REFERENCES `farms` (`id`) ON DELETE CASCADE,
  CONSTRAINT `farm_produce_ibfk_2` FOREIGN KEY (`produce_id`) REFERENCES `products` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `farm_produce`
--

LOCK TABLES `farm_produce` WRITE;
/*!40000 ALTER TABLE `farm_produce` DISABLE KEYS */;
INSERT INTO `farm_produce` VALUES ('591fa805-6d60-49af-b73f-66233a5572eb','00e72ee6-6a4b-40aa-a71d-0522523648ca','2021-02-15 00:00:00','/uploads/SUCCESS-STORY-OF-KAKUZI-LTD-FARMING-OVER-1000-ACRES-OF-HASS-AVOCADOS.jpg','2021-09-29 00:00:00','19894299-d3e0-43b0-9981-62b79f423b44','2023-04-05 09:26:45','2023-04-05 09:26:45'),('4bd4a4c1-955f-4c31-94cc-a0a770448831','95195db8-8eb3-4077-9748-ff7e594b6bca','2021-08-02 00:00:00','/uploads/apple_farm.jpeg','2021-11-09 00:00:00','f37767f0-41eb-4c4f-8824-e3041b913e81','2023-04-05 10:11:07','2023-04-05 10:11:07');
/*!40000 ALTER TABLE `farm_produce` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `farm_produce_operation`
--

DROP TABLE IF EXISTS `farm_produce_operation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `farm_produce_operation` (
  `farm_produce_id` varchar(64) NOT NULL,
  `operation_id` varchar(64) NOT NULL,
  `operation_date` datetime DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `id` varchar(64) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `farm_produce_id` (`farm_produce_id`),
  KEY `operation_id` (`operation_id`),
  CONSTRAINT `farm_produce_operation_ibfk_1` FOREIGN KEY (`farm_produce_id`) REFERENCES `farm_produce` (`id`) ON DELETE CASCADE,
  CONSTRAINT `farm_produce_operation_ibfk_2` FOREIGN KEY (`operation_id`) REFERENCES `operations` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `farm_produce_operation`
--

LOCK TABLES `farm_produce_operation` WRITE;
/*!40000 ALTER TABLE `farm_produce_operation` DISABLE KEYS */;
INSERT INTO `farm_produce_operation` VALUES ('f37767f0-41eb-4c4f-8824-e3041b913e81','5e1ee09b-c077-4d91-a0ce-21769882b9aa','2021-11-02 00:00:00','Getting rid of fruit flies that affects the produced apples making them rot from the inside.','01088224-db8f-4fe8-9d0f-1e4151aa707e','2023-04-05 10:34:41','2023-04-05 10:34:41'),('19894299-d3e0-43b0-9981-62b79f423b44','6539ab1f-17af-4766-823c-e7e414115fef','2021-07-16 00:00:00','More manure to increase yield of produce.','1cb1104e-5b31-424c-b2e6-bee28382316b','2023-04-05 09:52:56','2023-04-05 09:52:56'),('f37767f0-41eb-4c4f-8824-e3041b913e81','b236859c-070c-45ef-828d-1c02fa0c171f','2021-09-20 00:00:00','Weeding to remove overgrown weeds interfering with apple growth.','1d9cd676-efae-4c22-a736-313e0807e8aa','2023-04-05 10:33:16','2023-04-05 10:33:16'),('19894299-d3e0-43b0-9981-62b79f423b44','bb3d1b03-fae8-434d-b128-57ea07e8ae90','2021-09-29 00:00:00','Harvesting of Avacados.','3d69e73f-9760-4e62-ab9d-f5cce5508eed','2023-04-05 09:58:47','2023-04-05 09:58:47'),('f37767f0-41eb-4c4f-8824-e3041b913e81','6539ab1f-17af-4766-823c-e7e414115fef','2021-09-13 00:00:00','Applying Manure to increase yield','3def745d-9ce6-401b-b2a8-8080f5225bd6','2023-04-05 10:30:36','2023-04-05 10:30:36'),('19894299-d3e0-43b0-9981-62b79f423b44','6539ab1f-17af-4766-823c-e7e414115fef','2021-05-31 00:00:00','This is an organic operation since the avocados grown here are organically grown.','4cc8872e-554c-42d8-bb07-7c9c849258ae','2023-04-05 09:50:40','2023-04-05 09:50:40'),('19894299-d3e0-43b0-9981-62b79f423b44','b236859c-070c-45ef-828d-1c02fa0c171f','2021-03-03 00:00:00','Farm cleaning and manual removal of weeds from the farm undergrowth','5a07b4eb-6b2d-44b1-9231-0562f5b4f991','2023-04-05 09:47:31','2023-04-05 09:47:31'),('f37767f0-41eb-4c4f-8824-e3041b913e81','9c6e96c8-558e-4003-98f5-0bb9ee38349c','2021-08-02 00:00:00','Planting of seedlings from the nursery to the main orchard.','69d8184c-12c8-4625-9a1c-33e4c3d7bfe7','2023-04-05 10:17:12','2023-04-05 10:17:12'),('19894299-d3e0-43b0-9981-62b79f423b44','9c6e96c8-558e-4003-98f5-0bb9ee38349c','2021-02-15 00:00:00','Seedlings transplanted into farm ground from the nursery.','9d13a7d2-0d4f-41a3-9183-8aca7ab6dc3e','2023-04-05 09:45:36','2023-04-05 09:45:36'),('f37767f0-41eb-4c4f-8824-e3041b913e81','e2a8dada-5ca0-48dc-9e48-5fe12e7b77a9','2021-09-13 00:00:00','Applying fertilizers N.P.K to increase the yield.','bad18c33-53f6-4645-9aad-0b462a44b055','2023-04-05 10:32:03','2023-04-05 10:32:03'),('f37767f0-41eb-4c4f-8824-e3041b913e81','b236859c-070c-45ef-828d-1c02fa0c171f','2021-09-09 00:00:00','Removal of unwanted weeds from interfering with apple growth.','c29fdd74-25ba-4cb2-8a6d-bebc21ae1a13','2023-04-05 10:28:54','2023-04-05 10:28:54'),('19894299-d3e0-43b0-9981-62b79f423b44','b236859c-070c-45ef-828d-1c02fa0c171f','2021-06-07 00:00:00','More weeding to ensure proper growth and nutrification of produce.','c75c42db-e2fc-4f82-83b4-a9f709ea8742','2023-04-05 09:52:00','2023-04-05 09:52:00'),('f37767f0-41eb-4c4f-8824-e3041b913e81','bb3d1b03-fae8-434d-b128-57ea07e8ae90','2021-11-09 00:00:00','Harvesting apples for sale.','e3a00b39-8e2c-4c55-8667-d8d62ee9e433','2023-04-05 10:35:35','2023-04-05 10:35:35');
/*!40000 ALTER TABLE `farm_produce_operation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `farm_produce_operation_input`
--

DROP TABLE IF EXISTS `farm_produce_operation_input`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `farm_produce_operation_input` (
  `farm_produce_operation_id` varchar(64) DEFAULT NULL,
  `input_id` varchar(64) DEFAULT NULL,
  KEY `farm_produce_operation_id` (`farm_produce_operation_id`),
  KEY `input_id` (`input_id`),
  CONSTRAINT `farm_produce_operation_input_ibfk_1` FOREIGN KEY (`farm_produce_operation_id`) REFERENCES `farm_produce_operation` (`id`) ON DELETE CASCADE,
  CONSTRAINT `farm_produce_operation_input_ibfk_2` FOREIGN KEY (`input_id`) REFERENCES `inputs` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `farm_produce_operation_input`
--

LOCK TABLES `farm_produce_operation_input` WRITE;
/*!40000 ALTER TABLE `farm_produce_operation_input` DISABLE KEYS */;
INSERT INTO `farm_produce_operation_input` VALUES ('bad18c33-53f6-4645-9aad-0b462a44b055','f5f2ee9e-c162-47b1-9f60-6cfdf0953ca3'),('01088224-db8f-4fe8-9d0f-1e4151aa707e','4b60a527-2102-46bf-b0ed-09ee49306d84');
/*!40000 ALTER TABLE `farm_produce_operation_input` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `farmers`
--

DROP TABLE IF EXISTS `farmers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `farmers` (
  `id` varchar(64) NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `farmers_ibfk_1` FOREIGN KEY (`id`) REFERENCES `users` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `farmers`
--

LOCK TABLES `farmers` WRITE;
/*!40000 ALTER TABLE `farmers` DISABLE KEYS */;
INSERT INTO `farmers` VALUES ('e1b7d730-d010-41d6-b6dd-1ef6e85a8a22');
/*!40000 ALTER TABLE `farmers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `farmers_farm`
--

DROP TABLE IF EXISTS `farmers_farm`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `farmers_farm` (
  `farmer_id` varchar(64) DEFAULT NULL,
  `farms_id` varchar(64) DEFAULT NULL,
  KEY `farmer_id` (`farmer_id`),
  KEY `farms_id` (`farms_id`),
  CONSTRAINT `farmers_farm_ibfk_1` FOREIGN KEY (`farmer_id`) REFERENCES `farmers` (`id`) ON DELETE CASCADE,
  CONSTRAINT `farmers_farm_ibfk_2` FOREIGN KEY (`farms_id`) REFERENCES `farms` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `farmers_farm`
--

LOCK TABLES `farmers_farm` WRITE;
/*!40000 ALTER TABLE `farmers_farm` DISABLE KEYS */;
INSERT INTO `farmers_farm` VALUES ('e1b7d730-d010-41d6-b6dd-1ef6e85a8a22','591fa805-6d60-49af-b73f-66233a5572eb'),('e1b7d730-d010-41d6-b6dd-1ef6e85a8a22','4bd4a4c1-955f-4c31-94cc-a0a770448831');
/*!40000 ALTER TABLE `farmers_farm` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `farms`
--

DROP TABLE IF EXISTS `farms`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `farms` (
  `farm_name` varchar(128) NOT NULL,
  `address` varchar(128) NOT NULL,
  `image_file` varchar(128) DEFAULT NULL,
  `id` varchar(64) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `farm_name` (`farm_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `farms`
--

LOCK TABLES `farms` WRITE;
/*!40000 ALTER TABLE `farms` DISABLE KEYS */;
INSERT INTO `farms` VALUES ('Hollow Point Vineyard','1945-20100 Nakuru','','4bd4a4c1-955f-4c31-94cc-a0a770448831','2023-04-05 09:21:26','2023-04-05 09:21:26'),('Ravenwood Fields',' 619-60200 Meru','','591fa805-6d60-49af-b73f-66233a5572eb','2023-04-05 09:06:24','2023-04-05 09:06:24');
/*!40000 ALTER TABLE `farms` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inputs`
--

DROP TABLE IF EXISTS `inputs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inputs` (
  `input_name` varchar(128) NOT NULL,
  `manufactring_date` datetime DEFAULT NULL,
  `expiry_date` datetime DEFAULT NULL,
  `source` varchar(128) NOT NULL,
  `cautions` varchar(255) DEFAULT NULL,
  `pre_harvest_interval` varchar(128) DEFAULT NULL,
  `toxicity_level` enum('Highly toxic','Toxic','Moderately toxic','Slightly toxic','Virtually non-toxic') DEFAULT NULL,
  `ingredient` varchar(255) DEFAULT NULL,
  `image_file` varchar(128) DEFAULT NULL,
  `label_file` varchar(128) DEFAULT NULL,
  `user_manual_file_name` varchar(128) DEFAULT NULL,
  `id` varchar(64) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inputs`
--

LOCK TABLES `inputs` WRITE;
/*!40000 ALTER TABLE `inputs` DISABLE KEYS */;
INSERT INTO `inputs` VALUES ('Insect-killer','2021-02-04 00:00:00','2023-02-02 00:00:00','ASL Chemicals','','20','Toxic','Chlorpyrifos, pyrethrin, arsenic','/uploads/pesticides.jpeg','',NULL,'4b60a527-2102-46bf-b0ed-09ee49306d84','2023-04-05 10:26:17','2023-04-05 10:26:17'),('N.P.K','2018-06-06 00:00:00','2020-06-04 00:00:00','ASL Chemicals','','30','Moderately toxic','Nitrogen, Phosphorous and Potassium','/uploads/npk-fertilizers-500x500-2206723055.jpeg','',NULL,'f5f2ee9e-c162-47b1-9f60-6cfdf0953ca3','2023-04-05 10:19:42','2023-04-05 10:19:42');
/*!40000 ALTER TABLE `inputs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `operations`
--

DROP TABLE IF EXISTS `operations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `operations` (
  `operation_name` varchar(128) NOT NULL,
  `id` varchar(64) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `operations`
--

LOCK TABLES `operations` WRITE;
/*!40000 ALTER TABLE `operations` DISABLE KEYS */;
INSERT INTO `operations` VALUES ('Spraying Pesticides','5e1ee09b-c077-4d91-a0ce-21769882b9aa','2023-04-05 09:43:48','2023-04-05 09:43:48'),('Applying manure','6539ab1f-17af-4766-823c-e7e414115fef','2023-04-05 09:43:18','2023-04-05 09:43:18'),('Planting','9c6e96c8-558e-4003-98f5-0bb9ee38349c','2023-04-05 09:42:47','2023-04-05 09:42:47'),('Weeding','b236859c-070c-45ef-828d-1c02fa0c171f','2023-04-05 09:41:49','2023-04-05 09:41:49'),('Harvesting','bb3d1b03-fae8-434d-b128-57ea07e8ae90','2023-04-05 09:43:57','2023-04-05 09:43:57'),('Applying Fertilizers','e2a8dada-5ca0-48dc-9e48-5fe12e7b77a9','2023-04-05 09:43:09','2023-04-05 09:43:09');
/*!40000 ALTER TABLE `operations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products` (
  `produce_name` varchar(128) NOT NULL,
  `image_file` varchar(128) DEFAULT NULL,
  `id` varchar(64) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` VALUES ('Avacado','/uploads/ben-wicks-gwxcddjTbw4-unsplash.jpg','00e72ee6-6a4b-40aa-a71d-0522523648ca','2023-04-05 09:24:47','2023-04-05 09:24:47'),('Tomatoes','/uploads/pexels-suvan-chowdhury-428301.jpg','44923277-d2f8-483f-91dc-a0e0cbe09354','2023-04-05 09:23:49','2023-04-05 09:23:49'),('Bananas','/uploads/kamila-maciejewska-sL8P4-Ep4PY-unsplash.jpg','62fff3de-5e72-4639-87e7-8a5b1faa792a','2023-04-05 09:24:28','2023-04-05 09:24:28'),('Apples','/uploads/skylar-zilka-VW4x7oFSFJU-unsplash.jpg','95195db8-8eb3-4077-9748-ff7e594b6bca','2023-04-05 09:25:11','2023-04-05 09:25:11'),('Onions','/uploads/goh-rhy-yan-CCxWLAx0qmk-unsplash.jpg','f72a32fd-e30d-4f3b-b289-cc5903aaa619','2023-04-05 09:24:08','2023-04-05 09:24:08');
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `first_name` varchar(128) DEFAULT NULL,
  `last_name` varchar(128) DEFAULT NULL,
  `email` varchar(128) NOT NULL,
  `password` varchar(128) NOT NULL,
  `phone` varchar(128) NOT NULL,
  `image_file` varchar(128) DEFAULT NULL,
  `type` varchar(128) NOT NULL,
  `id` varchar(64) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('Bill',NULL,'bill.burr@gmail.com','c2f0750b092d29f7c1352c010809490a','+456709008','','consumer','69c4e892-274e-4a08-a595-47ad8c45fc08','2023-04-28 18:08:17','2023-04-28 18:08:17'),('bill',NULL,'bill.men@gmail.com','c2f0750b092d29f7c1352c010809490a','bill.men@gmail.com','','consumer','829a6712-e294-484e-b795-f005fb2016ad','2023-04-28 18:52:55','2023-04-28 18:52:55'),('Kirimi',NULL,'kir.kev@gmail.com','c2f0750b092d29f7c1352c010809490a','+254791364251','','consumer','88ec9bb6-0721-4a99-a06b-5ace2a963d35','2023-04-28 19:09:07','2023-04-28 19:09:07'),('Gavin',NULL,'gavin.vaughan@gmail.com','2e334771a35ae0433453e2b64867370f','+254539014191','','consumer','cf2db828-a610-427a-ba9f-05c2e0837fbd','2023-04-05 09:07:40','2023-04-05 09:07:40'),('Kevin','Campbell','kevin.campbell@gmail.com','c4d173b59953689e1c9c7586a1c38ca3','+254617148854','','farmer','e1b7d730-d010-41d6-b6dd-1ef6e85a8a22','2023-04-05 09:06:24','2023-04-05 09:06:24');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-07-03 20:21:04
