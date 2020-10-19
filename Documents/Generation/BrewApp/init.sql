-- Adminer 4.7.7 MySQL dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

SET NAMES utf8mb4;

CREATE DATABASE `brew_app` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `brew_app`;

DROP TABLE IF EXISTS `drinks`;
CREATE TABLE `drinks` (
  `Drink_ID` int NOT NULL AUTO_INCREMENT,
  `Drink_Name` varchar(50) DEFAULT NULL,
  `Drink_Temp` varchar(10) DEFAULT NULL,
  `InStock` tinyint(1) NOT NULL DEFAULT '0',
  `Quantity` int DEFAULT '0',
  PRIMARY KEY (`Drink_ID`),
  UNIQUE KEY `Drink_Name` (`Drink_Name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `drinks` (`Drink_ID`, `Drink_Name`, `Drink_Temp`, `InStock`, `Quantity`) VALUES
(1,	'Tea',	NULL,	0,	0),
(2,	'Mocha',	NULL,	0,	0),
(3,	'Coffee',	NULL,	0,	0),
(4,	'Cortado',	NULL,	0,	0),
(5,	'Water',	NULL,	0,	0),
(6,	'Coke',	NULL,	0,	0),
(7,	'Orange juice',	NULL,	0,	0),
(8,	'Test drink',	NULL,	0,	0);

DROP TABLE IF EXISTS `orders`;
CREATE TABLE `orders` (
  `round_id` int NOT NULL,
  `order_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `drink` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`round_id`,`order_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `orders` (`round_id`, `order_id`, `name`, `drink`) VALUES
(3,	1,	'Maria',	'Water'),
(2,	1,	'Joe',	'Coffee'),
(1,	3,	'Joe',	'Coffee'),
(1,	2,	'Aria',	'Orange juice'),
(1,	1,	'Aria',	'Tea');

DROP TABLE IF EXISTS `preferences`;
CREATE TABLE `preferences` (
  `user_name` varchar(50) NOT NULL,
  `fav_drink` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`user_name`),
  UNIQUE KEY `user_name` (`user_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `preferences` (`user_name`, `fav_drink`) VALUES
('Aria',	'Water'),
('John',	'Cortado'),
('Maria',	'Tea'),
('Suman',	'Almdudler (discontinued)');

DROP TABLE IF EXISTS `rounds`;
CREATE TABLE `rounds` (
  `round_id` int NOT NULL AUTO_INCREMENT,
  `owner` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `brewer` varchar(50) DEFAULT NULL,
  `active_status` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`round_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `rounds` (`round_id`, `owner`, `brewer`, `active_status`) VALUES
(1,	'Aria',	'Khalid',	'Yes'),
(2,	'John',	'Khalid',	'Yes'),
(3,	'John',	'Joe',	'Yes'),
(4,	'Suman',	'Joe',	'Yes'),
(5,	'Joe',	'Will',	'Yes'),
(6,	'Maria',	'Will',	'Yes');

DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `PersonID` int NOT NULL AUTO_INCREMENT,
  `Person_first_name` varchar(50) NOT NULL,
  `Person_last_name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `Person_age` int DEFAULT '16',
  PRIMARY KEY (`PersonID`),
  UNIQUE KEY `Person_first_name` (`Person_first_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `users` (`PersonID`, `Person_first_name`, `Person_last_name`, `Person_age`) VALUES
(1,	'John',	NULL,	16),
(2,	'Maria',	NULL,	16),
(3,	'Joe',	NULL,	16),
(4,	'Aria',	NULL,	16),
(5,	'Suman',	NULL,	16),
(14,	'Billie',	NULL,	16);

-- 2020-10-08 10:33:15

