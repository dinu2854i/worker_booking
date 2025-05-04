/*
SQLyog Enterprise - MySQL GUI v6.56
MySQL - 5.0.67-community-nt : Database - service_portal
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`service_portal` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `service_portal`;

/*Table structure for table `message` */

DROP TABLE IF EXISTS `message`;

CREATE TABLE `message` (
  `id` int(11) NOT NULL auto_increment,
  `w_id` varchar(1000) default NULL,
  `worker` varchar(1000) default NULL,
  `u_id` varchar(1000) default NULL,
  `msg` varchar(1000) default NULL,
  `replay` varchar(1000) default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `message` */

insert  into `message`(`id`,`w_id`,`worker`,`u_id`,`msg`,`replay`) values (1,'1','Electrician','2','will you able to negotiate','yes iam negotiable'),(2,'1','Electrician','2','hello are you there','waiting'),(3,'3','Driver','2','can you able to come for 800','ok fine');

/*Table structure for table `product` */

DROP TABLE IF EXISTS `product`;

CREATE TABLE `product` (
  `id` int(11) NOT NULL auto_increment,
  `shop_id` varchar(100) default NULL,
  `pname` varchar(1000) default NULL,
  `price` varchar(1000) default NULL,
  `available` varchar(1000) default NULL,
  `usage` varchar(1000) default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `product` */

insert  into `product`(`id`,`shop_id`,`pname`,`price`,`available`,`usage`) values (1,'1','cooking oil','145','12','cocking'),(2,'1','soap','12','12','batching');

/*Table structure for table `product_book` */

DROP TABLE IF EXISTS `product_book`;

CREATE TABLE `product_book` (
  `id` int(11) NOT NULL auto_increment,
  `user_id` varchar(1000) default NULL,
  `product_id` varchar(1000) default NULL,
  `shop_id` varchar(1000) default NULL,
  `date` varchar(1000) default NULL,
  `status` varchar(1000) default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `product_book` */

insert  into `product_book`(`id`,`user_id`,`product_id`,`shop_id`,`date`,`status`) values (1,'1','2','1','2024-02-28 18:55:41','Accepted');

/*Table structure for table `register` */

DROP TABLE IF EXISTS `register`;

CREATE TABLE `register` (
  `id` int(11) NOT NULL auto_increment,
  `name` varchar(1000) default NULL,
  `email` varchar(1000) default NULL,
  `mobile` varchar(1000) default NULL,
  `address` varchar(1000) default NULL,
  `username` varchar(200) default NULL,
  `password` varchar(1000) default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `register` */

insert  into `register`(`id`,`name`,`email`,`mobile`,`address`,`username`,`password`) values (1,'customer','customer@gmail.com','1234567890','hyd','customer','123'),(2,'kishan','kishan@gmail.com','1234567890','hyd','kishan','123');

/*Table structure for table `service` */

DROP TABLE IF EXISTS `service`;

CREATE TABLE `service` (
  `id` int(11) NOT NULL auto_increment,
  `service` varchar(1000) default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `service` */

insert  into `service`(`id`,`service`) values (1,'plumber'),(2,'Electrician'),(3,'Driver'),(4,'Cliner');

/*Table structure for table `service_book` */

DROP TABLE IF EXISTS `service_book`;

CREATE TABLE `service_book` (
  `id` int(11) NOT NULL auto_increment,
  `userid` varchar(1000) default NULL,
  `service_id` varchar(1000) default NULL,
  `date` varchar(1000) default NULL,
  `status` varchar(1000) default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `service_book` */

insert  into `service_book`(`id`,`userid`,`service_id`,`date`,`status`) values (1,'1','1','2024-02-28 18:44:27','Accepted'),(2,'1','1','2024-02-28 20:25:44','Accepted'),(3,'2','1','2024-05-21 19:54:34','Accepted'),(4,'2','3','2024-05-21 20:37:12','Accepted');

/*Table structure for table `sregister` */

DROP TABLE IF EXISTS `sregister`;

CREATE TABLE `sregister` (
  `id` int(11) NOT NULL auto_increment,
  `service` varchar(1000) default NULL,
  `email` varchar(1000) default NULL,
  `username` varchar(1000) default NULL,
  `password` varchar(1000) default NULL,
  `w_hours` varchar(1000) default NULL,
  `cost` varchar(1000) default NULL,
  `mobile` varchar(1000) default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `sregister` */

insert  into `sregister`(`id`,`service`,`email`,`username`,`password`,`w_hours`,`cost`,`mobile`) values (1,'Electrician','kishangadicherla508@gmail.com','electrian','123','6hr','1500','9876786543'),(2,'plumber','venkat@gmail.com','venkat','123','7hr','1700','96402572921'),(3,'Driver','driver@gmail.com','driver@gmail.com','123','8','1000','9876543210');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*
SQLyog Enterprise - MySQL GUI v6.56
MySQL - 5.0.67-community-nt : Database - service_portal
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`service_portal` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `service_portal`;

/*Table structure for table `group_chat` */

DROP TABLE IF EXISTS `group_chat`;

CREATE TABLE `group_chat` (
  `id` int(11) NOT NULL auto_increment,
  `uid` varchar(1000) default NULL,
  `message` longtext,
  `s_id` varchar(1000) default NULL,
  `reply` longtext,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `group_chat` */

insert  into `group_chat`(`id`,`uid`,`message`,`s_id`,`reply`) values (1,'2','i need to help by sharing my lorry space i have only two tones of material but it can handle 10 tones  if any one required transport space please contact me 1234567890','3','ok i need remaining spance'),(2,'2','i need to help by sharing my lorry space i have only two tones of material but it can handle 10 tones  if any one required transport space please contact me 1234567890','waiting','waiting');

/*Table structure for table `message` */

DROP TABLE IF EXISTS `message`;

CREATE TABLE `message` (
  `id` int(11) NOT NULL auto_increment,
  `w_id` varchar(1000) default NULL,
  `worker` varchar(1000) default NULL,
  `u_id` varchar(1000) default NULL,
  `msg` varchar(1000) default NULL,
  `replay` varchar(1000) default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `message` */

insert  into `message`(`id`,`w_id`,`worker`,`u_id`,`msg`,`replay`) values (1,'1','Electrician','2','will you able to negotiate','yes iam negotiable'),(2,'1','Electrician','2','hello are you there','waiting'),(3,'3','Driver','2','can you able to come for 800','ok fine');

/*Table structure for table `product` */

DROP TABLE IF EXISTS `product`;

CREATE TABLE `product` (
  `id` int(11) NOT NULL auto_increment,
  `shop_id` varchar(100) default NULL,
  `pname` varchar(1000) default NULL,
  `price` varchar(1000) default NULL,
  `available` varchar(1000) default NULL,
  `usage` varchar(1000) default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `product` */

insert  into `product`(`id`,`shop_id`,`pname`,`price`,`available`,`usage`) values (1,'1','cooking oil','145','12','cocking'),(2,'1','soap','12','12','batching');

/*Table structure for table `product_book` */

DROP TABLE IF EXISTS `product_book`;

CREATE TABLE `product_book` (
  `id` int(11) NOT NULL auto_increment,
  `user_id` varchar(1000) default NULL,
  `product_id` varchar(1000) default NULL,
  `shop_id` varchar(1000) default NULL,
  `date` varchar(1000) default NULL,
  `status` varchar(1000) default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `product_book` */

insert  into `product_book`(`id`,`user_id`,`product_id`,`shop_id`,`date`,`status`) values (1,'1','2','1','2024-02-28 18:55:41','Accepted');

/*Table structure for table `register` */

DROP TABLE IF EXISTS `register`;

CREATE TABLE `register` (
  `id` int(11) NOT NULL auto_increment,
  `name` varchar(1000) default NULL,
  `email` varchar(1000) default NULL,
  `mobile` varchar(1000) default NULL,
  `address` varchar(1000) default NULL,
  `username` varchar(200) default NULL,
  `password` varchar(1000) default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `register` */

insert  into `register`(`id`,`name`,`email`,`mobile`,`address`,`username`,`password`) values (1,'customer','customer@gmail.com','1234567890','hyd','customer','123'),(2,'kishan','kishan@gmail.com','1234567890','hyd','kishan','123'),(3,'venkat','venkat@gmail.com','01234567890','hyd','venkat','123'),(4,'abc','abc@gmail.com','1234567890','hyd','abc','123');

/*Table structure for table `service` */

DROP TABLE IF EXISTS `service`;

CREATE TABLE `service` (
  `id` int(11) NOT NULL auto_increment,
  `service` varchar(1000) default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `service` */

insert  into `service`(`id`,`service`) values (1,'plumber'),(2,'Electrician'),(3,'Driver'),(4,'Cliner');

/*Table structure for table `service_book` */

DROP TABLE IF EXISTS `service_book`;

CREATE TABLE `service_book` (
  `id` int(11) NOT NULL auto_increment,
  `userid` varchar(1000) default NULL,
  `service_id` varchar(1000) default NULL,
  `date` varchar(1000) default NULL,
  `status` varchar(1000) default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `service_book` */

insert  into `service_book`(`id`,`userid`,`service_id`,`date`,`status`) values (1,'1','1','2024-02-28 18:44:27','Accepted'),(2,'1','1','2024-02-28 20:25:44','Accepted'),(3,'2','1','2024-05-21 19:54:34','Accepted'),(4,'2','3','2024-05-21 20:37:12','Accepted');

/*Table structure for table `sregister` */

DROP TABLE IF EXISTS `sregister`;

CREATE TABLE `sregister` (
  `id` int(11) NOT NULL auto_increment,
  `service` varchar(1000) default NULL,
  `email` varchar(1000) default NULL,
  `username` varchar(1000) default NULL,
  `password` varchar(1000) default NULL,
  `w_hours` varchar(1000) default NULL,
  `cost` varchar(1000) default NULL,
  `mobile` varchar(1000) default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `sregister` */

insert  into `sregister`(`id`,`service`,`email`,`username`,`password`,`w_hours`,`cost`,`mobile`) values (1,'Electrician','kishangadicherla508@gmail.com','electrian','123','6hr','1500','9876786543'),(2,'plumber','venkat@gmail.com','venkat','123','7hr','1700','96402572921'),(3,'Driver','driver@gmail.com','driver@gmail.com','123','8','1000','9876543210');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;

