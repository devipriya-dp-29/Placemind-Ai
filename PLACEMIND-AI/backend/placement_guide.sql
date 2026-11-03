-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 17, 2026 at 04:49 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `placement_guide`
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
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add user', 6, 'add_customuser'),
(22, 'Can change user', 6, 'change_customuser'),
(23, 'Can delete user', 6, 'delete_customuser'),
(24, 'Can view user', 6, 'view_customuser'),
(25, 'Can add student profile', 7, 'add_studentprofile'),
(26, 'Can change student profile', 7, 'change_studentprofile'),
(27, 'Can delete student profile', 7, 'delete_studentprofile'),
(28, 'Can view student profile', 7, 'view_studentprofile'),
(29, 'Can add notification', 8, 'add_notification'),
(30, 'Can change notification', 8, 'change_notification'),
(31, 'Can delete notification', 8, 'delete_notification'),
(32, 'Can view notification', 8, 'view_notification'),
(33, 'Can add allowed student', 9, 'add_allowedstudent'),
(34, 'Can change allowed student', 9, 'change_allowedstudent'),
(35, 'Can delete allowed student', 9, 'delete_allowedstudent'),
(36, 'Can view allowed student', 9, 'view_allowedstudent'),
(37, 'Can add company', 10, 'add_company'),
(38, 'Can change company', 10, 'change_company'),
(39, 'Can delete company', 10, 'delete_company'),
(40, 'Can view company', 10, 'view_company'),
(41, 'Can add mock test', 11, 'add_mocktest'),
(42, 'Can change mock test', 11, 'change_mocktest'),
(43, 'Can delete mock test', 11, 'delete_mocktest'),
(44, 'Can view mock test', 11, 'view_mocktest'),
(45, 'Can add placement drive', 12, 'add_placementdrive'),
(46, 'Can change placement drive', 12, 'change_placementdrive'),
(47, 'Can delete placement drive', 12, 'delete_placementdrive'),
(48, 'Can view placement drive', 12, 'view_placementdrive'),
(49, 'Can add mock test result', 13, 'add_mocktestresult'),
(50, 'Can change mock test result', 13, 'change_mocktestresult'),
(51, 'Can delete mock test result', 13, 'delete_mocktestresult'),
(52, 'Can view mock test result', 13, 'view_mocktestresult'),
(53, 'Can add application', 14, 'add_application'),
(54, 'Can change application', 14, 'change_application'),
(55, 'Can delete application', 14, 'delete_application'),
(56, 'Can view application', 14, 'view_application');

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
  `user_id` bigint(20) NOT NULL
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
(4, 'contenttypes', 'contenttype'),
(14, 'placements', 'application'),
(10, 'placements', 'company'),
(11, 'placements', 'mocktest'),
(13, 'placements', 'mocktestresult'),
(12, 'placements', 'placementdrive'),
(5, 'sessions', 'session'),
(9, 'users', 'allowedstudent'),
(6, 'users', 'customuser'),
(8, 'users', 'notification'),
(7, 'users', 'studentprofile');

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
(1, 'contenttypes', '0001_initial', '2026-02-25 11:17:43.968091'),
(2, 'contenttypes', '0002_remove_content_type_name', '2026-02-25 11:17:44.027126'),
(3, 'auth', '0001_initial', '2026-02-25 11:17:44.221446'),
(4, 'auth', '0002_alter_permission_name_max_length', '2026-02-25 11:17:44.272786'),
(5, 'auth', '0003_alter_user_email_max_length', '2026-02-25 11:17:44.278189'),
(6, 'auth', '0004_alter_user_username_opts', '2026-02-25 11:17:44.284092'),
(7, 'auth', '0005_alter_user_last_login_null', '2026-02-25 11:17:44.290553'),
(8, 'auth', '0006_require_contenttypes_0002', '2026-02-25 11:17:44.294170'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2026-02-25 11:17:44.300495'),
(10, 'auth', '0008_alter_user_username_max_length', '2026-02-25 11:17:44.305761'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2026-02-25 11:17:44.310565'),
(12, 'auth', '0010_alter_group_name_max_length', '2026-02-25 11:17:44.324011'),
(13, 'auth', '0011_update_proxy_permissions', '2026-02-25 11:17:44.329692'),
(14, 'auth', '0012_alter_user_first_name_max_length', '2026-02-25 11:17:44.335375'),
(15, 'users', '0001_initial', '2026-02-25 11:17:44.622732'),
(16, 'admin', '0001_initial', '2026-02-25 11:17:44.715787'),
(17, 'admin', '0002_logentry_remove_auto_add', '2026-02-25 11:17:44.722500'),
(18, 'admin', '0003_logentry_add_action_flag_choices', '2026-02-25 11:17:44.730682'),
(19, 'placements', '0001_initial', '2026-02-25 11:17:45.038615'),
(20, 'placements', '0002_mocktest_questions', '2026-02-25 11:17:45.060109'),
(21, 'sessions', '0001_initial', '2026-02-25 11:17:45.096261'),
(22, 'users', '0002_notification', '2026-02-25 11:17:45.160335'),
(23, 'users', '0003_studentprofile_arrears_count_and_more', '2026-02-25 11:17:45.227288'),
(24, 'users', '0004_studentprofile_degree', '2026-02-25 11:17:45.246190'),
(25, 'users', '0005_studentprofile_resume_score_and_more', '2026-02-25 11:17:45.296185'),
(26, 'users', '0006_studentprofile_account_frozen_and_more', '2026-02-25 11:17:45.348527'),
(27, 'users', '0007_allowedstudent', '2026-02-25 11:17:45.391633'),
(28, 'placements', '0003_placementdrive_salary_lpa', '2026-03-12 17:22:23.808626'),
(29, 'users', '0008_remove_studentprofile_placed_and_more', '2026-03-12 17:22:23.957544');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `placements_application`
--

CREATE TABLE `placements_application` (
  `id` bigint(20) NOT NULL,
  `applied_at` datetime(6) NOT NULL,
  `status` varchar(20) NOT NULL,
  `resume` varchar(100) DEFAULT NULL,
  `drive_id` bigint(20) NOT NULL,
  `student_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `placements_company`
--

CREATE TABLE `placements_company` (
  `id` bigint(20) NOT NULL,
  `name` varchar(255) NOT NULL,
  `description` longtext NOT NULL,
  `website` varchar(200) NOT NULL,
  `logo` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `placements_mocktest`
--

CREATE TABLE `placements_mocktest` (
  `id` bigint(20) NOT NULL,
  `title` varchar(255) NOT NULL,
  `description` longtext NOT NULL,
  `total_marks` int(11) NOT NULL,
  `duration_minutes` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `drive_id` bigint(20) DEFAULT NULL,
  `questions` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL CHECK (json_valid(`questions`))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `placements_mocktest`
--

INSERT INTO `placements_mocktest` (`id`, `title`, `description`, `total_marks`, `duration_minutes`, `created_at`, `drive_id`, `questions`) VALUES
(4, 'Technical Skill Assessment (AI-Trained)', 'Comprehensive test covering DS, OOP, React, and SQL based on training datasets.', 100, 30, '2026-03-17 15:44:27.144419', NULL, '[{\"id\": 1, \"question\": \"What is the time complexity of searching an element in a balanced Binary Search Tree?\", \"options\": [\"O(n)\", \"O(log n)\", \"O(n log n)\", \"O(1)\"], \"correctIndex\": 1, \"skills\": [\"Data Structures\", \"Algorithms\"]}, {\"id\": 2, \"question\": \"Which of the following is NOT a primary principle of Object-Oriented Programming?\", \"options\": [\"Encapsulation\", \"Inheritance\", \"Polymorphism\", \"Compilation\"], \"correctIndex\": 3, \"skills\": [\"Java\", \"OOP\", \"Python\"]}, {\"id\": 3, \"question\": \"In React, which hook is used to handle side effects?\", \"options\": [\"useState\", \"useContext\", \"useEffect\", \"useReducer\"], \"correctIndex\": 2, \"skills\": [\"React\", \"JavaScript\", \"Frontend\"]}, {\"id\": 4, \"question\": \"What does SQL stand for?\", \"options\": [\"Structured Query Language\", \"Simple Query Language\", \"Statement Query Language\", \"Sequential Query Language\"], \"correctIndex\": 0, \"skills\": [\"SQL\", \"Database\"]}, {\"id\": 5, \"question\": \"Which HTTP method is typically used to update an existing resource?\", \"options\": [\"GET\", \"POST\", \"PUT\", \"DELETE\"], \"correctIndex\": 2, \"skills\": [\"Networking\", \"Web Development\"]}, {\"id\": 6, \"question\": \"What is the purpose of the \'git clone\' command?\", \"options\": [\"Create a new branch\", \"Copy a repository from a remote server\", \"Commit changes\", \"Merging branches\"], \"correctIndex\": 1, \"skills\": [\"Git\", \"Version Control\"]}, {\"id\": 7, \"question\": \"Which of these is a Python data type that is immutable?\", \"options\": [\"List\", \"Dictionary\", \"Set\", \"Tuple\"], \"correctIndex\": 3, \"skills\": [\"Python\"]}, {\"id\": 8, \"question\": \"What is a \'Primary Key\' in a database table?\", \"options\": [\"A key that opens the database\", \"A unique identifier for each record\", \"A secondary index\", \"A foreign relationship\"], \"correctIndex\": 1, \"skills\": [\"Database\", \"SQL\"]}, {\"id\": 9, \"question\": \"Which sorting algorithm has the best average time complexity?\", \"options\": [\"Bubble Sort\", \"Insertion Sort\", \"Merge Sort\", \"Selection Sort\"], \"correctIndex\": 2, \"skills\": [\"Algorithms\", \"Data Structures\"]}, {\"id\": 10, \"question\": \"What is the result of 10 + \'5\' in JavaScript?\", \"options\": [\"15\", \"105\", \"Error\", \"NaN\"], \"correctIndex\": 1, \"skills\": [\"JavaScript\", \"Frontend\"]}, {\"id\": 11, \"question\": \"Which of the following is a NoSQL database?\", \"options\": [\"MySQL\", \"PostgreSQL\", \"MongoDB\", \"Oracle\"], \"correctIndex\": 2, \"skills\": [\"Database\", \"Backend\"]}, {\"id\": 12, \"question\": \"What does CSS stand for?\", \"options\": [\"Creative Style Sheets\", \"Cascading Style Sheets\", \"Computer Style Sheets\", \"Colorful Style Sheets\"], \"correctIndex\": 1, \"skills\": [\"CSS\", \"Frontend\"]}, {\"id\": 13, \"question\": \"Which company developed Java?\", \"options\": [\"Microsoft\", \"Sun Microsystems\", \"Apple\", \"Google\"], \"correctIndex\": 1, \"skills\": [\"Java\"]}, {\"id\": 14, \"question\": \"In Python, how do you start a block of code?\", \"options\": [\"{\", \"(\", \":\", \"[\"], \"correctIndex\": 2, \"skills\": [\"Python\", \"Algorithms\"]}]'),
(5, 'Quantitative Aptitude & Reasoning', 'Evaluate basic math, logic, and problem solving skills.', 50, 20, '2026-03-17 15:44:27.149959', NULL, '[{\"id\": 1, \"question\": \"If a train 120m long passes a pole in 6 seconds, what is its speed?\", \"options\": [\"72 km/hr\", \"60 km/hr\", \"54 km/hr\", \"45 km/hr\"], \"correctIndex\": 0, \"skills\": [\"Aptitude\", \"Math\"]}, {\"id\": 2, \"question\": \"What is the next number in the series: 2, 6, 12, 20, 30, ...?\", \"options\": [\"40\", \"42\", \"44\", \"48\"], \"correctIndex\": 1, \"skills\": [\"Reasoning\", \"Pattern\"]}, {\"id\": 3, \"question\": \"If NOIDA is written as OPJEB, then what will be the code for DELHI?\", \"options\": [\"EFMID\", \"EFMIJ\", \"EFMIK\", \"EFMIM\"], \"correctIndex\": 1, \"skills\": [\"Reasoning\", \"Logic\"]}]'),
(6, 'Frontend Web Development', 'Assess HTML, CSS, JavaScript, and framework knowledge like React.', 60, 25, '2026-03-17 15:44:27.157807', NULL, '[{\"id\": 1, \"question\": \"What does DOM stand for in JavaScript?\", \"options\": [\"Document Object Mechanism\", \"Document Oriented Model\", \"Document Object Model\", \"Dynamic Object Model\"], \"correctIndex\": 2, \"skills\": [\"JavaScript\", \"Frontend\"]}, {\"id\": 2, \"question\": \"In CSS, how to make the text bold?\", \"options\": [\"font-weight: bold\", \"style: bold\", \"font: bold\", \"text-style: bold\"], \"correctIndex\": 0, \"skills\": [\"CSS\", \"Frontend\"]}]');

-- --------------------------------------------------------

--
-- Table structure for table `placements_mocktestresult`
--

CREATE TABLE `placements_mocktestresult` (
  `id` bigint(20) NOT NULL,
  `score` double NOT NULL,
  `taken_at` datetime(6) NOT NULL,
  `student_id` bigint(20) NOT NULL,
  `test_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `placements_placementdrive`
--

CREATE TABLE `placements_placementdrive` (
  `id` bigint(20) NOT NULL,
  `job_role` varchar(255) NOT NULL,
  `description` longtext NOT NULL,
  `eligibility_criteria` longtext NOT NULL,
  `min_cgpa` double NOT NULL,
  `allowed_branches` varchar(255) NOT NULL,
  `max_arrears` int(11) NOT NULL,
  `salary_package` varchar(100) NOT NULL,
  `deadline` datetime(6) NOT NULL,
  `interview_date` datetime(6) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `company_id` bigint(20) NOT NULL,
  `salary_lpa` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `users_allowedstudent`
--

CREATE TABLE `users_allowedstudent` (
  `id` bigint(20) NOT NULL,
  `student_name` varchar(255) DEFAULT NULL,
  `email` varchar(254) NOT NULL,
  `roll_number` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users_allowedstudent`
--

INSERT INTO `users_allowedstudent` (`id`, `student_name`, `email`, `roll_number`) VALUES
(68, 'Aarthi R', 'aarthirajaguru63@gmail.com', '142222104001'),
(69, 'Abarna', 'abarnam2004@gmail.com', '142222104002'),
(70, 'Abdul Basith A', 'abdulbasith0824@gmail.com', '142222104003'),
(71, 'P ABISHEK', '26abishek05@gmail.com', '142222104005'),
(72, 'Abinaya C', 'abinayachinnadurai24@gmail.com', '142222104006'),
(73, 'ABINESH  S', 'abinesh.sokk2005@gmail.com', '142222104008'),
(74, 'ADHIYAMAAN E', 'adhielango0907@gmail.com', '142222104011'),
(75, 'Aishwariya.P.S', 'aishwariyaps24@gmail.com', '142222104012'),
(76, 'Ajay B.S.', 'bsajay111@gmail.com', '142222104013'),
(77, 'Arun Pandian J', 'arunmag123ar@gmail.com', '142222104022'),
(78, 'Devipriya N', 'devipriya290903@gmail.com', '142222104036'),
(79, 'Dharani D', 'dharu2464@gmail.com', '142222104038'),
(80, 'DHARSHINI PRIYA S', 'dharshinipriya2255@gmail.com', '142222104041'),
(81, 'M.Dhinesh', 'dhineshmuthusamy81@gmail.com', '142222104043'),
(82, 'Durai Kannan M', 'duraikannanmoorthy@gmail.com', '142222104049'),
(83, 'Durga Devi T', 'durgadevitsrsdd@gmail.com', '142222104050'),
(84, 'P S Geetha Lekshmi', 'psgeethalekshmi3010@gmail.com', '142222104051'),
(85, 'Gokulraj j', 'gokulrajjsgm@gmail.com', '142222104054'),
(86, 'Hariesh Subramanian M', 'hariesh1745@gmail.com', '142222104060'),
(87, 'JANANI R', 'janani250605@gmail.com', '142222104063'),
(88, 'JAYAPRIYA B', 'jayapriya07032005@gmail.com', '142222104066'),
(89, 'JEEVARAJ S P', 'pandiselvijeevaraj@gmail.com', '142222104069'),
(90, 'KARTHICK S', '17.karthick.03@gmail.com', '142222104073'),
(91, 'KAVEEYA M', 'kaveeyam@gmail.com', '142222104077'),
(92, 'KAVIYA S', 'spkaviya29@gmail.com', '142222104078'),
(93, 'LINGEESHWAR TS', 'lingeeshd@gmail.com', '142222104083'),
(94, 'MADHUMITHA S', 'smadhumitha1309@gmail.com', '142222104087'),
(95, 'MUKESH KUMAR B', 'mukeshkumarb107@gmail.com', '142222104094'),
(96, 'NAUSHEEN BEGUM S', 'nausheen11begum@gmail.com', '142222104096'),
(97, 'NIKHIL B', 'nikhilbalaram03@gmail.com', '142222104099'),
(98, 'PAVITHRA.A', 'pavithraarulanandam@gmail.com', '142222104102'),
(99, 'PRAVEEN RAJ P', 'ppraveenraj1206@gmail.com', '142222104110'),
(100, 'RAGUL P', 'iamragulpushparaj@gmail.com', '142222104113'),
(101, 'RAGUNATH R', 'raguyuva2004@gmail.com', '142222104115'),
(102, 'RAJALAKSHMI V', 'v.uma4547@gmail.com', '142222104116'),
(103, 'RAAJASRI C', 'raajasri2003@gmail.com', '142222104117'),
(104, 'Ramya.V.S', '12c40ramyavs@gmail.com', '142222104118'),
(105, 'RISHAP M', 'rishap.m12@gmail.com', '142222104120'),
(106, 'Rubisha J', 'rubiviji156@gmail.com', '142222104126'),
(107, 'SANDHIYA S', 'sandhiyasuresh2812@gmail.com', '142222104132'),
(108, 'R.Sangeetha', 'sangeethards439@gmail.com', '142222104133'),
(109, 'V. SARITHA', 'sarithavijayakumar24@gmail.com', '142222104139'),
(110, 'SELVAGANAPATHY E', 'selvaganapathy0421g@gmail.com', '142222104142'),
(111, 'SELVAKUMAR S', 'selvakumar20041121@gmail.com', '142222104143'),
(112, 'SHAKTHI K', 'ksakthi960@gmail.com', '142222104144'),
(113, 'SHIVSHARAN A', 'shivsharan.an@gmail.com', '142222104146'),
(114, 'Shravya G', 'shravyagadupuri@gmail.com', '142222104147'),
(115, 'SUBASHINI.K', 'ssuba1722@gmail.com', '142222104153'),
(116, 'SUDHARRSHAN S', 'sudharrshancourse23@gmail.com', '142222104155'),
(117, 'Syed Shifana S', 'syedshifana451@gmail.com', '142222104160'),
(118, 'VENKATESAN S', 'venkatesansettu73@gmail.com', '142222104168'),
(119, 'VIJAYA SHANKARAN', 'mkmk371tvm@gmail.com', '142222104172'),
(120, 'VISHWA KRISH S', 'sanjayvishwa894@gmail.com', '142222104175'),
(121, 'YUVASRI S', 'yuvasrisiva5@gmail.com', '142222104179'),
(122, 'M.Abimanyu', 'abimanyu1452005@gmail.com', '142222128002'),
(123, 'Abinav', 'abinav291@gmail.com', '142222128003'),
(124, 'ABIRAMI R', 'abiramiravi4200@gmail.com', '142222128004'),
(125, 'Alagu Sruthi Bharathi', 'alagusruthibharathi@gmail.com', '142222128007'),
(126, 'S.ASWIN RAJ', 'aswinrajs155@gmail.com', '142222128010'),
(127, 'Janani J', 'janani0509@outlook.com', '142222128014'),
(128, 'Boopathi M', 'boopathikarpagam20@gmail.com', '142222128016'),
(129, 'Jothika k', 'jothikakrishnan39@gmail.com', '142222128028'),
(130, 'Karunakaran S', 'karunakarandeveloper@icloud.com', '142222128030'),
(131, 'Krishna Prasadh K', 'krishnaprasadhf@gmail.com', '142222128031'),
(132, 'SHARIKA J', 'sharikaj003@gmail.com', '142222128049'),
(133, 'Susithra K', 'ksusithra04@gmail.com', '142222128054'),
(134, 'K.Yasmin', 'yasminkasim439@gmail.com', '142222128059');

-- --------------------------------------------------------

--
-- Table structure for table `users_customuser`
--

CREATE TABLE `users_customuser` (
  `id` bigint(20) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `role` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users_customuser`
--

INSERT INTO `users_customuser` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`, `role`) VALUES
(1, 'pbkdf2_sha256$600000$PesNRroTUGAU2Byzoc66O1$4mNx+zfa2GHFb5JjPTanf0ox5KuKhzHbWpNK54iyy5M=', NULL, 1, 'admin', '', '', 'admin@example.com', 1, 1, '2026-02-25 11:18:40.256995', 'admin');

-- --------------------------------------------------------

--
-- Table structure for table `users_customuser_groups`
--

CREATE TABLE `users_customuser_groups` (
  `id` bigint(20) NOT NULL,
  `customuser_id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `users_customuser_user_permissions`
--

CREATE TABLE `users_customuser_user_permissions` (
  `id` bigint(20) NOT NULL,
  `customuser_id` bigint(20) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `users_notification`
--

CREATE TABLE `users_notification` (
  `id` bigint(20) NOT NULL,
  `title` varchar(255) NOT NULL,
  `message` longtext NOT NULL,
  `is_read` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `recipient_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `users_studentprofile`
--

CREATE TABLE `users_studentprofile` (
  `id` bigint(20) NOT NULL,
  `cgpa` double NOT NULL,
  `department` varchar(100) NOT NULL,
  `year_of_study` int(11) NOT NULL,
  `skills` longtext NOT NULL,
  `resume` varchar(100) DEFAULT NULL,
  `user_id` bigint(20) NOT NULL,
  `arrears_count` int(11) NOT NULL,
  `attendance_percentage` double NOT NULL,
  `missed_interviews_count` int(11) NOT NULL,
  `placement_risk` varchar(20) NOT NULL,
  `degree` varchar(100) NOT NULL,
  `resume_score` int(11) NOT NULL,
  `skill_score` int(11) NOT NULL,
  `account_frozen` tinyint(1) NOT NULL,
  `warning_issued` tinyint(1) NOT NULL,
  `aadhaar_number` varchar(12) DEFAULT NULL,
  `pan_card_number` varchar(10) DEFAULT NULL,
  `placed_lpa` double NOT NULL,
  `tenth_percentage` double NOT NULL,
  `twelfth_percentage` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

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
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_users_customuser_id` (`user_id`);

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
-- Indexes for table `placements_application`
--
ALTER TABLE `placements_application`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `placements_application_student_id_drive_id_0373c32a_uniq` (`student_id`,`drive_id`),
  ADD KEY `placements_applicati_drive_id_caaf8a2c_fk_placement` (`drive_id`);

--
-- Indexes for table `placements_company`
--
ALTER TABLE `placements_company`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `placements_mocktest`
--
ALTER TABLE `placements_mocktest`
  ADD PRIMARY KEY (`id`),
  ADD KEY `placements_mocktest_drive_id_dd31e47d_fk_placement` (`drive_id`);

--
-- Indexes for table `placements_mocktestresult`
--
ALTER TABLE `placements_mocktestresult`
  ADD PRIMARY KEY (`id`),
  ADD KEY `placements_mocktestr_student_id_3fa74f7b_fk_users_cus` (`student_id`),
  ADD KEY `placements_mocktestr_test_id_b23b8410_fk_placement` (`test_id`);

--
-- Indexes for table `placements_placementdrive`
--
ALTER TABLE `placements_placementdrive`
  ADD PRIMARY KEY (`id`),
  ADD KEY `placements_placement_company_id_3b5a3129_fk_placement` (`company_id`);

--
-- Indexes for table `users_allowedstudent`
--
ALTER TABLE `users_allowedstudent`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD UNIQUE KEY `roll_number` (`roll_number`);

--
-- Indexes for table `users_customuser`
--
ALTER TABLE `users_customuser`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `users_customuser_groups`
--
ALTER TABLE `users_customuser_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `users_customuser_groups_customuser_id_group_id_76b619e3_uniq` (`customuser_id`,`group_id`),
  ADD KEY `users_customuser_groups_group_id_01390b14_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `users_customuser_user_permissions`
--
ALTER TABLE `users_customuser_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `users_customuser_user_pe_customuser_id_permission_7a7debf6_uniq` (`customuser_id`,`permission_id`),
  ADD KEY `users_customuser_use_permission_id_baaa2f74_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `users_notification`
--
ALTER TABLE `users_notification`
  ADD PRIMARY KEY (`id`),
  ADD KEY `users_notification_recipient_id_0ae2cf8f_fk_users_customuser_id` (`recipient_id`);

--
-- Indexes for table `users_studentprofile`
--
ALTER TABLE `users_studentprofile`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`);

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=57;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- AUTO_INCREMENT for table `placements_application`
--
ALTER TABLE `placements_application`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `placements_company`
--
ALTER TABLE `placements_company`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `placements_mocktest`
--
ALTER TABLE `placements_mocktest`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `placements_mocktestresult`
--
ALTER TABLE `placements_mocktestresult`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `placements_placementdrive`
--
ALTER TABLE `placements_placementdrive`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `users_allowedstudent`
--
ALTER TABLE `users_allowedstudent`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=135;

--
-- AUTO_INCREMENT for table `users_customuser`
--
ALTER TABLE `users_customuser`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `users_customuser_groups`
--
ALTER TABLE `users_customuser_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `users_customuser_user_permissions`
--
ALTER TABLE `users_customuser_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `users_notification`
--
ALTER TABLE `users_notification`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `users_studentprofile`
--
ALTER TABLE `users_studentprofile`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

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
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_users_customuser_id` FOREIGN KEY (`user_id`) REFERENCES `users_customuser` (`id`);

--
-- Constraints for table `placements_application`
--
ALTER TABLE `placements_application`
  ADD CONSTRAINT `placements_applicati_drive_id_caaf8a2c_fk_placement` FOREIGN KEY (`drive_id`) REFERENCES `placements_placementdrive` (`id`),
  ADD CONSTRAINT `placements_applicati_student_id_6c195465_fk_users_cus` FOREIGN KEY (`student_id`) REFERENCES `users_customuser` (`id`);

--
-- Constraints for table `placements_mocktest`
--
ALTER TABLE `placements_mocktest`
  ADD CONSTRAINT `placements_mocktest_drive_id_dd31e47d_fk_placement` FOREIGN KEY (`drive_id`) REFERENCES `placements_placementdrive` (`id`);

--
-- Constraints for table `placements_mocktestresult`
--
ALTER TABLE `placements_mocktestresult`
  ADD CONSTRAINT `placements_mocktestr_student_id_3fa74f7b_fk_users_cus` FOREIGN KEY (`student_id`) REFERENCES `users_customuser` (`id`),
  ADD CONSTRAINT `placements_mocktestr_test_id_b23b8410_fk_placement` FOREIGN KEY (`test_id`) REFERENCES `placements_mocktest` (`id`);

--
-- Constraints for table `placements_placementdrive`
--
ALTER TABLE `placements_placementdrive`
  ADD CONSTRAINT `placements_placement_company_id_3b5a3129_fk_placement` FOREIGN KEY (`company_id`) REFERENCES `placements_company` (`id`);

--
-- Constraints for table `users_customuser_groups`
--
ALTER TABLE `users_customuser_groups`
  ADD CONSTRAINT `users_customuser_gro_customuser_id_958147bf_fk_users_cus` FOREIGN KEY (`customuser_id`) REFERENCES `users_customuser` (`id`),
  ADD CONSTRAINT `users_customuser_groups_group_id_01390b14_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `users_customuser_user_permissions`
--
ALTER TABLE `users_customuser_user_permissions`
  ADD CONSTRAINT `users_customuser_use_customuser_id_5771478b_fk_users_cus` FOREIGN KEY (`customuser_id`) REFERENCES `users_customuser` (`id`),
  ADD CONSTRAINT `users_customuser_use_permission_id_baaa2f74_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

--
-- Constraints for table `users_notification`
--
ALTER TABLE `users_notification`
  ADD CONSTRAINT `users_notification_recipient_id_0ae2cf8f_fk_users_customuser_id` FOREIGN KEY (`recipient_id`) REFERENCES `users_customuser` (`id`);

--
-- Constraints for table `users_studentprofile`
--
ALTER TABLE `users_studentprofile`
  ADD CONSTRAINT `users_studentprofile_user_id_d0e95184_fk_users_customuser_id` FOREIGN KEY (`user_id`) REFERENCES `users_customuser` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
