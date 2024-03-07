-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 22-02-2024 a las 01:33:04
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `battlewayweb1`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `auth_permission`
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
(25, 'Can add tournament', 7, 'add_tournament'),
(26, 'Can change tournament', 7, 'change_tournament'),
(27, 'Can delete tournament', 7, 'delete_tournament'),
(28, 'Can view tournament', 7, 'view_tournament'),
(29, 'Can add user', 8, 'add_user'),
(30, 'Can change user', 8, 'change_user'),
(31, 'Can delete user', 8, 'delete_user'),
(32, 'Can view user', 8, 'view_user'),
(33, 'Can add game', 9, 'add_game'),
(34, 'Can change game', 9, 'change_game'),
(35, 'Can delete game', 9, 'delete_game'),
(36, 'Can view game', 9, 'view_game'),
(37, 'Can add player', 8, 'add_player'),
(38, 'Can change player', 8, 'change_player'),
(39, 'Can delete player', 8, 'delete_player'),
(40, 'Can view player', 8, 'view_player');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user`
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
-- Volcado de datos para la tabla `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$720000$YmeRBbo5WfExmtPnkTJFVU$3QWcygdU4UcZEckldRp+2M89oPZv/rYgBnSFEHdvjM0=', '2024-02-18 05:40:47.258994', 1, 'battlewayadmin', '', '', 'battleway@gmail.com', 1, 1, '2024-02-18 05:40:11.134388');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_admin_log`
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
-- Volcado de datos para la tabla `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2024-02-18 05:43:14.753610', '1', 'Tournament object (1)', 1, '[{\"added\": {}}]', 7, 1),
(2, '2024-02-18 05:49:16.662203', '2', 'Tournament object (2)', 1, '[{\"added\": {}}]', 7, 1),
(3, '2024-02-18 05:57:55.833463', '3', 'Titulo: asd - Fecha: 13-02-2024 Hora: 05:57 AM', 1, '[{\"added\": {}}]', 7, 1),
(4, '2024-02-18 05:58:04.777133', '3', 'Titulo: asd - Fecha: 13-02-2024 Hora: 05:57 AM', 3, '', 7, 1),
(5, '2024-02-19 05:23:06.061308', '7', 'Titulo: Prueba de juegos - Fecha: 13-02-2024 Hora: 12:00 PM', 2, '[{\"changed\": {\"fields\": [\"Titulo\"]}}]', 7, 1),
(6, '2024-02-19 07:03:12.226681', '1', 'User object (1)', 1, '[{\"added\": {}}]', 8, 1),
(7, '2024-02-19 07:03:41.254268', '1', 'User object (1)', 2, '[]', 8, 1),
(8, '2024-02-19 07:05:00.805499', '2', 'User object (2)', 1, '[{\"added\": {}}]', 8, 1),
(9, '2024-02-19 07:06:24.987761', '3', 'User object (3)', 1, '[{\"added\": {}}]', 8, 1),
(10, '2024-02-19 07:12:07.416398', '4', 'Nombre: sebasPumaGamer - Puntaje: 50', 1, '[{\"added\": {}}]', 8, 1),
(11, '2024-02-19 07:21:19.709744', '5', 'Nombre: Datos nada - Puntaje: 222', 1, '[{\"added\": {}}]', 8, 1),
(12, '2024-02-20 05:05:54.766456', '1', 'Game object (1)', 1, '[{\"added\": {}}]', 9, 1),
(13, '2024-02-20 05:09:18.347220', '2', 'Nombre: Stumble Guys - Empresa: KitkaGames - Scopely', 1, '[{\"added\": {}}]', 9, 1),
(14, '2024-02-20 05:23:18.236205', '1', 'Nombre: Call of Duty - Empresa: Activision - Microsoft', 2, '[{\"changed\": {\"fields\": [\"Detalles\"]}}]', 9, 1),
(15, '2024-02-20 05:28:19.518175', '3', 'Nombre: Free Fire - Empresa: Garena International', 1, '[{\"added\": {}}]', 9, 1),
(16, '2024-02-20 05:28:33.751625', '2', 'Nombre: Stumble Guys - Empresa: KitkaGames - Scopely', 2, '[{\"changed\": {\"fields\": [\"Activo\"]}}]', 9, 1),
(17, '2024-02-20 05:28:42.999482', '3', 'Nombre: Free Fire - Empresa: Garena International', 2, '[{\"changed\": {\"fields\": [\"Activo\"]}}]', 9, 1),
(18, '2024-02-20 05:29:54.864493', '2', 'Nombre: Stumble Guys - Empresa: KitkaGames - Scopely', 2, '[{\"changed\": {\"fields\": [\"Activo\"]}}]', 9, 1),
(19, '2024-02-20 05:30:15.300799', '3', 'Nombre: Free Fire - Empresa: Garena International', 2, '[{\"changed\": {\"fields\": [\"Activo\"]}}]', 9, 1),
(20, '2024-02-20 05:30:48.393958', '3', 'Nombre: Free Fire - Empresa: Garena International', 2, '[{\"changed\": {\"fields\": [\"Activo\"]}}]', 9, 1),
(21, '2024-02-20 05:36:41.781717', '3', 'Nombre: Free Fire - Empresa: Garena International', 2, '[{\"changed\": {\"fields\": [\"Activo\"]}}]', 9, 1),
(22, '2024-02-21 00:50:09.477485', '7', 'Titulo: Call of Duty - Fecha: 13-02-2024 Hora: 12:00 PM', 2, '[{\"changed\": {\"fields\": [\"Titulo\", \"Estado\", \"Imagen\"]}}]', 7, 1),
(23, '2024-02-21 00:50:44.379194', '7', 'Titulo: Call of Duty - Fecha: 13-02-2024 Hora: 12:00 PM', 2, '[{\"changed\": {\"fields\": [\"Juego\"]}}]', 7, 1),
(24, '2024-02-21 00:56:27.322417', '7', 'Titulo: Call of Duty - Fecha: 13-02-2024 Hora: 12:00 PM', 2, '[]', 7, 1),
(25, '2024-02-21 00:56:36.512073', '2', 'Titulo: Torneo explosivo - Fecha: 29-02-2024 Hora: 12:00 PM', 2, '[{\"changed\": {\"fields\": [\"Juego\", \"Estado\", \"Imagen\"]}}]', 7, 1),
(26, '2024-02-21 00:56:45.821508', '1', 'Titulo: Último sobreviviente - Fecha: 23-02-2024 Hora: 06:00 AM', 2, '[{\"changed\": {\"fields\": [\"Juego\", \"Estado\"]}}]', 7, 1),
(27, '2024-02-21 01:19:35.201849', '8', 'Titulo: Torneo dinamita - Fecha: 21-02-2024 Hora: 01:19 AM', 1, '[{\"added\": {}}]', 7, 1),
(28, '2024-02-21 01:19:54.655579', '7', 'Titulo: Call of Duty - Fecha: 13-02-2024 Hora: 12:00 PM', 2, '[{\"changed\": {\"fields\": [\"Estado\"]}}]', 7, 1),
(29, '2024-02-21 01:20:00.782414', '1', 'Titulo: Último sobreviviente - Fecha: 23-02-2024 Hora: 06:00 AM', 2, '[{\"changed\": {\"fields\": [\"Estado\"]}}]', 7, 1),
(30, '2024-02-21 02:04:07.411507', '8', 'Titulo: Torneo dinamita - Fecha: 21-02-2024 Hora: 01:19 AM', 2, '[{\"changed\": {\"fields\": [\"Estado\"]}}]', 7, 1),
(31, '2024-02-21 02:04:34.966992', '2', 'Titulo: Torneo explosivo - Fecha: 29-02-2024 Hora: 12:00 PM', 2, '[{\"changed\": {\"fields\": [\"Estado\"]}}]', 7, 1),
(32, '2024-02-21 02:10:46.602220', '1', 'Titulo: Último sobreviviente - Fecha: 23-02-2024 Hora: 06:00 AM', 2, '[{\"changed\": {\"fields\": [\"Imagen\"]}}]', 7, 1),
(33, '2024-02-21 03:55:22.546286', '7', 'Titulo: Call of Duty - Fecha: 13-02-2024 Hora: 12:00 PM', 2, '[{\"changed\": {\"fields\": [\"Estado\"]}}]', 7, 1),
(34, '2024-02-21 04:43:58.544123', '2', 'Titulo: Torneo explosivo - Fecha: 29-02-2024 Hora: 12:00 PM', 2, '[{\"changed\": {\"fields\": [\"Estado\"]}}]', 7, 1),
(35, '2024-02-21 04:54:23.917845', '7', 'Titulo: Call of Duty - Fecha: 13-02-2024 Hora: 12:00 PM', 2, '[{\"changed\": {\"fields\": [\"Estado\"]}}]', 7, 1),
(36, '2024-02-21 04:54:28.603956', '2', 'Titulo: Torneo explosivo - Fecha: 29-02-2024 Hora: 12:00 PM', 2, '[{\"changed\": {\"fields\": [\"Estado\"]}}]', 7, 1),
(37, '2024-02-21 05:00:09.602220', '3', 'Nombre: Free Fire - Empresa: Garena International', 2, '[{\"changed\": {\"fields\": [\"Activo\"]}}]', 9, 1),
(38, '2024-02-21 05:00:52.417618', '3', 'Nombre: Free Fire - Empresa: Garena International', 2, '[{\"changed\": {\"fields\": [\"Activo\"]}}]', 9, 1),
(39, '2024-02-21 20:08:52.363106', '3', 'Nombre: Free Fire - Empresa: Garena International', 2, '[{\"changed\": {\"fields\": [\"Activo\"]}}]', 9, 1),
(40, '2024-02-21 20:09:02.878830', '3', 'Nombre: Free Fire - Empresa: Garena International', 2, '[{\"changed\": {\"fields\": [\"Activo\"]}}]', 9, 1),
(41, '2024-02-21 20:15:58.815641', '2', 'Titulo: Torneo explosivo - Fecha: 29-02-2024 Hora: 12:00 PM', 2, '[{\"changed\": {\"fields\": [\"Estado\"]}}]', 7, 1),
(42, '2024-02-21 20:16:09.884591', '1', 'Titulo: Último sobreviviente - Fecha: 23-02-2024 Hora: 06:00 AM', 2, '[{\"changed\": {\"fields\": [\"Estado\"]}}]', 7, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session'),
(9, 'tournaments', 'game'),
(8, 'tournaments', 'player'),
(7, 'tournaments', 'tournament');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-02-18 05:33:14.872470'),
(2, 'auth', '0001_initial', '2024-02-18 05:33:15.056876'),
(3, 'admin', '0001_initial', '2024-02-18 05:33:15.101045'),
(4, 'admin', '0002_logentry_remove_auto_add', '2024-02-18 05:33:15.112557'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2024-02-18 05:33:15.117068'),
(6, 'contenttypes', '0002_remove_content_type_name', '2024-02-18 05:33:15.163612'),
(7, 'auth', '0002_alter_permission_name_max_length', '2024-02-18 05:33:15.182324'),
(8, 'auth', '0003_alter_user_email_max_length', '2024-02-18 05:33:15.189889'),
(9, 'auth', '0004_alter_user_username_opts', '2024-02-18 05:33:15.193888'),
(10, 'auth', '0005_alter_user_last_login_null', '2024-02-18 05:33:15.216416'),
(11, 'auth', '0006_require_contenttypes_0002', '2024-02-18 05:33:15.217425'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2024-02-18 05:33:15.222428'),
(13, 'auth', '0008_alter_user_username_max_length', '2024-02-18 05:33:15.237858'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2024-02-18 05:33:15.248368'),
(15, 'auth', '0010_alter_group_name_max_length', '2024-02-18 05:33:15.254884'),
(16, 'auth', '0011_update_proxy_permissions', '2024-02-18 05:33:15.258883'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2024-02-18 05:33:15.266331'),
(18, 'sessions', '0001_initial', '2024-02-18 05:33:15.280844'),
(19, 'tournaments', '0001_initial', '2024-02-18 05:33:15.288863'),
(20, 'tournaments', '0002_alter_tournament_rules', '2024-02-18 05:45:19.018998'),
(21, 'tournaments', '0003_user', '2024-02-19 06:50:06.600794'),
(22, 'tournaments', '0004_alter_user_image', '2024-02-19 07:11:00.074337'),
(23, 'tournaments', '0005_alter_user_image', '2024-02-19 07:20:23.674714'),
(24, 'tournaments', '0006_game', '2024-02-20 04:49:50.742627'),
(25, 'tournaments', '0007_remove_tournament_game_alter_user_points', '2024-02-21 00:17:37.408908'),
(26, 'tournaments', '0008_alter_game_options_tournament_game_and_more', '2024-02-21 00:46:28.060380'),
(27, 'tournaments', '0009_alter_tournament_options_alter_tournament_table', '2024-02-21 00:58:05.000181'),
(28, 'tournaments', '0010_rename_user_player_alter_player_options_and_more', '2024-02-21 01:01:02.000326');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('s8y73a71u58bactm8yamlum45cifx7bg', '.eJxVjMsOwiAQRf-FtSE8yoAu3fcbyMwAUjU0Ke3K-O_apAvd3nPOfYmI21rj1vMSpyQuQovT70bIj9x2kO7YbrPkua3LRHJX5EG7HOeUn9fD_Tuo2Ou3VtoHggzEA7NSFChZyJg8BIVcBrYWNBt71pmDU449uqKKNslwgFLE-wPxcThT:1rbZux:p-sbJFaZQSBbfLOJDdBzVtCGWYsBNAldYb25Heuf2fs', '2024-03-03 05:40:47.260718');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `games`
--

CREATE TABLE `games` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `company` varchar(100) NOT NULL,
  `details` varchar(500) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `image` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `games`
--

INSERT INTO `games` (`id`, `name`, `company`, `details`, `status`, `image`) VALUES
(1, 'Call of Duty', 'Activision - Microsoft', 'Videojuego de disparos en primera persona para la plataforma de Android e IOS.', 1, 'tournaments/images/games/CODM2024_S1.jpg'),
(2, 'Stumble Guys', 'KitkaGames - Scopely', 'Juego multijugador masivo en grupo de derribos donde pueden jugar hasta 32 usuarios en línea.', 1, 'tournaments/images/games/STG.jpg'),
(3, 'Free Fire', 'Garena International', 'Juego de acción y aventura de tipo battle royale que se juega únicamente en tercera persona.', 0, 'tournaments/images/games/FFR.png');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `players`
--

CREATE TABLE `players` (
  `id` int(11) NOT NULL,
  `username` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone` varchar(20) NOT NULL,
  `image` varchar(100) DEFAULT NULL,
  `points` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `players`
