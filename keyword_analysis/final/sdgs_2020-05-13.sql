# ************************************************************
# Sequel Pro SQL dump
# Version 4541
#
# http://www.sequelpro.com/
# https://github.com/sequelpro/sequelpro
#
# Host: 127.0.0.1 (MySQL 5.7.29)
# Database: sdgs
# Generation Time: 2020-05-13 13:54:25 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table input
# ------------------------------------------------------------

CREATE TABLE `input` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `text_code` varchar(32) NOT NULL,
  `class_name` varchar(32) NOT NULL,
  `teacher_name` varchar(8) NOT NULL,
  `text_content` mediumtext NOT NULL,
  `text_length` int(10) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `text_code` (`text_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table output
# ------------------------------------------------------------

CREATE TABLE `output` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `text_code` varchar(32) NOT NULL DEFAULT '',
  `category_id` int(10) unsigned NOT NULL,
  `score` decimal(12,1) NOT NULL,
  `language` varchar(8) DEFAULT NULL,
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `text_code` (`text_code`),
  KEY `category_id` (`category_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table process_detail
# ------------------------------------------------------------

CREATE TABLE `process_detail` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `text_code` varchar(32) NOT NULL DEFAULT '',
  `term_id` int(10) unsigned NOT NULL,
  `frequency` int(10) NOT NULL,
  `language` varchar(8) DEFAULT NULL,
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `text_code` (`text_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table sdgs_category
# ------------------------------------------------------------

CREATE TABLE `sdgs_category` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table sdgs_term
# ------------------------------------------------------------

CREATE TABLE `sdgs_term` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `category_id` int(10) unsigned NOT NULL,
  `term` varchar(32) NOT NULL,
  `weight` decimal(12,1) NOT NULL,
  `language` varchar(8) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `category_id` (`category_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table v_output
# ------------------------------------------------------------

CREATE TABLE `v_output` (
   `text_code` VARCHAR(32) NOT NULL DEFAULT '',
   `class_name` VARCHAR(32) NOT NULL,
   `teacher_name` VARCHAR(8) NOT NULL,
   `category_1` DECIMAL(12) NULL DEFAULT NULL,
   `category_2` DECIMAL(12) NULL DEFAULT NULL,
   `category_3` DECIMAL(12) NULL DEFAULT NULL,
   `category_4` DECIMAL(12) NULL DEFAULT NULL,
   `category_5` DECIMAL(12) NULL DEFAULT NULL,
   `category_6` DECIMAL(12) NULL DEFAULT NULL,
   `category_7` DECIMAL(12) NULL DEFAULT NULL,
   `category_8` DECIMAL(12) NULL DEFAULT NULL,
   `category_9` DECIMAL(12) NULL DEFAULT NULL,
   `category_10` DECIMAL(12) NULL DEFAULT NULL,
   `category_11` DECIMAL(12) NULL DEFAULT NULL,
   `category_12` DECIMAL(12) NULL DEFAULT NULL,
   `category_13` DECIMAL(12) NULL DEFAULT NULL,
   `category_14` DECIMAL(12) NULL DEFAULT NULL,
   `category_15` DECIMAL(12) NULL DEFAULT NULL,
   `category_16` DECIMAL(12) NULL DEFAULT NULL,
   `category_17` DECIMAL(12) NULL DEFAULT NULL,
   `text_length` INT(10) NULL DEFAULT NULL,
   `language` VARCHAR(8) NULL DEFAULT NULL,
   `create_time` TIMESTAMP NOT NULL DEFAULT '0000-00-00 00:00:00'
) ENGINE=MyISAM;



# Dump of table v_process_detail
# ------------------------------------------------------------

CREATE TABLE `v_process_detail` (
   `text_code` VARCHAR(32) NOT NULL DEFAULT '',
   `category_id` INT(10) UNSIGNED NOT NULL,
   `term` VARCHAR(32) NOT NULL,
   `weight` DECIMAL(12) NOT NULL,
   `frequency` INT(10) NOT NULL,
   `score` DECIMAL(22) NOT NULL DEFAULT '0.0',
   `language` VARCHAR(8) NULL DEFAULT NULL,
   `create_time` TIMESTAMP NOT NULL DEFAULT '0000-00-00 00:00:00'
) ENGINE=MyISAM;



# Dump of table v_term_frequency
# ------------------------------------------------------------

CREATE TABLE `v_term_frequency` (
   `category_id` INT(10) UNSIGNED NOT NULL,
   `term` VARCHAR(32) NOT NULL,
   `frequency` DECIMAL(32) NULL DEFAULT NULL
) ENGINE=MyISAM;



# Dump of table v_term_length_less_than_1
# ------------------------------------------------------------

CREATE TABLE `v_term_length_less_than_1` (
   `category_id` INT(10) UNSIGNED NOT NULL,
   `term` VARCHAR(32) NOT NULL,
   `weight` DECIMAL(12) NOT NULL
) ENGINE=MyISAM;



# Dump of table v_term_not_used
# ------------------------------------------------------------

CREATE TABLE `v_term_not_used` (
   `category_id` INT(10) UNSIGNED NOT NULL,
   `term` VARCHAR(32) NOT NULL,
   `weight` DECIMAL(12) NOT NULL
) ENGINE=MyISAM;





# Replace placeholder table for v_process_detail with correct view syntax
# ------------------------------------------------------------

DROP TABLE `v_process_detail`;

CREATE ALGORITHM=UNDEFINED DEFINER=`sdgs`@`localhost` SQL SECURITY DEFINER VIEW `v_process_detail`
AS SELECT
   `process_detail`.`text_code` AS `text_code`,
   `sdgs_term`.`category_id` AS `category_id`,
   `sdgs_term`.`term` AS `term`,
   `sdgs_term`.`weight` AS `weight`,
   `process_detail`.`frequency` AS `frequency`,(`sdgs_term`.`weight` * `process_detail`.`frequency`) AS `score`,
   `sdgs_term`.`language` AS `language`,
   `process_detail`.`create_time` AS `create_time`
FROM (`process_detail` join `sdgs_term` on((`process_detail`.`term_id` = `sdgs_term`.`id`)));


# Replace placeholder table for v_term_not_used with correct view syntax
# ------------------------------------------------------------

DROP TABLE `v_term_not_used`;

CREATE ALGORITHM=UNDEFINED DEFINER=`sdgs`@`localhost` SQL SECURITY DEFINER VIEW `v_term_not_used`
AS SELECT
   `sdgs_term`.`category_id` AS `category_id`,
   `sdgs_term`.`term` AS `term`,
   `sdgs_term`.`weight` AS `weight`
FROM `sdgs_term` where (not(`sdgs_term`.`id` in (select distinct `process_detail`.`term_id` from `process_detail`)));


# Replace placeholder table for v_term_frequency with correct view syntax
# ------------------------------------------------------------

DROP TABLE `v_term_frequency`;

CREATE ALGORITHM=UNDEFINED DEFINER=`sdgs`@`localhost` SQL SECURITY DEFINER VIEW `v_term_frequency`
AS SELECT
   `sdgs_term`.`category_id` AS `category_id`,
   `sdgs_term`.`term` AS `term`,sum(`process_detail`.`frequency`) AS `frequency`
FROM (`process_detail` join `sdgs_term` on((`process_detail`.`term_id` = `sdgs_term`.`id`))) group by `process_detail`.`term_id` order by `sdgs_term`.`category_id`,`frequency` desc;


# Replace placeholder table for v_term_length_less_than_1 with correct view syntax
# ------------------------------------------------------------

DROP TABLE `v_term_length_less_than_1`;

CREATE ALGORITHM=UNDEFINED DEFINER=`sdgs`@`localhost` SQL SECURITY DEFINER VIEW `v_term_length_less_than_1`
AS SELECT
   `sdgs_term`.`category_id` AS `category_id`,
   `sdgs_term`.`term` AS `term`,
   `sdgs_term`.`weight` AS `weight`
FROM `sdgs_term` where (char_length(`sdgs_term`.`term`) < 2);


# Replace placeholder table for v_output with correct view syntax
# ------------------------------------------------------------

DROP TABLE `v_output`;

CREATE ALGORITHM=UNDEFINED DEFINER=`sdgs`@`localhost` SQL SECURITY DEFINER VIEW `v_output`
AS SELECT
   `output`.`text_code` AS `text_code`,
   `input`.`class_name` AS `class_name`,
   `input`.`teacher_name` AS `teacher_name`,max((case when (`output`.`category_id` = 1) then `output`.`score` end)) AS `category_1`,max((case when (`output`.`category_id` = 2) then `output`.`score` end)) AS `category_2`,max((case when (`output`.`category_id` = 3) then `output`.`score` end)) AS `category_3`,max((case when (`output`.`category_id` = 4) then `output`.`score` end)) AS `category_4`,max((case when (`output`.`category_id` = 5) then `output`.`score` end)) AS `category_5`,max((case when (`output`.`category_id` = 6) then `output`.`score` end)) AS `category_6`,max((case when (`output`.`category_id` = 7) then `output`.`score` end)) AS `category_7`,max((case when (`output`.`category_id` = 8) then `output`.`score` end)) AS `category_8`,max((case when (`output`.`category_id` = 9) then `output`.`score` end)) AS `category_9`,max((case when (`output`.`category_id` = 10) then `output`.`score` end)) AS `category_10`,max((case when (`output`.`category_id` = 11) then `output`.`score` end)) AS `category_11`,max((case when (`output`.`category_id` = 12) then `output`.`score` end)) AS `category_12`,max((case when (`output`.`category_id` = 13) then `output`.`score` end)) AS `category_13`,max((case when (`output`.`category_id` = 14) then `output`.`score` end)) AS `category_14`,max((case when (`output`.`category_id` = 15) then `output`.`score` end)) AS `category_15`,max((case when (`output`.`category_id` = 16) then `output`.`score` end)) AS `category_16`,max((case when (`output`.`category_id` = 17) then `output`.`score` end)) AS `category_17`,max(`input`.`text_length`) AS `text_length`,
   `output`.`language` AS `language`,
   `output`.`create_time` AS `create_time`
FROM (`output` join `input` on((`output`.`text_code` = `input`.`text_code`))) group by `output`.`text_code`,`input`.`class_name`,`input`.`teacher_name`,`output`.`language`,`output`.`create_time`;

/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
