/*
SQLyog Ultimate v13.1.1 (64 bit)
MySQL - 8.0.31 : Database - alpha
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`alpha` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `alpha`;

/*Table structure for table `accounts` */

DROP TABLE IF EXISTS `accounts`;

CREATE TABLE `accounts` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(200) NOT NULL,
  `email` varchar(150) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `accounts` */

insert  into `accounts`(`id`,`username`,`password`,`email`) values 
(3,'jmerazo96','$2b$12$RP..I/F5W73pae/4hCKWLOUVz5yVMthI35BEhMNMPSviqpXFwVh5y','jmerazo96@gmail.com'),
(5,'mark','$2b$12$RP..I/F5W73pae/4hCKWLOUVz5yVMthI35BEhMNMPSviqpXFwVh5y','markbaezae@gmail.com'),
(6,'sayan','$2b$12$9Ge/fLCD0f/im8zInEYBU.7OS5nCsn/06oNI9o57bgaK7e6aJBdJy','sayanblack@gmail.com');

/*Table structure for table `delivery` */

DROP TABLE IF EXISTS `delivery`;

CREATE TABLE `delivery` (
  `id` int NOT NULL AUTO_INCREMENT,
  `document_type` varchar(30) DEFAULT NULL,
  `document_number` varchar(20) DEFAULT NULL,
  `names` varchar(60) DEFAULT NULL,
  `last_names` varchar(60) DEFAULT NULL,
  `cell` varchar(20) DEFAULT NULL,
  `pami` varchar(5) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `delivery` */

insert  into `delivery`(`id`,`document_type`,`document_number`,`names`,`last_names`,`cell`,`pami`) values 
(1,'Cédula de ciudadanía','27356026','Luz Mery','Nupan Pantoja','3152729527','5596'),
(2,'Cédula de ciudadanía','1006501241','Yeison Andrés','Aguirre Medina','3025158952','5596'),
(3,'Cédula de ciudadanía','18130158','Edwin','Ñañez Sinsajoa','3215768819','3864'),
(4,'Cédula de ciudadanía','41182036','Mariana de Jesus','Erazo Brabo','3134216166','3864'),
(5,'Cédula de ciudadanía','123456789','Carlos','Piedrahita','3223919146','3864');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
