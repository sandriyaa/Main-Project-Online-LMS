-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 17, 2025 at 06:48 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.0.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `lms_db`
--

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
(25, 'Can add batch', 7, 'add_batch'),
(26, 'Can change batch', 7, 'change_batch'),
(27, 'Can delete batch', 7, 'delete_batch'),
(28, 'Can view batch', 7, 'view_batch'),
(29, 'Can add category', 8, 'add_category'),
(30, 'Can change category', 8, 'change_category'),
(31, 'Can delete category', 8, 'delete_category'),
(32, 'Can view category', 8, 'view_category'),
(33, 'Can add lesson', 9, 'add_lesson'),
(34, 'Can change lesson', 9, 'change_lesson'),
(35, 'Can delete lesson', 9, 'delete_lesson'),
(36, 'Can view lesson', 9, 'view_lesson'),
(37, 'Can add login', 10, 'add_login'),
(38, 'Can change login', 10, 'change_login'),
(39, 'Can delete login', 10, 'delete_login'),
(40, 'Can view login', 10, 'view_login'),
(41, 'Can add subject', 11, 'add_subject'),
(42, 'Can change subject', 11, 'change_subject'),
(43, 'Can delete subject', 11, 'delete_subject'),
(44, 'Can view subject', 11, 'view_subject'),
(45, 'Can add assignment', 12, 'add_assignment'),
(46, 'Can change assignment', 12, 'change_assignment'),
(47, 'Can delete assignment', 12, 'delete_assignment'),
(48, 'Can view assignment', 12, 'view_assignment'),
(49, 'Can add course', 13, 'add_course'),
(50, 'Can change course', 13, 'change_course'),
(51, 'Can delete course', 13, 'delete_course'),
(52, 'Can view course', 13, 'view_course'),
(53, 'Can add exam', 14, 'add_exam'),
(54, 'Can change exam', 14, 'change_exam'),
(55, 'Can delete exam', 14, 'delete_exam'),
(56, 'Can view exam', 14, 'view_exam'),
(57, 'Can add lecture_notes', 15, 'add_lecture_notes'),
(58, 'Can change lecture_notes', 15, 'change_lecture_notes'),
(59, 'Can delete lecture_notes', 15, 'delete_lecture_notes'),
(60, 'Can view lecture_notes', 15, 'view_lecture_notes'),
(61, 'Can add doubts', 16, 'add_doubts'),
(62, 'Can change doubts', 16, 'change_doubts'),
(63, 'Can delete doubts', 16, 'delete_doubts'),
(64, 'Can view doubts', 16, 'view_doubts'),
(65, 'Can add questions', 17, 'add_questions'),
(66, 'Can change questions', 17, 'change_questions'),
(67, 'Can delete questions', 17, 'delete_questions'),
(68, 'Can view questions', 17, 'view_questions'),
(69, 'Can add student_register', 18, 'add_student_register'),
(70, 'Can change student_register', 18, 'change_student_register'),
(71, 'Can delete student_register', 18, 'delete_student_register'),
(72, 'Can view student_register', 18, 'view_student_register'),
(73, 'Can add feedback', 19, 'add_feedback'),
(74, 'Can change feedback', 19, 'change_feedback'),
(75, 'Can delete feedback', 19, 'delete_feedback'),
(76, 'Can view feedback', 19, 'view_feedback'),
(77, 'Can add enrollment', 20, 'add_enrollment'),
(78, 'Can change enrollment', 20, 'change_enrollment'),
(79, 'Can delete enrollment', 20, 'delete_enrollment'),
(80, 'Can view enrollment', 20, 'view_enrollment'),
(81, 'Can add answers', 21, 'add_answers'),
(82, 'Can change answers', 21, 'change_answers'),
(83, 'Can delete answers', 21, 'delete_answers'),
(84, 'Can view answers', 21, 'view_answers'),
(85, 'Can add submission', 22, 'add_submission'),
(86, 'Can change submission', 22, 'change_submission'),
(87, 'Can delete submission', 22, 'delete_submission'),
(88, 'Can view submission', 22, 'view_submission'),
(89, 'Can add teacher_register', 23, 'add_teacher_register'),
(90, 'Can change teacher_register', 23, 'change_teacher_register'),
(91, 'Can delete teacher_register', 23, 'delete_teacher_register'),
(92, 'Can view teacher_register', 23, 'view_teacher_register');

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
(1, 'pbkdf2_sha256$720000$No6zfCHcHc7v7vBQQSYP40$46jogNAFBUpWk8+/kdhwHxk3UrYvpf17Ea/0xZrgiWs=', NULL, 1, 'admin', '', '', 'admin@gmail.com', 1, 1, '2025-03-17 15:45:22.066147');

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
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(21, 'lmsapp', 'answers'),
(12, 'lmsapp', 'assignment'),
(7, 'lmsapp', 'batch'),
(8, 'lmsapp', 'category'),
(13, 'lmsapp', 'course'),
(16, 'lmsapp', 'doubts'),
(20, 'lmsapp', 'enrollment'),
(14, 'lmsapp', 'exam'),
(19, 'lmsapp', 'feedback'),
(15, 'lmsapp', 'lecture_notes'),
(9, 'lmsapp', 'lesson'),
(10, 'lmsapp', 'login'),
(17, 'lmsapp', 'questions'),
(18, 'lmsapp', 'student_register'),
(11, 'lmsapp', 'subject'),
(22, 'lmsapp', 'submission'),
(23, 'lmsapp', 'teacher_register'),
(6, 'sessions', 'session');

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
(1, 'contenttypes', '0001_initial', '2025-03-17 15:42:20.859933'),
(2, 'auth', '0001_initial', '2025-03-17 15:42:34.170794'),
(3, 'admin', '0001_initial', '2025-03-17 15:42:36.211355'),
(4, 'admin', '0002_logentry_remove_auto_add', '2025-03-17 15:42:36.243441'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2025-03-17 15:42:36.300600'),
(6, 'contenttypes', '0002_remove_content_type_name', '2025-03-17 15:42:37.118772'),
(7, 'auth', '0002_alter_permission_name_max_length', '2025-03-17 15:42:38.286952'),
(8, 'auth', '0003_alter_user_email_max_length', '2025-03-17 15:42:38.659992'),
(9, 'auth', '0004_alter_user_username_opts', '2025-03-17 15:42:38.808387'),
(10, 'auth', '0005_alter_user_last_login_null', '2025-03-17 15:42:40.094948'),
(11, 'auth', '0006_require_contenttypes_0002', '2025-03-17 15:42:40.189196'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2025-03-17 15:42:40.249348'),
(13, 'auth', '0008_alter_user_username_max_length', '2025-03-17 15:42:40.431955'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2025-03-17 15:42:41.174082'),
(15, 'auth', '0010_alter_group_name_max_length', '2025-03-17 15:42:41.642287'),
(16, 'auth', '0011_update_proxy_permissions', '2025-03-17 15:42:41.748685'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2025-03-17 15:42:41.977297'),
(18, 'lmsapp', '0001_initial', '2025-03-17 15:43:34.253510'),
(19, 'sessions', '0001_initial', '2025-03-17 15:43:35.932979');

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
('5u0oy688t9mt3175ybn9lokf88hojlcq', 'eyJsb2dpbl9pZCI6MSwidGVhY2hlciI6MX0:1tuEY0:rIdGTVYbiKzcTua0YMdR1UlEoo3o2q8vOqTwnM8nxoQ', '2025-03-31 17:46:44.825030'),
('a5k2cp856y038e9nfa0psjz4pcoikfjr', 'eyJsb2dpbl9pZCI6Niwic3R1ZGVudCI6MX0:1tuEHk:ZGI2ZIdnonG8Ubt9wz3vGExn4HfN3i3f2nLql32s3Rc', '2025-03-31 17:29:56.744522');

-- --------------------------------------------------------

--
-- Table structure for table `tb_answers`
--

CREATE TABLE `tb_answers` (
  `a_id` int(11) NOT NULL,
  `answer` varchar(200) DEFAULT NULL,
  `question_id` int(11) DEFAULT NULL,
  `student_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tb_answers`
--

INSERT INTO `tb_answers` (`a_id`, `answer`, `question_id`, `student_id`) VALUES
(1, 'True', 1, 1),
(2, '27', 2, 1),
(3, 'True', 3, 1),
(4, 'AND', 4, 1),
(5, 'Hello 3 times', 5, 1);

-- --------------------------------------------------------

--
-- Table structure for table `tb_assignment`
--

CREATE TABLE `tb_assignment` (
  `a_id` int(11) NOT NULL,
  `title` varchar(100) NOT NULL,
  `description` longtext DEFAULT NULL,
  `due_date` date NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `total_mark` double NOT NULL,
  `status` tinyint(1) NOT NULL,
  `teacher_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tb_assignment`
--

INSERT INTO `tb_assignment` (`a_id`, `title`, `description`, `due_date`, `created_at`, `total_mark`, `status`, `teacher_id`) VALUES
(1, 'Python operators assignment', 'Assignment operators in Python are used to assign values to variables', '2025-03-21', '2025-03-17 17:05:44.438549', 30, 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `tb_assignment_batch`
--

CREATE TABLE `tb_assignment_batch` (
  `id` bigint(20) NOT NULL,
  `assignment_id` int(11) NOT NULL,
  `batch_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tb_assignment_batch`
--

INSERT INTO `tb_assignment_batch` (`id`, `assignment_id`, `batch_id`) VALUES
(1, 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `tb_batch`
--

CREATE TABLE `tb_batch` (
  `b_id` int(11) NOT NULL,
  `title` varchar(150) NOT NULL,
  `closing_date` date NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date NOT NULL,
  `status` tinyint(1) NOT NULL,
  `course_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tb_batch`
--

INSERT INTO `tb_batch` (`b_id`, `title`, `closing_date`, `start_date`, `end_date`, `status`, `course_id`) VALUES
(1, 'Python full stack development batch March 2025', '2025-03-18', '2025-03-20', '2025-05-23', 1, 1),
(2, 'class 1-4 online tuition June 2025', '2025-03-23', '2025-03-25', '2025-09-30', 1, 4),
(3, 'Complete c programming', '2025-03-22', '2025-04-02', '2025-07-01', 1, 3);

-- --------------------------------------------------------

--
-- Table structure for table `tb_batch_teacher`
--

CREATE TABLE `tb_batch_teacher` (
  `id` bigint(20) NOT NULL,
  `batch_id` int(11) NOT NULL,
  `teacher_register_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tb_batch_teacher`
--

INSERT INTO `tb_batch_teacher` (`id`, `batch_id`, `teacher_register_id`) VALUES
(1, 1, 1),
(2, 1, 2),
(3, 1, 4),
(4, 2, 3),
(5, 3, 5);

-- --------------------------------------------------------

--
-- Table structure for table `tb_category`
--

CREATE TABLE `tb_category` (
  `ct_id` int(11) NOT NULL,
  `course_category` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tb_category`
--

INSERT INTO `tb_category` (`ct_id`, `course_category`) VALUES
(1, 'School class Online Tuition'),
(2, 'Software course');

-- --------------------------------------------------------

--
-- Table structure for table `tb_course`
--

CREATE TABLE `tb_course` (
  `c_id` int(11) NOT NULL,
  `course_name` varchar(100) NOT NULL,
  `description` longtext DEFAULT NULL,
  `fees` double NOT NULL,
  `image` longtext DEFAULT NULL,
  `certificate_course` tinyint(1) NOT NULL,
  `category_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tb_course`
--

INSERT INTO `tb_course` (`c_id`, `course_name`, `description`, `fees`, `image`, `certificate_course`, `category_id`) VALUES
(1, 'Full stack Development in python', 'Learn the basics of python and use it to develop applications. Also learn to work with mongodb in python. This additional language is a value-added skill as python is increasingly in demand for full stack projects. In this module, you will learn:\r\n\r\nPython Installation & Configuration\r\nDeveloping a Python Application\r\nIntroduction to HTML\r\nBrowsers and HTML\r\nntroduction CSS\r\nApplying CSS to HTML\r\nSelectors, Properties and Values\r\nCSS Colors and Backgrounds', 25000, '/media/python.png', 1, 2),
(2, 'Full stack Development in Java', 'A typical Java Full Stack Developer course syllabus covers Java fundamentals, front-end technologies (HTML, CSS, JavaScript, React), back-end development (Spring Boot, Microservices), databases (SQL, NoSQL), and DevOps practices. \r\n. Core Java Fundamentals:\r\nProgramming Basics: Variables, data types, operators, control flow, loops.\r\nObject-Oriented Programming (OOP): Classes, objects, inheritance, polymorphism, abstraction.\r\nData Structures and Algorithms: Arrays, linked lists, stacks, queues, trees, graphs.\r\nException Handling: Understanding and implementing error handling techniques.\r\nMultithreading: Introduction to concurrent programming. \r\nFront-End Development: \r\nHTML, CSS, and JavaScript: Understanding the fundamentals of web page structure, styling, and interactivity.', 30000, '/media/hq.jpg', 1, 2),
(3, 'C Programming', 'Learning C language provides the easiest way to understand high-level languages like Java and Python. It gives coders the basic knowledge of how to start programming and learn about loops, conditional statements and more.\r\n\r\nAnyone who is starting a career in programming or pursuing BCA, MCA, BE/BTech can learn C programming. Do you want to take up a C programming course? Then, you must know what it covers, the programming structure, operators, loops, and more.\r\nIntroduction to C\r\nHistory of C\r\nFeatures of C\r\nApplication areas of C\r\nExecution flow of C program\r\nOther translators\r\nStructure of C program with example\r\nKeywords', 8000, '/media/c.jpg', 1, 2),
(4, 'Class 1-4 online tuition', 'For Kerala\'s state syllabus in classes 1-4, you can find interactive and easy-to-understand textbooks from the SCERT (State Council of Educational Research and Training) for both English and Malayalam mediums, covering subjects like Maths, English, and IC\r\nSCERT Kerala Textbooks for Class 4 Maths has 11 chapters discussed in two textbooks, Part 1 and Part 2. \r\nPart 1 includes 5 chapters, while Part 2 contains 6 chapters. \r\nKey topics include Wheel of Time, More and Less, Adding without Adding, Length and Weight, Data Collection and more. ', 20000, NULL, 0, 1);

-- --------------------------------------------------------

--
-- Table structure for table `tb_course_subjects`
--

CREATE TABLE `tb_course_subjects` (
  `id` bigint(20) NOT NULL,
  `course_id` int(11) NOT NULL,
  `subject_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tb_course_subjects`
--

INSERT INTO `tb_course_subjects` (`id`, `course_id`, `subject_id`) VALUES
(1, 1, 1),
(2, 1, 5),
(3, 1, 6),
(4, 1, 7),
(5, 2, 2),
(6, 2, 5),
(7, 2, 6),
(8, 2, 7),
(9, 3, 3),
(10, 4, 8);

-- --------------------------------------------------------

--
-- Table structure for table `tb_doubts`
--

CREATE TABLE `tb_doubts` (
  `d_id` int(11) NOT NULL,
  `msg` longtext NOT NULL,
  `msg_date` datetime(6) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `receiver_id` int(11) DEFAULT NULL,
  `sender_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tb_doubts`
--

INSERT INTO `tb_doubts` (`d_id`, `msg`, `msg_date`, `status`, `receiver_id`, `sender_id`) VALUES
(1, 'Hello sir', '2025-03-17 17:47:57.452067', 0, 1, 6);

-- --------------------------------------------------------

--
-- Table structure for table `tb_enrollment`
--

CREATE TABLE `tb_enrollment` (
  `e_id` int(11) NOT NULL,
  `amount` double NOT NULL,
  `enrolled_at` datetime(6) NOT NULL,
  `batch_id` int(11) NOT NULL,
  `student_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tb_enrollment`
--

INSERT INTO `tb_enrollment` (`e_id`, `amount`, `enrolled_at`, `batch_id`, `student_id`) VALUES
(1, 25000, '2025-03-17 17:31:10.170753', 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `tb_exam`
--

CREATE TABLE `tb_exam` (
  `e_id` int(11) NOT NULL,
  `title` varchar(200) NOT NULL,
  `topic` longtext DEFAULT NULL,
  `duration` double NOT NULL,
  `status` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `teacher_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tb_exam`
--

INSERT INTO `tb_exam` (`e_id`, `title`, `topic`, `duration`, `status`, `created_at`, `teacher_id`) VALUES
(1, 'Online examination python', 'Python operators', 5, 1, '2025-03-17 17:16:13.550813', 1);

-- --------------------------------------------------------

--
-- Table structure for table `tb_exam_batch`
--

CREATE TABLE `tb_exam_batch` (
  `id` bigint(20) NOT NULL,
  `exam_id` int(11) NOT NULL,
  `batch_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tb_exam_batch`
--

INSERT INTO `tb_exam_batch` (`id`, `exam_id`, `batch_id`) VALUES
(1, 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `tb_feedback`
--

CREATE TABLE `tb_feedback` (
  `f_id` int(11) NOT NULL,
  `feedback_date` datetime(6) NOT NULL,
  `feedback` longtext NOT NULL,
  `student_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `tb_lecture_notes`
--

CREATE TABLE `tb_lecture_notes` (
  `ln_id` int(11) NOT NULL,
  `note` longtext NOT NULL,
  `video_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tb_lecture_notes`
--

INSERT INTO `tb_lecture_notes` (`ln_id`, `note`, `video_id`) VALUES
(1, '/media/Introduction%20to%20Swing.pdf', 4),
(2, '/media/1.pdf', 1),
(3, '/media/Introduction%20to%20Swing_QYpzMYh.pdf', 1);

-- --------------------------------------------------------

--
-- Table structure for table `tb_lesson`
--

CREATE TABLE `tb_lesson` (
  `l_id` int(11) NOT NULL,
  `title` varchar(50) NOT NULL,
  `video` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `subject_id` int(11) DEFAULT NULL,
  `teacher_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tb_lesson`
--

INSERT INTO `tb_lesson` (`l_id`, `title`, `video`, `created_at`, `subject_id`, `teacher_id`) VALUES
(1, 'Python introduction Part-1', '/media/rec2.mp4', '2025-03-17 17:00:46.588963', 1, 1),
(2, 'Python Keyword Part-2', '/media/rec3.mp4', '2025-03-17 17:01:31.511747', 1, 1),
(3, 'Python Operator Part - 3', '/media/rec4.mp4', '2025-03-17 17:02:04.766329', 1, 1),
(4, 'Python Hello world Part - 4', '/media/rec6.mp4', '2025-03-17 17:02:54.890903', 1, 1),
(5, 'HTML introduction Part - 1', '/media/h1.mp4', '2025-03-17 17:23:46.466756', 5, 2),
(6, 'HTML tags Part - 2', '/media/h2.mp4', '2025-03-17 17:24:09.607113', 5, 2),
(7, 'HTML Form tags Part-3', '/media/h3.mp4', '2025-03-17 17:24:39.529981', 5, 2),
(8, 'C introduction Part - 1', '/media/c1%20(1).mp4', '2025-03-17 17:25:57.461238', 3, 5),
(9, 'C Libraries Part - 2', '/media/c1%20(2).mp4', '2025-03-17 17:26:22.759565', 3, 5),
(10, 'C Operators Part - 3', '/media/c1%20(3).mp4', '2025-03-17 17:26:45.653610', 3, 5);

-- --------------------------------------------------------

--
-- Table structure for table `tb_login`
--

CREATE TABLE `tb_login` (
  `login_id` int(11) NOT NULL,
  `username` varchar(20) NOT NULL,
  `password` longtext NOT NULL,
  `user_type` varchar(15) NOT NULL,
  `status` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tb_login`
--

INSERT INTO `tb_login` (`login_id`, `username`, `password`, `user_type`, `status`) VALUES
(1, 'ram12', 'ram12', 'Teacher', 1),
(2, 'sam12', 'sam12', 'Teacher', 1),
(3, 'anu12', 'anu12', 'Teacher', 1),
(4, 'ajith12', 'ajith12', 'Teacher', 1),
(5, 'tom12', 'tom12', 'Teacher', 1),
(6, 'manu12', 'manu12', 'Student', 1);

-- --------------------------------------------------------

--
-- Table structure for table `tb_questions`
--

CREATE TABLE `tb_questions` (
  `q_id` int(11) NOT NULL,
  `question` longtext NOT NULL,
  `optionA` varchar(200) NOT NULL,
  `optionB` varchar(200) NOT NULL,
  `optionC` varchar(200) NOT NULL,
  `optionD` varchar(200) NOT NULL,
  `answer` varchar(200) NOT NULL,
  `exam_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tb_questions`
--

INSERT INTO `tb_questions` (`q_id`, `question`, `optionA`, `optionB`, `optionC`, `optionD`, `answer`, `exam_id`) VALUES
(1, 'What is the result of the expression 4 < 5 and 5 < 6?', 'True', 'False', 'Error', 'None of the above', 'True', 1),
(2, 'What will be the output of the following code?\r\nprint(3 ** 3)', '9', '27', '81', '6', '27', 1),
(3, 'What does the expression not(10 == 10) evaluate to?', 'True', 'False', 'Error', 'None of the above', 'False', 1),
(4, 'Which operator is used to perform logical AND operation?', '&', '&&', 'and', 'AND', 'and', 1),
(5, 'What is the result of the following expression in Python?\r\n3 * \"Hello\"', 'HelloHelloHelloHello', 'Hello 3 times', 'HelloHelloHello', 'Error', 'HelloHelloHelloHello', 1);

-- --------------------------------------------------------

--
-- Table structure for table `tb_student_register`
--

CREATE TABLE `tb_student_register` (
  `sr_id` int(11) NOT NULL,
  `name` varchar(30) NOT NULL,
  `email` varchar(40) NOT NULL,
  `contact_number` bigint(20) NOT NULL,
  `address` longtext NOT NULL,
  `image` longtext DEFAULT NULL,
  `login_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tb_student_register`
--

INSERT INTO `tb_student_register` (`sr_id`, `name`, `email`, `contact_number`, `address`, `image`, `login_id`) VALUES
(1, 'Manu', 'manu@gmail.com', 9054575457, 'Manu bhavan', NULL, 6);

-- --------------------------------------------------------

--
-- Table structure for table `tb_subject`
--

CREATE TABLE `tb_subject` (
  `s_id` int(11) NOT NULL,
  `subject` varchar(80) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tb_subject`
--

INSERT INTO `tb_subject` (`s_id`, `subject`) VALUES
(1, 'Python'),
(2, 'Java'),
(3, 'C'),
(4, 'C++'),
(5, 'HTML'),
(6, 'CSS'),
(7, 'JavaScript'),
(8, 'Maths');

-- --------------------------------------------------------

--
-- Table structure for table `tb_submission`
--

CREATE TABLE `tb_submission` (
  `s_id` int(11) NOT NULL,
  `submitted_date` date NOT NULL,
  `assignment_file` longtext NOT NULL,
  `mark` double DEFAULT NULL,
  `assignment_id` int(11) DEFAULT NULL,
  `student_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tb_submission`
--

INSERT INTO `tb_submission` (`s_id`, `submitted_date`, `assignment_file`, `mark`, `assignment_id`, `student_id`) VALUES
(1, '2025-03-17', '/media/1_izQowKF.pdf', 20, 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `tb_teacher_register`
--

CREATE TABLE `tb_teacher_register` (
  `tr_id` int(11) NOT NULL,
  `name` varchar(30) NOT NULL,
  `email` varchar(40) NOT NULL,
  `contact_number` bigint(20) NOT NULL,
  `address` longtext NOT NULL,
  `experience` varchar(30) NOT NULL,
  `qualification` varchar(50) NOT NULL,
  `image` longtext DEFAULT NULL,
  `login_id` int(11) NOT NULL,
  `subject_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tb_teacher_register`
--

INSERT INTO `tb_teacher_register` (`tr_id`, `name`, `email`, `contact_number`, `address`, `experience`, `qualification`, `image`, `login_id`, `subject_id`) VALUES
(1, 'Ram', 'ram@gmail.com', 9454555457, 'Ram bhavan', '1 year', 'MCA', '/media/profile2.jpg', 1, 1),
(2, 'Sam', 'sam@gmail.com', 9454555457, 'Sam villa', '1 year', 'MCA', '/media/testimonials-4.jpg', 2, 5),
(3, 'Anu', 'anu@gmail.com', 9454555457, 'Anu villa', '1 year', 'Msc Maths', '/media/testimonial-2.jpg', 3, 8),
(4, 'Ajith', 'ajith@gmail.com', 9454555459, 'Ajith bhavan', '1 year', 'MCA', '/media/testimonial-1.jpg', 4, 6),
(5, 'Tom', 'tom@gmail.com', 9454555455, 'Tom villa', '2 year', 'MCA', '/media/testimonial-3.jpg', 5, 3);

--
-- Indexes for dumped tables
--

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
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `tb_answers`
--
ALTER TABLE `tb_answers`
  ADD PRIMARY KEY (`a_id`),
  ADD KEY `tb_Answers_question_id_2af90e72_fk_tb_Questions_q_id` (`question_id`),
  ADD KEY `tb_Answers_student_id_14003d1a_fk_tb_Student_register_sr_id` (`student_id`);

--
-- Indexes for table `tb_assignment`
--
ALTER TABLE `tb_assignment`
  ADD PRIMARY KEY (`a_id`),
  ADD KEY `tb_Assignment_teacher_id_036bfb9a_fk_tb_Teacher_register_tr_id` (`teacher_id`);

--
-- Indexes for table `tb_assignment_batch`
--
ALTER TABLE `tb_assignment_batch`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `tb_Assignment_batch_assignment_id_batch_id_c898d4d6_uniq` (`assignment_id`,`batch_id`),
  ADD KEY `tb_Assignment_batch_batch_id_0d0af580_fk_tb_Batch_b_id` (`batch_id`);

--
-- Indexes for table `tb_batch`
--
ALTER TABLE `tb_batch`
  ADD PRIMARY KEY (`b_id`),
  ADD KEY `tb_Batch_course_id_cfe3f2c0_fk_tb_Course_c_id` (`course_id`);

--
-- Indexes for table `tb_batch_teacher`
--
ALTER TABLE `tb_batch_teacher`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `tb_Batch_teacher_batch_id_teacher_register_id_5c40e56a_uniq` (`batch_id`,`teacher_register_id`),
  ADD KEY `tb_Batch_teacher_teacher_register_id_63263364_fk_tb_Teache` (`teacher_register_id`);

--
-- Indexes for table `tb_category`
--
ALTER TABLE `tb_category`
  ADD PRIMARY KEY (`ct_id`);

--
-- Indexes for table `tb_course`
--
ALTER TABLE `tb_course`
  ADD PRIMARY KEY (`c_id`),
  ADD KEY `tb_Course_category_id_5598ed16_fk_tb_Category_ct_id` (`category_id`);

--
-- Indexes for table `tb_course_subjects`
--
ALTER TABLE `tb_course_subjects`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `tb_Course_subjects_course_id_subject_id_d984be96_uniq` (`course_id`,`subject_id`),
  ADD KEY `tb_Course_subjects_subject_id_305d663d_fk_tb_Subject_s_id` (`subject_id`);

--
-- Indexes for table `tb_doubts`
--
ALTER TABLE `tb_doubts`
  ADD PRIMARY KEY (`d_id`),
  ADD KEY `tb_Doubts_receiver_id_11ddaa87_fk_tb_Login_login_id` (`receiver_id`),
  ADD KEY `tb_Doubts_sender_id_889c8ce2_fk_tb_Login_login_id` (`sender_id`);

--
-- Indexes for table `tb_enrollment`
--
ALTER TABLE `tb_enrollment`
  ADD PRIMARY KEY (`e_id`),
  ADD KEY `tb_Enrollment_batch_id_02a28b5d_fk_tb_Batch_b_id` (`batch_id`),
  ADD KEY `tb_Enrollment_student_id_2d3c397b_fk_tb_Student_register_sr_id` (`student_id`);

--
-- Indexes for table `tb_exam`
--
ALTER TABLE `tb_exam`
  ADD PRIMARY KEY (`e_id`),
  ADD KEY `tb_Exam_teacher_id_be174f2f_fk_tb_Teacher_register_tr_id` (`teacher_id`);

--
-- Indexes for table `tb_exam_batch`
--
ALTER TABLE `tb_exam_batch`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `tb_Exam_batch_exam_id_batch_id_86ae6f17_uniq` (`exam_id`,`batch_id`),
  ADD KEY `tb_Exam_batch_batch_id_3d357463_fk_tb_Batch_b_id` (`batch_id`);

--
-- Indexes for table `tb_feedback`
--
ALTER TABLE `tb_feedback`
  ADD PRIMARY KEY (`f_id`),
  ADD KEY `tb_Feedback_student_id_31a77e09_fk_tb_Student_register_sr_id` (`student_id`);

--
-- Indexes for table `tb_lecture_notes`
--
ALTER TABLE `tb_lecture_notes`
  ADD PRIMARY KEY (`ln_id`),
  ADD KEY `tb_Lecture_notes_video_id_42f572fe_fk_tb_Lesson_l_id` (`video_id`);

--
-- Indexes for table `tb_lesson`
--
ALTER TABLE `tb_lesson`
  ADD PRIMARY KEY (`l_id`),
  ADD KEY `tb_Lesson_subject_id_2a5de9d9_fk_tb_Subject_s_id` (`subject_id`),
  ADD KEY `tb_Lesson_teacher_id_c783a121_fk_tb_Teacher_register_tr_id` (`teacher_id`);

--
-- Indexes for table `tb_login`
--
ALTER TABLE `tb_login`
  ADD PRIMARY KEY (`login_id`);

--
-- Indexes for table `tb_questions`
--
ALTER TABLE `tb_questions`
  ADD PRIMARY KEY (`q_id`),
  ADD KEY `tb_Questions_exam_id_4161400a_fk_tb_Exam_e_id` (`exam_id`);

--
-- Indexes for table `tb_student_register`
--
ALTER TABLE `tb_student_register`
  ADD PRIMARY KEY (`sr_id`),
  ADD KEY `tb_Student_register_login_id_b494b13d_fk_tb_Login_login_id` (`login_id`);

--
-- Indexes for table `tb_subject`
--
ALTER TABLE `tb_subject`
  ADD PRIMARY KEY (`s_id`);

--
-- Indexes for table `tb_submission`
--
ALTER TABLE `tb_submission`
  ADD PRIMARY KEY (`s_id`),
  ADD KEY `tb_Submission_assignment_id_33df87b2_fk_tb_Assignment_a_id` (`assignment_id`),
  ADD KEY `tb_Submission_student_id_1303ea43_fk_tb_Student_register_sr_id` (`student_id`);

--
-- Indexes for table `tb_teacher_register`
--
ALTER TABLE `tb_teacher_register`
  ADD PRIMARY KEY (`tr_id`),
  ADD KEY `tb_Teacher_register_login_id_13f6f515_fk_tb_Login_login_id` (`login_id`),
  ADD KEY `tb_Teacher_register_subject_id_87b521fc_fk_tb_Subject_s_id` (`subject_id`);

--
-- AUTO_INCREMENT for dumped tables
--

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=93;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT for table `tb_answers`
--
ALTER TABLE `tb_answers`
  MODIFY `a_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `tb_assignment`
--
ALTER TABLE `tb_assignment`
  MODIFY `a_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `tb_assignment_batch`
--
ALTER TABLE `tb_assignment_batch`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `tb_batch`
--
ALTER TABLE `tb_batch`
  MODIFY `b_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `tb_batch_teacher`
--
ALTER TABLE `tb_batch_teacher`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `tb_category`
--
ALTER TABLE `tb_category`
  MODIFY `ct_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `tb_course`
--
ALTER TABLE `tb_course`
  MODIFY `c_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `tb_course_subjects`
--
ALTER TABLE `tb_course_subjects`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `tb_doubts`
--
ALTER TABLE `tb_doubts`
  MODIFY `d_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `tb_enrollment`
--
ALTER TABLE `tb_enrollment`
  MODIFY `e_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `tb_exam`
--
ALTER TABLE `tb_exam`
  MODIFY `e_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `tb_exam_batch`
--
ALTER TABLE `tb_exam_batch`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `tb_feedback`
--
ALTER TABLE `tb_feedback`
  MODIFY `f_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tb_lecture_notes`
--
ALTER TABLE `tb_lecture_notes`
  MODIFY `ln_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `tb_lesson`
--
ALTER TABLE `tb_lesson`
  MODIFY `l_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `tb_login`
--
ALTER TABLE `tb_login`
  MODIFY `login_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `tb_questions`
--
ALTER TABLE `tb_questions`
  MODIFY `q_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `tb_student_register`
--
ALTER TABLE `tb_student_register`
  MODIFY `sr_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `tb_subject`
--
ALTER TABLE `tb_subject`
  MODIFY `s_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `tb_submission`
--
ALTER TABLE `tb_submission`
  MODIFY `s_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `tb_teacher_register`
--
ALTER TABLE `tb_teacher_register`
  MODIFY `tr_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Constraints for dumped tables
--

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
-- Constraints for table `tb_answers`
--
ALTER TABLE `tb_answers`
  ADD CONSTRAINT `tb_Answers_question_id_2af90e72_fk_tb_Questions_q_id` FOREIGN KEY (`question_id`) REFERENCES `tb_questions` (`q_id`),
  ADD CONSTRAINT `tb_Answers_student_id_14003d1a_fk_tb_Student_register_sr_id` FOREIGN KEY (`student_id`) REFERENCES `tb_student_register` (`sr_id`);

--
-- Constraints for table `tb_assignment`
--
ALTER TABLE `tb_assignment`
  ADD CONSTRAINT `tb_Assignment_teacher_id_036bfb9a_fk_tb_Teacher_register_tr_id` FOREIGN KEY (`teacher_id`) REFERENCES `tb_teacher_register` (`tr_id`);

--
-- Constraints for table `tb_assignment_batch`
--
ALTER TABLE `tb_assignment_batch`
  ADD CONSTRAINT `tb_Assignment_batch_assignment_id_785cdcab_fk_tb_Assignment_a_id` FOREIGN KEY (`assignment_id`) REFERENCES `tb_assignment` (`a_id`),
  ADD CONSTRAINT `tb_Assignment_batch_batch_id_0d0af580_fk_tb_Batch_b_id` FOREIGN KEY (`batch_id`) REFERENCES `tb_batch` (`b_id`);

--
-- Constraints for table `tb_batch`
--
ALTER TABLE `tb_batch`
  ADD CONSTRAINT `tb_Batch_course_id_cfe3f2c0_fk_tb_Course_c_id` FOREIGN KEY (`course_id`) REFERENCES `tb_course` (`c_id`);

--
-- Constraints for table `tb_batch_teacher`
--
ALTER TABLE `tb_batch_teacher`
  ADD CONSTRAINT `tb_Batch_teacher_batch_id_196a8133_fk_tb_Batch_b_id` FOREIGN KEY (`batch_id`) REFERENCES `tb_batch` (`b_id`),
  ADD CONSTRAINT `tb_Batch_teacher_teacher_register_id_63263364_fk_tb_Teache` FOREIGN KEY (`teacher_register_id`) REFERENCES `tb_teacher_register` (`tr_id`);

--
-- Constraints for table `tb_course`
--
ALTER TABLE `tb_course`
  ADD CONSTRAINT `tb_Course_category_id_5598ed16_fk_tb_Category_ct_id` FOREIGN KEY (`category_id`) REFERENCES `tb_category` (`ct_id`);

--
-- Constraints for table `tb_course_subjects`
--
ALTER TABLE `tb_course_subjects`
  ADD CONSTRAINT `tb_Course_subjects_course_id_eb32f787_fk_tb_Course_c_id` FOREIGN KEY (`course_id`) REFERENCES `tb_course` (`c_id`),
  ADD CONSTRAINT `tb_Course_subjects_subject_id_305d663d_fk_tb_Subject_s_id` FOREIGN KEY (`subject_id`) REFERENCES `tb_subject` (`s_id`);

--
-- Constraints for table `tb_doubts`
--
ALTER TABLE `tb_doubts`
  ADD CONSTRAINT `tb_Doubts_receiver_id_11ddaa87_fk_tb_Login_login_id` FOREIGN KEY (`receiver_id`) REFERENCES `tb_login` (`login_id`),
  ADD CONSTRAINT `tb_Doubts_sender_id_889c8ce2_fk_tb_Login_login_id` FOREIGN KEY (`sender_id`) REFERENCES `tb_login` (`login_id`);

--
-- Constraints for table `tb_enrollment`
--
ALTER TABLE `tb_enrollment`
  ADD CONSTRAINT `tb_Enrollment_batch_id_02a28b5d_fk_tb_Batch_b_id` FOREIGN KEY (`batch_id`) REFERENCES `tb_batch` (`b_id`),
  ADD CONSTRAINT `tb_Enrollment_student_id_2d3c397b_fk_tb_Student_register_sr_id` FOREIGN KEY (`student_id`) REFERENCES `tb_student_register` (`sr_id`);

--
-- Constraints for table `tb_exam`
--
ALTER TABLE `tb_exam`
  ADD CONSTRAINT `tb_Exam_teacher_id_be174f2f_fk_tb_Teacher_register_tr_id` FOREIGN KEY (`teacher_id`) REFERENCES `tb_teacher_register` (`tr_id`);

--
-- Constraints for table `tb_exam_batch`
--
ALTER TABLE `tb_exam_batch`
  ADD CONSTRAINT `tb_Exam_batch_batch_id_3d357463_fk_tb_Batch_b_id` FOREIGN KEY (`batch_id`) REFERENCES `tb_batch` (`b_id`),
  ADD CONSTRAINT `tb_Exam_batch_exam_id_6aa4065b_fk_tb_Exam_e_id` FOREIGN KEY (`exam_id`) REFERENCES `tb_exam` (`e_id`);

--
-- Constraints for table `tb_feedback`
--
ALTER TABLE `tb_feedback`
  ADD CONSTRAINT `tb_Feedback_student_id_31a77e09_fk_tb_Student_register_sr_id` FOREIGN KEY (`student_id`) REFERENCES `tb_student_register` (`sr_id`);

--
-- Constraints for table `tb_lecture_notes`
--
ALTER TABLE `tb_lecture_notes`
  ADD CONSTRAINT `tb_Lecture_notes_video_id_42f572fe_fk_tb_Lesson_l_id` FOREIGN KEY (`video_id`) REFERENCES `tb_lesson` (`l_id`);

--
-- Constraints for table `tb_lesson`
--
ALTER TABLE `tb_lesson`
  ADD CONSTRAINT `tb_Lesson_subject_id_2a5de9d9_fk_tb_Subject_s_id` FOREIGN KEY (`subject_id`) REFERENCES `tb_subject` (`s_id`),
  ADD CONSTRAINT `tb_Lesson_teacher_id_c783a121_fk_tb_Teacher_register_tr_id` FOREIGN KEY (`teacher_id`) REFERENCES `tb_teacher_register` (`tr_id`);

--
-- Constraints for table `tb_questions`
--
ALTER TABLE `tb_questions`
  ADD CONSTRAINT `tb_Questions_exam_id_4161400a_fk_tb_Exam_e_id` FOREIGN KEY (`exam_id`) REFERENCES `tb_exam` (`e_id`);

--
-- Constraints for table `tb_student_register`
--
ALTER TABLE `tb_student_register`
  ADD CONSTRAINT `tb_Student_register_login_id_b494b13d_fk_tb_Login_login_id` FOREIGN KEY (`login_id`) REFERENCES `tb_login` (`login_id`);

--
-- Constraints for table `tb_submission`
--
ALTER TABLE `tb_submission`
  ADD CONSTRAINT `tb_Submission_assignment_id_33df87b2_fk_tb_Assignment_a_id` FOREIGN KEY (`assignment_id`) REFERENCES `tb_assignment` (`a_id`),
  ADD CONSTRAINT `tb_Submission_student_id_1303ea43_fk_tb_Student_register_sr_id` FOREIGN KEY (`student_id`) REFERENCES `tb_student_register` (`sr_id`);

--
-- Constraints for table `tb_teacher_register`
--
ALTER TABLE `tb_teacher_register`
  ADD CONSTRAINT `tb_Teacher_register_login_id_13f6f515_fk_tb_Login_login_id` FOREIGN KEY (`login_id`) REFERENCES `tb_login` (`login_id`),
  ADD CONSTRAINT `tb_Teacher_register_subject_id_87b521fc_fk_tb_Subject_s_id` FOREIGN KEY (`subject_id`) REFERENCES `tb_subject` (`s_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
