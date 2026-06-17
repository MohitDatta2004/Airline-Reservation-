-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 10, 2024 at 06:08 AM
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
-- Database: `airline_reservation`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(12) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`id`, `username`, `password`) VALUES
(1, 'bobby', 'bobby1234'),
(2, 'donald', 'donald1234'),
(3, 'kretos', 'kretos1234'),
(4, 'trevour', 'trevour1234'),
(5, 'micheal', 'micheal1234');

-- --------------------------------------------------------

--
-- Table structure for table `aircrafts`
--

CREATE TABLE `aircrafts` (
  `id` int(11) NOT NULL,
  `aircraft_id` varchar(20) NOT NULL,
  `model` varchar(20) NOT NULL,
  `sitting_capacity` varchar(20) NOT NULL,
  `engine_type` varchar(20) NOT NULL,
  `other_description` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `aircrafts`
--

INSERT INTO `aircrafts` (`id`, `aircraft_id`, `model`, `sitting_capacity`, `engine_type`, `other_description`) VALUES
(1, 'airliner', '', '', '', ''),
(2, 'AB45', 'Airbus A380', '2000', 'Turbo Jet', ''),
(3, '12', 'Boeing', '200', 'Turbo Jet', 'Not Available'),
(5, 'kmklmlkm', 'lkm', 'lkmlkm', 'Turbo Jet', 'kmlkmlkmlk');

-- --------------------------------------------------------

--
-- Table structure for table `airlines`
--

CREATE TABLE `airlines` (
  `id` int(11) NOT NULL,
  `airline_id` varchar(50) NOT NULL,
  `airline_name` varchar(20) NOT NULL,
  `founded_year` varchar(20) NOT NULL,
  `country` varchar(20) NOT NULL,
  `headquarters` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `airlines`
--

INSERT INTO `airlines` (`id`, `airline_id`, `airline_name`, `founded_year`, `country`, `headquarters`) VALUES
(3, 'QA1', 'Quarter Airways', '1967', 'Saudi Arab', 'Saudi Arab'),
(6, 'SP1', 'Singapore Airlines', '1988', 'Singapore', 'Singapore');

-- --------------------------------------------------------

--
-- Table structure for table `booking`
--

CREATE TABLE `booking` (
  `id` int(11) NOT NULL,
  `flight_number` varchar(20) NOT NULL,
  `airline` varchar(20) NOT NULL,
  `departure_airport` varchar(20) NOT NULL,
  `destination` varchar(50) NOT NULL,
  `date` varchar(20) NOT NULL,
  `aircraft_type` varchar(20) NOT NULL,
  `ticket_price` varchar(20) NOT NULL,
  `number_of_tickets` varchar(20) NOT NULL,
  `total_price` varchar(20) NOT NULL,
  `passenger_name` varchar(20) NOT NULL,
  `date_of_birth` varchar(20) NOT NULL,
  `gender` varchar(20) NOT NULL,
  `passport_id` varchar(20) NOT NULL,
  `contact_number` varchar(20) NOT NULL,
  `passenger_email` varchar(20) NOT NULL,
  `status` varchar(20) NOT NULL,
  `added_by` varchar(20) NOT NULL,
  `created_on` timestamp(6) NOT NULL DEFAULT current_timestamp(6)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `booking`
--

INSERT INTO `booking` (`id`, `flight_number`, `airline`, `departure_airport`, `destination`, `date`, `aircraft_type`, `ticket_price`, `number_of_tickets`, `total_price`, `passenger_name`, `date_of_birth`, `gender`, `passport_id`, `contact_number`, `passenger_email`, `status`, `added_by`, `created_on`) VALUES
(1, '', 'alice', '1234567890', '', 'hsp', 'alice@gmail.com', '', '', '', 'artist', 'F', '2024-08-08', '1489.00', 'amritsar', '', 'delhi', 'bobby@gmail.com', '2024-08-07 11:02:47.568356'),
(2, '1234', 'Quarter Airways', 'Delhi', '', '12-09-9090', 'Airbus A380', '', '', '', 'Demo', '1-09-9060', 'Male', 'PUI4535U', 'Airbus A380', '', 'Pending', 'bobby@gmail.com', '2024-08-07 11:02:47.568356'),
(3, '452459', 'Quarter Airways', 'Delhi', 'America', '12-09-4045', 'Airbus A380', '60000', '2', '120000', 'Demo', '12-09-3457', 'Male', 'K234545FG345', 'Airbus A380', '', 'Pending', 'bobby@gmail.com', '2024-08-07 18:27:19.879236'),
(4, '456634', 'Singapore Airlines', 'Mumbai', 'Russia', '8/16/24', 'Boeing', '200000', '1', '200000', 'Justin', '8/6/24', 'Male', 'SDGF454564RT', 'Boeing', 'justin@gmail.com', 'Confirmed', 'bobby@gmail.com', '2024-08-07 18:40:14.630140'),
(5, '34534', 'Singapore Airlines', 'Madheya Pardesh', 'Dubai', '8/9/24', 'Airbus A380', '5000', '1', '5000', 'Jacob', '8/5/24', 'Male', 'RTEVF45635RT', 'Airbus A380', 'jacob@gmail.com', 'Pending', 'bobby@gmail.com', '2024-08-07 19:31:11.421241');

-- --------------------------------------------------------

--
-- Table structure for table `manager`
--

CREATE TABLE `manager` (
  `id` int(10) NOT NULL,
  `name` varchar(50) NOT NULL,
  `phone_number` varchar(12) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(25) NOT NULL,
  `address` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `manager`
--

INSERT INTO `manager` (`id`, `name`, `phone_number`, `email`, `password`, `address`) VALUES
(1, 'bobby', '123456789', 'bobby@gmail.com', 'bobby1234', 'hoshiarpur'),
(2, 'kretos', '12345678', 'kretos@gmail.com', 'kretos1234', 'hoshiarpur'),
(3, 'trevour', '12345678', 'trevour@gmail.com', 'trevour1234', 'jalandhar'),
(4, 'micheal', '123456789', 'micheal@gmail.com', 'micheal1234', 'los angels'),
(5, '123456789', 'bobby@gmail.', 'bobby1234', '', 'hoshiarpur'),
(8, 'sahil', '399303303', 'sahil@gmail.com', 'sahil1234', 'amritsar'),
(9, 'mohit', '399303308', 'sahil@gmail.com', 'sahil1234', 'amritsar'),
(10, 'karan', '12383383', 'karan@gmail.com', 'karan1234', 'hoshiarpur'),
(14, 'dsfkskdfj', 'jsdflskdjl', 'lkdsj', 'lkdjg', 'lksjglkjdf'),
(15, 'sdflxkmlk', 'slkfmslkm', 'sl', 'slkmv', 'dlksmlkmlkm'),
(16, 'Nia', '5678495678', 'nia@gmail.com', '123456', 'Hoshiarpur'),
(17, 'lkfmsldkmfslmf', 'lmlsmslml', 'lskmglsml', 'lsmglsddml', 'sldmfsdlfmdsklf'),
(18, 'lskmdaslkdmaskl', 'sdlkfmsdlfkm', 'sldfmslfmlk', 'lskfmsldfmsl', 'lsfmsldfmsdlkmf'),
(19, 'sdldkmfsldfm', 'lsmflsdmkf', 'slfmsldfldm', 'lfmslfdmlmf', 'lfmslmflmflk'),
(21, 'lfkmsdlfmsdlk', 'slkfmsldmk', 'lsmslfmsdlm', 'llsdmfldsfsldkm', 'lsdfmsldfmldsmfls');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `aircrafts`
--
ALTER TABLE `aircrafts`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `airlines`
--
ALTER TABLE `airlines`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `booking`
--
ALTER TABLE `booking`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `manager`
--
ALTER TABLE `manager`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `aircrafts`
--
ALTER TABLE `aircrafts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `airlines`
--
ALTER TABLE `airlines`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `booking`
--
ALTER TABLE `booking`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `manager`
--
ALTER TABLE `manager`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
