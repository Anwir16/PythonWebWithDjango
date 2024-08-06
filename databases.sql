-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 02, 2024 at 07:21 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `finalgame`
--


CREATE DATABASE IF NOT EXISTS finalgame;

USE finalgame;
-- --------------------------------------------------------

--
-- Table structure for table `account_emailaddress`
--
CREATE TABLE `account_emailaddress` (
  `id` int(11) NOT NULL,
  `email` varchar(254) NOT NULL,
  `verified` tinyint(1) NOT NULL,
  `primary` tinyint(1) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `account_emailaddress`
--

INSERT INTO `account_emailaddress` (`id`, `email`, `verified`, `primary`, `user_id`) VALUES
(1, 'phucndce171160@fpt.edu.vn', 1, 1, 3);

-- --------------------------------------------------------

--
-- Table structure for table `account_emailconfirmation`
--

CREATE TABLE `account_emailconfirmation` (
  `id` int(11) NOT NULL,
  `created` datetime(6) NOT NULL,
  `sent` datetime(6) DEFAULT NULL,
  `key` varchar(64) NOT NULL,
  `email_address_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add user registration', 7, 'add_userregistration'),
(26, 'Can change user registration', 7, 'change_userregistration'),
(27, 'Can delete user registration', 7, 'delete_userregistration'),
(28, 'Can view user registration', 7, 'view_userregistration'),
(29, 'Can add site', 8, 'add_site'),
(30, 'Can change site', 8, 'change_site'),
(31, 'Can delete site', 8, 'delete_site'),
(32, 'Can view site', 8, 'view_site'),
(33, 'Can add email address', 9, 'add_emailaddress'),
(34, 'Can change email address', 9, 'change_emailaddress'),
(35, 'Can delete email address', 9, 'delete_emailaddress'),
(36, 'Can view email address', 9, 'view_emailaddress'),
(37, 'Can add email confirmation', 10, 'add_emailconfirmation'),
(38, 'Can change email confirmation', 10, 'change_emailconfirmation'),
(39, 'Can delete email confirmation', 10, 'delete_emailconfirmation'),
(40, 'Can view email confirmation', 10, 'view_emailconfirmation'),
(41, 'Can add social account', 11, 'add_socialaccount'),
(42, 'Can change social account', 11, 'change_socialaccount'),
(43, 'Can delete social account', 11, 'delete_socialaccount'),
(44, 'Can view social account', 11, 'view_socialaccount'),
(45, 'Can add social application', 12, 'add_socialapp'),
(46, 'Can change social application', 12, 'change_socialapp'),
(47, 'Can delete social application', 12, 'delete_socialapp'),
(48, 'Can view social application', 12, 'view_socialapp'),
(49, 'Can add social application token', 13, 'add_socialtoken'),
(50, 'Can change social application token', 13, 'change_socialtoken'),
(51, 'Can delete social application token', 13, 'delete_socialtoken'),
(52, 'Can view social application token', 13, 'view_socialtoken'),
(53, 'Can add Password Reset Token', 14, 'add_resetpasswordtoken'),
(54, 'Can change Password Reset Token', 14, 'change_resetpasswordtoken'),
(55, 'Can delete Password Reset Token', 14, 'delete_resetpasswordtoken'),
(56, 'Can view Password Reset Token', 14, 'view_resetpasswordtoken'),
(57, 'Can add profile', 15, 'add_profile'),
(58, 'Can change profile', 15, 'change_profile'),
(59, 'Can delete profile', 15, 'delete_profile'),
(60, 'Can view profile', 15, 'view_profile'),
(61, 'Can add payment history', 16, 'add_paymenthistory'),
(62, 'Can change payment history', 16, 'change_paymenthistory'),
(63, 'Can delete payment history', 16, 'delete_paymenthistory'),
(64, 'Can view payment history', 16, 'view_paymenthistory'),
(65, 'Can add combo point', 17, 'add_combopoint'),
(66, 'Can change combo point', 17, 'change_combopoint'),
(67, 'Can delete combo point', 17, 'delete_combopoint'),
(68, 'Can view combo point', 17, 'view_combopoint'),
(69, 'Can add history', 18, 'add_history'),
(70, 'Can change history', 18, 'change_history'),
(71, 'Can delete history', 18, 'delete_history'),
(72, 'Can view history', 18, 'view_history');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$720000$EaGOKdxX6Firvo3yS6nI3g$1Yco6Vb7mAs89D5iTBRUwAWVg5n1RnwYH4t6ZPi0gOQ=', '2024-06-15 02:45:49.611264', 1, 'admin', '', '', 'admin@gmail.com', 1, 1, '2024-06-15 02:41:03.122837'),
(2, 'pbkdf2_sha256$720000$R06roD1Qw6MVJ2vLqrWLn7$6RCij3OAu+wXHI6CipxFSvAfe0Y547aiQAxgmZotPNs=', '2024-06-17 14:29:11.119991', 1, 'phuc', '', '', 'phuc@gmail.com', 1, 1, '2024-06-17 14:28:53.610090'),
(3, '!6UAnG9Bs9ppBkkXsEwEaVG7SGxls3k2KUarTzj1S', '2024-07-19 09:30:44.038822', 0, 'nguyen_duy_phuc', '', '', '', 0, 1, '2024-06-17 14:37:49.776422'),
(4, 'pbkdf2_sha256$720000$fsfU9j6fVOFStINTJfbFzQ$cI2mBs3FjJgMKYY6vKfyccoOSDf9mE/OjDcumvwpkwM=', '2024-06-20 14:23:35.680038', 1, 'admin123', '', '', 'nguyenduyphuc162003@gmail.com', 1, 1, '2024-06-20 14:23:06.341905'),
(40, 'pbkdf2_sha256$720000$Op63DDimw9FL7XQI6HTgbl$R5+HI6dclfq4/NlXKt8I7SxQkE0Y+hT1QGcQnOh0x4o=', '2024-07-17 17:15:28.016379', 0, 'vand', '', '', '', 0, 1, '2024-07-17 17:15:26.838126'),
(73, 'pbkdf2_sha256$720000$4kLsLK6okZlyEwgQBNBZ23$eb8FU7g1a6wQvhZvYdeueUwLjUYn0yBlBAevgdoMMJo=', '2024-07-17 18:07:43.883040', 0, 'PhucND', '', '', '', 0, 1, '2024-07-17 18:07:42.788422');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2024-06-17 14:31:24.184090', '3', 'http://127.0.0.1:8000/', 2, '[{\"changed\": {\"fields\": [\"Domain name\", \"Display name\"]}}]', 8, 2),
(2, '2024-06-17 14:33:40.252656', '1', 'google', 1, '[{\"added\": {}}]', 12, 2);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(9, 'account', 'emailaddress'),
(10, 'account', 'emailconfirmation'),
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(14, 'django_rest_passwordreset', 'resetpasswordtoken'),
(18, 'game', 'history'),
(6, 'sessions', 'session'),
(8, 'sites', 'site'),
(11, 'socialaccount', 'socialaccount'),
(12, 'socialaccount', 'socialapp'),
(13, 'socialaccount', 'socialtoken'),
(15, 'user', 'profile'),
(7, 'user', 'userregistration'),
(17, 'wallet', 'combopoint'),
(16, 'wallet', 'paymenthistory');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-06-14 16:20:38.650002'),
(2, 'auth', '0001_initial', '2024-06-14 16:20:38.990732'),
(3, 'admin', '0001_initial', '2024-06-14 16:20:39.072329'),
(4, 'admin', '0002_logentry_remove_auto_add', '2024-06-14 16:20:39.078149'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2024-06-14 16:20:39.083835'),
(6, 'contenttypes', '0002_remove_content_type_name', '2024-06-14 16:20:39.127663'),
(7, 'auth', '0002_alter_permission_name_max_length', '2024-06-14 16:20:39.166319'),
(8, 'auth', '0003_alter_user_email_max_length', '2024-06-14 16:20:39.177741'),
(9, 'auth', '0004_alter_user_username_opts', '2024-06-14 16:20:39.182303'),
(10, 'auth', '0005_alter_user_last_login_null', '2024-06-14 16:20:39.213727'),
(11, 'auth', '0006_require_contenttypes_0002', '2024-06-14 16:20:39.216177'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2024-06-14 16:20:39.221918'),
(13, 'auth', '0008_alter_user_username_max_length', '2024-06-14 16:20:39.231798'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2024-06-14 16:20:39.241553'),
(15, 'auth', '0010_alter_group_name_max_length', '2024-06-14 16:20:39.252829'),
(16, 'auth', '0011_update_proxy_permissions', '2024-06-14 16:20:39.259057'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2024-06-14 16:20:39.269783'),
(18, 'sessions', '0001_initial', '2024-06-14 16:20:39.296556'),
(19, 'user', '0001_initial', '2024-06-14 16:20:39.305911'),
(20, 'account', '0001_initial', '2024-06-17 14:24:03.763314'),
(21, 'account', '0002_email_max_length', '2024-06-17 14:24:03.774318'),
(22, 'account', '0003_alter_emailaddress_create_unique_verified_email', '2024-06-17 14:24:03.794885'),
(23, 'account', '0004_alter_emailaddress_drop_unique_email', '2024-06-17 14:24:04.123289'),
(24, 'account', '0005_emailaddress_idx_upper_email', '2024-06-17 14:24:04.130290'),
(25, 'account', '0006_emailaddress_lower', '2024-06-17 14:24:04.143293'),
(26, 'account', '0007_emailaddress_idx_email', '2024-06-17 14:24:04.160297'),
(27, 'account', '0008_emailaddress_unique_primary_email_fixup', '2024-06-17 14:24:04.169298'),
(28, 'account', '0009_emailaddress_unique_primary_email', '2024-06-17 14:24:04.177300'),
(29, 'sites', '0001_initial', '2024-06-17 14:24:04.187304'),
(30, 'sites', '0002_alter_domain_unique', '2024-06-17 14:24:04.200819'),
(31, 'socialaccount', '0001_initial', '2024-06-17 14:24:04.486529'),
(32, 'socialaccount', '0002_token_max_lengths', '2024-06-17 14:24:04.511215'),
(33, 'socialaccount', '0003_extra_data_default_dict', '2024-06-17 14:24:04.517355'),
(34, 'socialaccount', '0004_app_provider_id_settings', '2024-06-17 14:24:04.548287'),
(35, 'socialaccount', '0005_socialtoken_nullable_app', '2024-06-17 14:24:04.794372'),
(36, 'socialaccount', '0006_alter_socialaccount_extra_data', '2024-06-17 14:24:04.839279'),
(37, 'django_rest_passwordreset', '0001_initial', '2024-06-23 16:32:43.768904'),
(38, 'django_rest_passwordreset', '0002_pk_migration', '2024-06-23 16:32:44.549716'),
(39, 'django_rest_passwordreset', '0003_allow_blank_and_null_fields', '2024-06-23 16:32:44.589736'),
(40, 'django_rest_passwordreset', '0004_alter_resetpasswordtoken_user_agent', '2024-06-23 16:32:44.602205'),
(41, 'user', '0002_profile_delete_userregistration', '2024-07-05 13:23:03.473495'),
(42, 'user', '0003_alter_profile_birthday', '2024-07-05 13:23:03.509951'),
(43, 'user', '0004_alter_profile_gender', '2024-07-05 13:23:03.521081'),
(44, 'user', '0005_alter_profile_image', '2024-07-05 13:23:03.527545'),
(45, 'user', '0006_alter_profile_image', '2024-07-05 13:23:03.534257'),
(46, 'user', '0007_alter_profile_image', '2024-07-05 13:23:03.540603'),
(47, 'user', '0008_alter_profile_image', '2024-07-05 13:23:03.549625'),
(48, 'user', '0009_profile_point', '2024-07-05 13:23:03.562945'),
(49, 'user', '0010_alter_profile_birthday', '2024-07-05 13:23:03.570061'),
(50, 'user', '0011_alter_profile_image', '2024-07-05 13:23:03.577055'),
(51, 'user', '0012_alter_profile_image', '2024-07-05 13:23:03.583507'),
(52, 'wallet', '0001_initial', '2024-07-05 13:23:03.644519'),
(53, 'wallet', '0002_combopoint_paymenthistory_combo_point', '2024-07-05 13:23:03.692747'),
(54, 'wallet', '0003_alter_combopoint_name', '2024-07-05 13:23:03.711712'),
(55, 'wallet', '0004_combopoint_price', '2024-07-05 13:23:03.720529'),
(56, 'wallet', '0005_combopoint_point', '2024-07-05 13:23:03.732157'),
(57, 'wallet', '0006_remove_paymenthistory_order_type', '2024-07-05 13:23:03.745649'),
(58, 'wallet', '0007_alter_paymenthistory_combo_point_and_more', '2024-07-05 13:23:04.650681'),
(59, 'game', '0001_initial', '2024-07-14 10:22:37.210490'),
(60, 'wallet', '0008_alter_combopoint_options', '2024-07-14 10:22:37.213773'),
(61, 'game', '0002_alter_history_user', '2024-07-14 13:59:01.881557'),
(62, 'game', '0003_remove_history_level_history_point', '2024-07-17 13:57:00.133222');

-- --------------------------------------------------------

--
-- Table structure for table `django_rest_passwordreset_resetpasswordtoken`
--

CREATE TABLE `django_rest_passwordreset_resetpasswordtoken` (
  `created_at` datetime(6) NOT NULL,
  `key` varchar(64) NOT NULL,
  `ip_address` char(39) DEFAULT NULL,
  `user_agent` varchar(512) NOT NULL,
  `user_id` int(11) NOT NULL,
  `id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('espq69toh0bs2iqadzhzt3owhhfpf9l1', '.eJxVjEEOwiAQRe_C2pDBAh1cuvcMZGBAqgaS0q6Md7dNutDtf-_9t_C0LsWvPc1-YnERSpx-t0DxmeoO-EH13mRsdZmnIHdFHrTLW-P0uh7u30GhXrYas2MwrNiGOPJAFgeXssEw6swZVDIIFtKgrUZ0RBm2QqlzpIygyYjPF-4gN-Y:1sIJQL:bg_TCZxK4kzR3WmdqXoKsFf9DOXXm21qZibucuJHiLQ', '2024-06-29 02:45:49.614947'),
('lk3trxspe1ljv8nqybw5e5s227jigufb', '.eJxVT0tuhTAMvIvXCMWJSXjs-q5RVSgk5oFKSUVCN4i7N1C6YGfNzzMbxOBGO1nnwjqnNiabOEKz7QX8Y3ZNA89pdDaNYW6_OA3BZ837Bn83NPcUyN4EDRqJqkYiKgVKIqML-F7Cz-h5yZZXCK-Js3YdjwREaRSSFtpIQ6rSKISG_aOAs0C7Rl7aU6nghnXWffJ8EHaaDri8apSn5qJj-Xab8bxct6jBxuF4QJK5VoI6z6JSVd89JHrBD1FLJWti69Aym94T5lXaOlHVCplyc5bYw_4LtOpvsw:1sUjwq:1IYAPe4RjnG59BU5XbRWFUvDp2nADjRNx9EJNJb9jbw', '2024-08-02 09:30:44.082797'),
('xk4tu8yfjv3zeqz0jnft2sr5o4v54oku', '.eJxVj7tugzAUht_lzIj6hm2yNUtUKVPXKkKOOQQrFEfYRIki3r2GkoHNOv_t8wuCt850xlo_9rEK0UQMsHvBN31-HR7Hw3Pc22txpLD7ecFt8BZD0qHzF9dDBrWJBnb92HUZ3K4WK-trrO44uMbh8FZ6fMQU-oApo4qWnLCCqbxUkhRUnqYM3vtmjC320VkTne-rX4ytr8Oy_f9OLRvihGBS9dqqBM81L4VWOpth766eIeDi_aXD5B3d3EApU5wKSaSaI4WkhEiYThksANUYcKgWJ4fN7WzsFftZMF03n_MVI188qxzyz8039mtqU9Wa0M4DgiFqTsS5RlLwojmXjNYES6IZZ1qgsdQgqqYWVCgpjSWF5hRFIkdGG5j-AGURkYQ:1sM1BP:KQ_PUrHv2XD1Z8CSRoELIDiLhOwHdmgywpgq5aVbNIs', '2024-07-09 08:05:43.886884');

-- --------------------------------------------------------

--
-- Table structure for table `django_site`
--

CREATE TABLE `django_site` (
  `id` int(11) NOT NULL,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_site`
--

INSERT INTO `django_site` (`id`, `domain`, `name`) VALUES
(3, 'http://127.0.0.1:8000/', 'http://127.0.0.1:8000/');

-- --------------------------------------------------------

--
-- Table structure for table `game_history`
--

CREATE TABLE `game_history` (
  `id` bigint(20) NOT NULL,
  `house` varchar(50) NOT NULL,
  `player` varchar(50) NOT NULL,
  `result` varchar(6) NOT NULL,
  `match_id` varchar(6) NOT NULL,
  `reward_point` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `point` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `socialaccount_socialaccount`
--

CREATE TABLE `socialaccount_socialaccount` (
  `id` int(11) NOT NULL,
  `provider` varchar(200) NOT NULL,
  `uid` varchar(191) NOT NULL,
  `last_login` datetime(6) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `extra_data` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL CHECK (json_valid(`extra_data`)),
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `socialaccount_socialaccount`
--

INSERT INTO `socialaccount_socialaccount` (`id`, `provider`, `uid`, `last_login`, `date_joined`, `extra_data`, `user_id`) VALUES
(1, 'google', '112731460672743561006', '2024-07-19 09:30:44.008712', '2024-06-17 14:37:49.787587', '{\"iss\": \"https://accounts.google.com\", \"azp\": \"1049052640941-74jbqa223ue0kinea04946leadcv1td2.apps.googleusercontent.com\", \"aud\": \"1049052640941-74jbqa223ue0kinea04946leadcv1td2.apps.googleusercontent.com\", \"sub\": \"112731460672743561006\", \"hd\": \"fpt.edu.vn\", \"email\": \"phucndce171160@fpt.edu.vn\", \"email_verified\": true, \"at_hash\": \"XO-mMPGKQy6Ov964TpyLUA\", \"name\": \"Nguyen Duy Phuc (K17 CT)\", \"picture\": \"https://lh3.googleusercontent.com/a/ACg8ocIe8g_oFbOC63HEWcnqwbrTl3w2LmfobOCpQDXIeaMBINDUm6Hc=s96-c\", \"given_name\": \"Nguyen Duy Phuc\", \"family_name\": \"(K17 CT)\", \"iat\": 1721381444, \"exp\": 1721385044}', 3);

-- --------------------------------------------------------

--
-- Table structure for table `socialaccount_socialapp`
--

CREATE TABLE `socialaccount_socialapp` (
  `id` int(11) NOT NULL,
  `provider` varchar(30) NOT NULL,
  `name` varchar(40) NOT NULL,
  `client_id` varchar(191) NOT NULL,
  `secret` varchar(191) NOT NULL,
  `key` varchar(191) NOT NULL,
  `provider_id` varchar(200) NOT NULL,
  `settings` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL CHECK (json_valid(`settings`))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `socialaccount_socialapp`
--

INSERT INTO `socialaccount_socialapp` (`id`, `provider`, `name`, `client_id`, `secret`, `key`, `provider_id`, `settings`) VALUES
(1, 'google', 'google', '1049052640941-74jbqa223ue0kinea04946leadcv1td2.apps.googleusercontent.com', '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', '', 'google', '{}');

-- --------------------------------------------------------

--
-- Table structure for table `socialaccount_socialapp_sites`
--

CREATE TABLE `socialaccount_socialapp_sites` (
  `id` bigint(20) NOT NULL,
  `socialapp_id` int(11) NOT NULL,
  `site_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `socialaccount_socialapp_sites`
--

INSERT INTO `socialaccount_socialapp_sites` (`id`, `socialapp_id`, `site_id`) VALUES
(1, 1, 3);

-- --------------------------------------------------------

--
-- Table structure for table `socialaccount_socialtoken`
--

CREATE TABLE `socialaccount_socialtoken` (
  `id` int(11) NOT NULL,
  `token` longtext NOT NULL,
  `token_secret` longtext NOT NULL,
  `expires_at` datetime(6) DEFAULT NULL,
  `account_id` int(11) NOT NULL,
  `app_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `user_profile`
--

CREATE TABLE `user_profile` (
  `id` bigint(20) NOT NULL,
  `image` varchar(100) NOT NULL,
  `gender` varchar(6) NOT NULL,
  `birthday` date NOT NULL,
  `user_id` int(11) NOT NULL,
  `point` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user_profile`
--

INSERT INTO `user_profile` (`id`, `image`, `gender`, `birthday`, `user_id`, `point`) VALUES
(1, 'images/default.png', 'Male', '2024-07-01', 1, 60),
(2, 'images/default.png', 'Male', '2024-07-01', 2, 60),
(3, 'images/default.png', 'Male', '2024-07-01', 3, 60),
(4, 'images/default.png', 'Male', '2024-07-01', 4, 60),
(44, 'images/default.png', 'Other', '2000-01-01', 40, 60),
(77, 'images/default.png', 'Other', '2000-01-01', 73, 60);

-- --------------------------------------------------------

--
-- Table structure for table `wallet_combopoint`
--

CREATE TABLE `wallet_combopoint` (
  `id` bigint(20) NOT NULL,
  `name` varchar(60) NOT NULL,
  `desc` varchar(500) DEFAULT NULL,
  `image` varchar(100) NOT NULL,
  `price` int(11) NOT NULL,
  `point` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `wallet_combopoint`
--

INSERT INTO `wallet_combopoint` (`id`, `name`, `desc`, `image`, `price`, `point`) VALUES
(1, 'Combo 1', '100 point + 20 point', 'points/combo1.png', 10000, 120),
(2, 'Combo 2', '500 point + 50 point', 'points/combo2.png', 50000, 550),
(3, 'Combo 3', '1000 point + 100 point', 'points/combo3.png', 100000, 1100);

-- --------------------------------------------------------

--
-- Table structure for table `wallet_paymenthistory`
--

CREATE TABLE `wallet_paymenthistory` (
  `id` bigint(20) NOT NULL,
  `order_id` varchar(8) NOT NULL,
  `amount` int(11) NOT NULL,
  `order_desc` varchar(100) NOT NULL,
  `order_date` datetime(6) NOT NULL,
  `user_id` int(11) NOT NULL,
  `combo_point_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `wallet_paymenthistory`
--

INSERT INTO `wallet_paymenthistory` (`id`, `order_id`, `amount`, `order_desc`, `order_date`, `user_id`, `combo_point_id`) VALUES
(1, '20240705', 100000, 'Thanh toan don hang thoi gian: 2024-07-05 15:02:31', '2024-07-05 22:03:15.000000', 3, 3),
(2, '20240705', 100000, 'Thanh toan don hang thoi gian: 2024-07-05 15:57:03', '2024-07-05 22:57:08.000000', 3, 3),
(3, '20240706', 50000, 'Thanh toan don hang thoi gian: 2024-07-06 13:07:29', '2024-07-06 20:07:31.000000', 3, 2),
(4, '20240706', 10000, 'Thanh toan don hang thoi gian: 2024-07-06 13:08:08', '2024-07-06 20:08:10.000000', 3, 1),
(5, '20240714', 50000, 'Thanh toan don hang thoi gian: 2024-07-14 15:57:22', '2024-07-14 22:57:42.000000', 3, 2),
(6, '20240714', 100000, 'Thanh toan don hang thoi gian: 2024-07-14 15:57:22', '2024-07-14 22:57:57.000000', 3, 3),
(7, '20240714', 50000, 'Thanh toan don hang thoi gian: 2024-07-14 15:59:14', '2024-07-14 22:59:16.000000', 3, 2),
(8, '20240714', 10000, 'Thanh toan don hang thoi gian: 2024-07-14 15:59:14', '2024-07-14 23:04:58.000000', 3, 1),
(9, '20240714', 100000, 'Thanh toan don hang thoi gian: 2024-07-14 16:20:22', '2024-07-14 23:20:27.000000', 3, 3),
(10, '20240714', 100000, 'Thanh toan don hang thoi gian: 2024-07-14 16:29:17', '2024-07-14 16:29:28.294767', 3, 3),
(11, '20240714', 50000, 'Thanh toan don hang thoi gian: 2024-07-14 16:29:54', '2024-07-14 16:33:47.603758', 3, 2),
(12, '20240715', 100000, 'Thanh toan don hang thoi gian: 2024-07-15 16:30:10', '2024-07-15 16:34:43.089623', 3, 3),
(13, '20240715', 100000, 'Thanh toan don hang thoi gian: 2024-07-15 16:34:43', '2024-07-15 16:35:38.709124', 3, 3),
(14, '20240715', 50000, 'Thanh toan don hang thoi gian: 2024-07-15 16:38:13', '2024-07-15 16:38:37.386336', 3, 2),
(15, '20240715', 100000, 'Thanh toan don hang thoi gian: 2024-07-15 16:48:56', '2024-07-15 16:49:30.573978', 3, 3);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `account_emailaddress`
--
ALTER TABLE `account_emailaddress`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `account_emailaddress_user_id_email_987c8728_uniq` (`user_id`,`email`),
  ADD KEY `account_emailaddress_email_03be32b2` (`email`);

--
-- Indexes for table `account_emailconfirmation`
--
ALTER TABLE `account_emailconfirmation`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `key` (`key`),
  ADD KEY `account_emailconfirm_email_address_id_5b7f8c58_fk_account_e` (`email_address_id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_rest_passwordreset_resetpasswordtoken`
--
ALTER TABLE `django_rest_passwordreset_resetpasswordtoken`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_rest_passwordreset_resetpasswordtoken_key_f1b65873_uniq` (`key`),
  ADD KEY `django_rest_password_user_id_e8015b11_fk_auth_user` (`user_id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `django_site`
--
ALTER TABLE `django_site`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_site_domain_a2e37b91_uniq` (`domain`);

--
-- Indexes for table `game_history`
--
ALTER TABLE `game_history`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `game_history_user_id_91d113f8_uniq` (`user_id`);

--
-- Indexes for table `socialaccount_socialaccount`
--
ALTER TABLE `socialaccount_socialaccount`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `socialaccount_socialaccount_provider_uid_fc810c6e_uniq` (`provider`,`uid`),
  ADD KEY `socialaccount_socialaccount_user_id_8146e70c_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `socialaccount_socialapp`
--
ALTER TABLE `socialaccount_socialapp`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `socialaccount_socialapp_sites`
--
ALTER TABLE `socialaccount_socialapp_sites`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `socialaccount_socialapp_sites_socialapp_id_site_id_71a9a768_uniq` (`socialapp_id`,`site_id`),
  ADD KEY `socialaccount_socialapp_sites_site_id_2579dee5_fk_django_site_id` (`site_id`);

--
-- Indexes for table `socialaccount_socialtoken`
--
ALTER TABLE `socialaccount_socialtoken`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `socialaccount_socialtoken_app_id_account_id_fca4e0ac_uniq` (`app_id`,`account_id`),
  ADD KEY `socialaccount_social_account_id_951f210e_fk_socialacc` (`account_id`);

--
-- Indexes for table `user_profile`
--
ALTER TABLE `user_profile`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- Indexes for table `wallet_combopoint`
--
ALTER TABLE `wallet_combopoint`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `wallet_paymenthistory`
--
ALTER TABLE `wallet_paymenthistory`
  ADD PRIMARY KEY (`id`),
  ADD KEY `wallet_paymenthistory_combo_point_id_e9fd1efb` (`combo_point_id`),
  ADD KEY `wallet_paymenthistory_user_id_fd597ef5` (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `account_emailaddress`
--
ALTER TABLE `account_emailaddress`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `account_emailconfirmation`
--
ALTER TABLE `account_emailconfirmation`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=73;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=619;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=63;

--
-- AUTO_INCREMENT for table `django_rest_passwordreset_resetpasswordtoken`
--
ALTER TABLE `django_rest_passwordreset_resetpasswordtoken`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_site`
--
ALTER TABLE `django_site`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `game_history`
--
ALTER TABLE `game_history`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `socialaccount_socialaccount`
--
ALTER TABLE `socialaccount_socialaccount`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `socialaccount_socialapp`
--
ALTER TABLE `socialaccount_socialapp`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `socialaccount_socialapp_sites`
--
ALTER TABLE `socialaccount_socialapp_sites`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `socialaccount_socialtoken`
--
ALTER TABLE `socialaccount_socialtoken`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `user_profile`
--
ALTER TABLE `user_profile`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=565;

--
-- AUTO_INCREMENT for table `wallet_combopoint`
--
ALTER TABLE `wallet_combopoint`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `wallet_paymenthistory`
--
ALTER TABLE `wallet_paymenthistory`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `account_emailaddress`
--
ALTER TABLE `account_emailaddress`
  ADD CONSTRAINT `account_emailaddress_user_id_2c513194_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `account_emailconfirmation`
--
ALTER TABLE `account_emailconfirmation`
  ADD CONSTRAINT `account_emailconfirm_email_address_id_5b7f8c58_fk_account_e` FOREIGN KEY (`email_address_id`) REFERENCES `account_emailaddress` (`id`);

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_rest_passwordreset_resetpasswordtoken`
--
ALTER TABLE `django_rest_passwordreset_resetpasswordtoken`
  ADD CONSTRAINT `django_rest_password_user_id_e8015b11_fk_auth_user` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `game_history`
--
ALTER TABLE `game_history`
  ADD CONSTRAINT `game_history_user_id_91d113f8_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `socialaccount_socialaccount`
--
ALTER TABLE `socialaccount_socialaccount`
  ADD CONSTRAINT `socialaccount_socialaccount_user_id_8146e70c_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `socialaccount_socialapp_sites`
--
ALTER TABLE `socialaccount_socialapp_sites`
  ADD CONSTRAINT `socialaccount_social_socialapp_id_97fb6e7d_fk_socialacc` FOREIGN KEY (`socialapp_id`) REFERENCES `socialaccount_socialapp` (`id`),
  ADD CONSTRAINT `socialaccount_socialapp_sites_site_id_2579dee5_fk_django_site_id` FOREIGN KEY (`site_id`) REFERENCES `django_site` (`id`);

--
-- Constraints for table `socialaccount_socialtoken`
--
ALTER TABLE `socialaccount_socialtoken`
  ADD CONSTRAINT `socialaccount_social_account_id_951f210e_fk_socialacc` FOREIGN KEY (`account_id`) REFERENCES `socialaccount_socialaccount` (`id`),
  ADD CONSTRAINT `socialaccount_social_app_id_636a42d7_fk_socialacc` FOREIGN KEY (`app_id`) REFERENCES `socialaccount_socialapp` (`id`);

--
-- Constraints for table `user_profile`
--
ALTER TABLE `user_profile`
  ADD CONSTRAINT `user_profile_user_id_8fdce8e2_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `wallet_paymenthistory`
--
ALTER TABLE `wallet_paymenthistory`
  ADD CONSTRAINT `wallet_paymenthistor_combo_point_id_e9fd1efb_fk_wallet_co` FOREIGN KEY (`combo_point_id`) REFERENCES `wallet_combopoint` (`id`),
  ADD CONSTRAINT `wallet_paymenthistory_user_id_fd597ef5_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