--

INSERT INTO `players` (`id`, `username`, `email`, `phone`, `image`, `points`) VALUES
(3, 'andrewgaming', 'andrew@gmail.com', '0987654321', 'tournaments/images/players/profile/profile3.jpg', 10),
(4, 'sebasPumaGamer', 'sebaspuma@gmail.com', '0986397753', 'tournaments/images/players/profile/profile4.jpg', 50),
(6, 'battlewayUser', 'andrew@gmail.com', '0968479276', 'tournaments/images/players/profile/profile3_TaAm5Cn.jpg', 133),
(7, 'battlewayUser', 'dicisdeleo@gmail.com', '0968479276', 'tournaments/images/players/profile/profile_picture.png', 133);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tournaments`
--

CREATE TABLE `tournaments` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `status` varchar(1) NOT NULL,
  `date` date NOT NULL,
  `time` time(6) NOT NULL,
  `max_participants` int(11) NOT NULL,
  `points` int(11) NOT NULL,
  `rules` longtext NOT NULL,
  `url` varchar(1000) NOT NULL,
  `image` varchar(100) DEFAULT NULL,
  `game_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `tournaments`
--

INSERT INTO `tournaments` (`id`, `name`, `status`, `date`, `time`, `max_participants`, `points`, `rules`, `url`, `image`, `game_id`) VALUES
(1, 'Último sobreviviente', 'O', '2024-02-23', '06:00:00.000000', 120, 500, 'Datos de reglamento irian aqui', 'https://cod.mobile.com', 'tournaments/images/CODMP3.jpg', 1),
(2, 'Torneo explosivo', 'C', '2024-02-29', '12:00:00.000000', 100, 250, '¡Bienvenidos al Torneo de Call of Duty Mobile! ????????\r\nAquí están las reglas para garantizar una competencia justa y emocionante. ¡Asegúrense de seguirlas para una experiencia de juego inolvidable! ????\r\n*Reglas Generales:*\r\n???? *Fecha y Hora:* El torneo se llevará a cabo el [Fecha] a las [Hora]. ¡No lleguen tarde!\r\n???? *Trampas y Hacks:* Cualquier forma de trampa resultará en descalificación inmediata. ¡Juego limpio, siempre!\r\n???? *Comunicación:* El uso de micrófonos está permitido, pero eviten contenido ofensivo. ¡Respeto ante todo!\r\n*Formato del Torneo:* [Indicar el modo de juego, por ejemplo, Batalla Royale o Multijugador].\r\n⏰ *Duración de las Partidas:* Cada partida tendrá un límite de tiempo de [X minutos].\r\n???? *Conexión:* Asegúrense de tener una conexión estable. Problemas de conexión no serán responsabilidad del torneo.\r\n???? *Inscripciones:* Cierren 30 minutos antes del inicio del torneo. ¡No se aceptarán inscripciones tardías!\r\n???? *Equipos:* Los equipos deben consistir en [Número de jugadores] jugadores. ¡Asegúrense de tener un nombre de equipo único y creativo!\r\nPuntuación:???? *Sistema de Puntuación:* [Describir el sistema de puntuación, por ejemplo, puntos por eliminación, posición, etc.].\r\n???? *Reporte de Resultados:* Los resultados deben ser reportados inmediatamente después de cada partida.\r\n*Premios:*???????????? *Colocaciones:* Los premios se otorgarán a los equipos con las mejores colocaciones. ¡Grandes recompensas esperan a los campeones!\r\n*????*Streaming en Vivo:* ¡Anima a tu equipo! El streaming en vivo está permitido, pero evita hacer trampa o dar información a otros equipos.\r\n¡Buena Suerte a Todos! Que comiencen las batallas y que los mejores conquisten la victoria. ????????\r\nRecuerden utilizar el canal de [Canal de Comunicación] para cualquier consulta o problema. ¡Diviértanse y que gane el mejor equipo! ????????', 'https://cod.mobile.com', 'tournaments/images/CODMP2.jpg', 1),
(7, 'Call of Duty', 'E', '2024-02-13', '12:00:00.000000', 123, 222, 'Datos de reglamento irian aqui', 'https://cod.mobile.com', 'tournaments/images/CODMP1.jpg', 1),
(8, 'Torneo dinamita', 'O', '2024-02-21', '01:19:18.000000', 123, 123, 'Datos de reglas', 'https://stumble.com', 'tournaments/images/STG1.jpg', 2);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indices de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indices de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indices de la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indices de la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indices de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indices de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indices de la tabla `games`
--
ALTER TABLE `games`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `players`
--
ALTER TABLE `players`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `tournaments`
--
ALTER TABLE `tournaments`
  ADD PRIMARY KEY (`id`),
  ADD KEY `tournaments_tournament_game_id_afed265c_fk_tournaments_game_id` (`game_id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=43;

--
-- AUTO_INCREMENT de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- AUTO_INCREMENT de la tabla `games`
--
ALTER TABLE `games`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `players`
--
ALTER TABLE `players`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `tournaments`
--
ALTER TABLE `tournaments`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Filtros para la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Filtros para la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `tournaments`
--
ALTER TABLE `tournaments`
  ADD CONSTRAINT `tournaments_tournament_game_id_afed265c_fk_tournaments_game_id` FOREIGN KEY (`game_id`) REFERENCES `games` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
