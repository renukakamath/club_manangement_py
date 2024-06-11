/*
SQLyog Community v13.1.6 (64 bit)
MySQL - 5.7.9 : Database - club_membership
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`club_membership` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `club_membership`;

/*Table structure for table `card` */

DROP TABLE IF EXISTS `card`;

CREATE TABLE `card` (
  `card_id` int(11) DEFAULT NULL,
  `cust_id` int(11) DEFAULT NULL,
  `card_no` varchar(100) DEFAULT NULL,
  `card_name` varchar(100) DEFAULT NULL,
  `exp_date` varchar(100) DEFAULT NULL,
  `cvv` varchar(100) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `card` */

insert  into `card`(`card_id`,`cust_id`,`card_no`,`card_name`,`exp_date`,`cvv`) values 
(NULL,1,'1234567890123456','sdfgh','2023-02-28','123'),
(NULL,1,'1234567890123456','sdfgh','2023-02-28','123'),
(NULL,1,'1234567890123456','sdfgh','2023-02-28','123');

/*Table structure for table `category` */

DROP TABLE IF EXISTS `category`;

CREATE TABLE `category` (
  `cat_id` int(11) NOT NULL AUTO_INCREMENT,
  `staff_id` int(11) DEFAULT NULL,
  `Name` varchar(100) DEFAULT NULL,
  `Description` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`cat_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `category` */

insert  into `category`(`cat_id`,`staff_id`,`Name`,`Description`) values 
(1,0,'ssdfghj','sdfghj');

/*Table structure for table `event` */

DROP TABLE IF EXISTS `event`;

CREATE TABLE `event` (
  `event_id` int(11) NOT NULL AUTO_INCREMENT,
  `hall_id` int(11) DEFAULT NULL,
  `b_date` varchar(100) DEFAULT NULL,
  `h_rate` varchar(100) DEFAULT NULL,
  `event_type` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`event_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `event` */

insert  into `event`(`event_id`,`hall_id`,`b_date`,`h_rate`,`event_type`) values 
(1,1,'123467','500','wsdfgh fghjh');

/*Table structure for table `fee` */

DROP TABLE IF EXISTS `fee`;

CREATE TABLE `fee` (
  `fee_id` int(11) NOT NULL AUTO_INCREMENT,
  `men_id` int(11) DEFAULT NULL,
  `card_id` int(11) DEFAULT NULL,
  `reg_fee` decimal(10,0) DEFAULT NULL,
  `p_date` varchar(100) DEFAULT NULL,
  `fee_status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`fee_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `fee` */

insert  into `fee`(`fee_id`,`men_id`,`card_id`,`reg_fee`,`p_date`,`fee_status`) values 
(1,1,0,500,'2023-02-26','Paid'),
(2,1,0,500,'2023-02-26','Paid'),
(3,1,0,500,'2023-02-26','Paid');

/*Table structure for table `hall` */

DROP TABLE IF EXISTS `hall`;

CREATE TABLE `hall` (
  `hall_id` int(11) NOT NULL AUTO_INCREMENT,
  `cat_id` int(11) DEFAULT NULL,
  `subcat_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`hall_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `hall` */

insert  into `hall`(`hall_id`,`cat_id`,`subcat_id`) values 
(1,1,1),
(2,2,1),
(3,2,1),
(4,2,1),
(5,2,1);

/*Table structure for table `hallpay` */

DROP TABLE IF EXISTS `hallpay`;

CREATE TABLE `hallpay` (
  `hpay_id` int(11) NOT NULL AUTO_INCREMENT,
  `event_id` int(11) DEFAULT NULL,
  `men_id` int(11) DEFAULT NULL,
  `pay_amt` varchar(100) DEFAULT NULL,
  `p_date` varchar(100) DEFAULT NULL,
  `fee_status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`hpay_id`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `hallpay` */

insert  into `hallpay`(`hpay_id`,`event_id`,`men_id`,`pay_amt`,`p_date`,`fee_status`) values 
(1,1,1,'500','2023-02-26','Paid'),
(2,1,1,'500','2023-02-26','Booked'),
(3,1,1,'500','2023-02-26','Booked'),
(4,1,1,'500','2023-02-26','Booked'),
(5,1,1,'500','2023-02-26','Booked'),
(6,1,1,'500','2023-02-26','Booked'),
(7,1,1,'500','2023-02-26','Booked'),
(8,1,1,'500','2023-02-26','Booked'),
(9,1,1,'500','2023-02-26','Booked');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `username` varchar(100) NOT NULL,
  `password` varchar(100) DEFAULT NULL,
  `user_type` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`username`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`username`,`password`,`user_type`,`status`) values 
('member@gamil.com','member','member','1'),
('admin@gmail.com','admin','admin','1'),
('student1@gmail.com','sdf','staff','1');

/*Table structure for table `men` */

DROP TABLE IF EXISTS `men`;

CREATE TABLE `men` (
  `men_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `men_fname` varchar(100) DEFAULT NULL,
  `men_lname` varchar(100) DEFAULT NULL,
  `men_housename` varchar(100) DEFAULT NULL,
  `men_city` varchar(100) DEFAULT NULL,
  `men_district` varchar(100) DEFAULT NULL,
  `men_state` varchar(100) DEFAULT NULL,
  `men_pincode` decimal(6,0) DEFAULT NULL,
  `men_phone` decimal(10,0) DEFAULT NULL,
  `men_password` varchar(100) DEFAULT NULL,
  `men_status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`men_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `men` */

insert  into `men`(`men_id`,`username`,`men_fname`,`men_lname`,`men_housename`,`men_city`,`men_district`,`men_state`,`men_pincode`,`men_phone`,`men_password`,`men_status`) values 
(1,'member@gamil.com','user','qwerty','xfdsgdsg','ddgdsgdsg','ekm','dgdsgd',123456,2345678907,'pass','1');

/*Table structure for table `pay` */

DROP TABLE IF EXISTS `pay`;

CREATE TABLE `pay` (
  `pay_id` int(11) NOT NULL AUTO_INCREMENT,
  `fee_id` int(11) DEFAULT NULL,
  `hpay_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`pay_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `pay` */

insert  into `pay`(`pay_id`,`fee_id`,`hpay_id`) values 
(1,1,1),
(2,1,2),
(3,1,3);

/*Table structure for table `staff` */

DROP TABLE IF EXISTS `staff`;

CREATE TABLE `staff` (
  `staff_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `staff_fname` varchar(100) DEFAULT NULL,
  `staff_lname` varchar(100) DEFAULT NULL,
  `staff_phone` decimal(10,0) DEFAULT NULL,
  `staff_gen` varchar(100) DEFAULT NULL,
  `staff_city` varchar(100) DEFAULT NULL,
  `staff_district` varchar(100) DEFAULT NULL,
  `staff_state` varchar(100) DEFAULT NULL,
  `staff_pin` decimal(6,0) DEFAULT NULL,
  `sdoj` varchar(100) DEFAULT NULL,
  `staff_status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`staff_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `staff` */

insert  into `staff`(`staff_id`,`username`,`staff_fname`,`staff_lname`,`staff_phone`,`staff_gen`,`staff_city`,`staff_district`,`staff_state`,`staff_pin`,`sdoj`,`staff_status`) values 
(1,'student1@gmail.com','users','qwertys',2345678901,'on','ddgdsgdsgs','ekms','dgdsgds',123456,'2023-03-02','1');

/*Table structure for table `subcat` */

DROP TABLE IF EXISTS `subcat`;

CREATE TABLE `subcat` (
  `subcat_id` int(11) NOT NULL AUTO_INCREMENT,
  `subcat_name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`subcat_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `subcat` */

insert  into `subcat`(`subcat_id`,`subcat_name`) values 
(1,'sdefrghjk'),
(2,'sdefrghjkss');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
