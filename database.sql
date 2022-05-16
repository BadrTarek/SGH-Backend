-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 16, 2022 at 10:18 PM
-- Server version: 10.4.19-MariaDB
-- PHP Version: 8.0.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `iot_project`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--
-- Error reading structure for table iot_project.auth_group: #1932 - Table 'iot_project.auth_group' doesn't exist in engine
-- Error reading data for table iot_project.auth_group: #1064 - You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'FROM `iot_project`.`auth_group`' at line 1

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--
-- Error reading structure for table iot_project.auth_group_permissions: #1932 - Table 'iot_project.auth_group_permissions' doesn't exist in engine
-- Error reading data for table iot_project.auth_group_permissions: #1064 - You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'FROM `iot_project`.`auth_group_permissions`' at line 1

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--
-- Error reading structure for table iot_project.auth_permission: #1932 - Table 'iot_project.auth_permission' doesn't exist in engine
-- Error reading data for table iot_project.auth_permission: #1064 - You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'FROM `iot_project`.`auth_permission`' at line 1

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--
-- Error reading structure for table iot_project.django_admin_log: #1932 - Table 'iot_project.django_admin_log' doesn't exist in engine
-- Error reading data for table iot_project.django_admin_log: #1064 - You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'FROM `iot_project`.`django_admin_log`' at line 1

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--
-- Error reading structure for table iot_project.django_content_type: #1932 - Table 'iot_project.django_content_type' doesn't exist in engine
-- Error reading data for table iot_project.django_content_type: #1064 - You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'FROM `iot_project`.`django_content_type`' at line 1

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--
-- Error reading structure for table iot_project.django_migrations: #1932 - Table 'iot_project.django_migrations' doesn't exist in engine
-- Error reading data for table iot_project.django_migrations: #1064 - You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'FROM `iot_project`.`django_migrations`' at line 1

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--
-- Error reading structure for table iot_project.django_session: #1932 - Table 'iot_project.django_session' doesn't exist in engine
-- Error reading data for table iot_project.django_session: #1064 - You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'FROM `iot_project`.`django_session`' at line 1

-- --------------------------------------------------------

--
-- Table structure for table `iot_actuator`
--
-- Error reading structure for table iot_project.iot_actuator: #1932 - Table 'iot_project.iot_actuator' doesn't exist in engine
-- Error reading data for table iot_project.iot_actuator: #1064 - You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'FROM `iot_project`.`iot_actuator`' at line 1

-- --------------------------------------------------------

--
-- Table structure for table `iot_actuatorsaction`
--
-- Error reading structure for table iot_project.iot_actuatorsaction: #1932 - Table 'iot_project.iot_actuatorsaction' doesn't exist in engine
-- Error reading data for table iot_project.iot_actuatorsaction: #1064 - You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'FROM `iot_project`.`iot_actuatorsaction`' at line 1

-- --------------------------------------------------------

--
-- Table structure for table `iot_product`
--
-- Error reading structure for table iot_project.iot_product: #1932 - Table 'iot_project.iot_product' doesn't exist in engine
-- Error reading data for table iot_project.iot_product: #1064 - You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'FROM `iot_project`.`iot_product`' at line 1

-- --------------------------------------------------------

--
-- Table structure for table `iot_productactuator`
--
-- Error reading structure for table iot_project.iot_productactuator: #1932 - Table 'iot_project.iot_productactuator' doesn't exist in engine
-- Error reading data for table iot_project.iot_productactuator: #1064 - You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'FROM `iot_project`.`iot_productactuator`' at line 1

-- --------------------------------------------------------

--
-- Table structure for table `iot_productsensor`
--
-- Error reading structure for table iot_project.iot_productsensor: #1932 - Table 'iot_project.iot_productsensor' doesn't exist in engine
-- Error reading data for table iot_project.iot_productsensor: #1064 - You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'FROM `iot_project`.`iot_productsensor`' at line 1

-- --------------------------------------------------------

--
-- Table structure for table `iot_sensor`
--
-- Error reading structure for table iot_project.iot_sensor: #1932 - Table 'iot_project.iot_sensor' doesn't exist in engine
-- Error reading data for table iot_project.iot_sensor: #1064 - You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'FROM `iot_project`.`iot_sensor`' at line 1

-- --------------------------------------------------------

--
-- Table structure for table `iot_sensorvalues`
--
-- Error reading structure for table iot_project.iot_sensorvalues: #1932 - Table 'iot_project.iot_sensorvalues' doesn't exist in engine
-- Error reading data for table iot_project.iot_sensorvalues: #1064 - You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'FROM `iot_project`.`iot_sensorvalues`' at line 1

-- --------------------------------------------------------

--
-- Table structure for table `token_blacklist_blacklistedtoken`
--
-- Error reading structure for table iot_project.token_blacklist_blacklistedtoken: #1932 - Table 'iot_project.token_blacklist_blacklistedtoken' doesn't exist in engine
-- Error reading data for table iot_project.token_blacklist_blacklistedtoken: #1064 - You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'FROM `iot_project`.`token_blacklist_blacklistedtoken`' at line 1

-- --------------------------------------------------------

--
-- Table structure for table `token_blacklist_outstandingtoken`
--
-- Error reading structure for table iot_project.token_blacklist_outstandingtoken: #1932 - Table 'iot_project.token_blacklist_outstandingtoken' doesn't exist in engine
-- Error reading data for table iot_project.token_blacklist_outstandingtoken: #1064 - You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'FROM `iot_project`.`token_blacklist_outstandingtoken`' at line 1

-- --------------------------------------------------------

--
-- Table structure for table `users_user`
--
-- Error reading structure for table iot_project.users_user: #1932 - Table 'iot_project.users_user' doesn't exist in engine
-- Error reading data for table iot_project.users_user: #1064 - You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'FROM `iot_project`.`users_user`' at line 1

-- --------------------------------------------------------

--
-- Table structure for table `users_user_groups`
--
-- Error reading structure for table iot_project.users_user_groups: #1932 - Table 'iot_project.users_user_groups' doesn't exist in engine
-- Error reading data for table iot_project.users_user_groups: #1064 - You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'FROM `iot_project`.`users_user_groups`' at line 1

-- --------------------------------------------------------

--
-- Table structure for table `users_user_user_permissions`
--
-- Error reading structure for table iot_project.users_user_user_permissions: #1932 - Table 'iot_project.users_user_user_permissions' doesn't exist in engine
-- Error reading data for table iot_project.users_user_user_permissions: #1064 - You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'FROM `iot_project`.`users_user_user_permissions`' at line 1
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
