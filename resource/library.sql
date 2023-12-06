-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: library
-- ------------------------------------------------------
-- Server version	8.0.33

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `tbl_addaccount`
--

DROP TABLE IF EXISTS `tbl_addaccount`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_addaccount` (
  `name` varchar(255) DEFAULT NULL,
  `accountID` varchar(255) DEFAULT NULL,
  `phone` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `isAvail` tinyint DEFAULT '1',
  `limit` int DEFAULT '0',
  KEY `accountID` (`accountID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_addaccount`
--

LOCK TABLES `tbl_addaccount` WRITE;
/*!40000 ALTER TABLE `tbl_addaccount` DISABLE KEYS */;
INSERT INTO `tbl_addaccount` VALUES ('Ma Kwok Yin','1mlztg6uwx','134-3692-7945','makwokyin2015@mail.com',1,0),('Masuda Sara','dM36Zc89q8','74-141-4186','smasuda@icloud.com',1,0),('Liang Anqi','F6RNC3VjBN','(161) 745 1077','anqi5@mail.com',1,0),('Lei Yuning','ABw8E3AMPB','213-071-4361','leiy1024@icloud.com',1,0),('Julia Shaw','a0svyPfhq7','(116) 875 1738','shawjulia@mail.com',1,0),('Lo On Na','O1xgTGniS7','7067 485163','onnalo@gmail.com',1,0),('Yuen Chieh Lun','04rFcYmtRg','(20) 5667 5055','ycl@gmail.com',1,0),('Jack Reyes','OiGO4Vc0aY','11-639-8389','rj104@icloud.com',1,0),('Philip Lee','NIfS3Trsw3','(121) 666 9759','plee724@hotmail.com',1,0),('Mui Chi Yuen','tDvbH09bUa','70-2978-5245','mucy4@outlook.com',1,0),('Ito Eita','AApyFsg1yh','80-7041-5086','eita2014@icloud.com',1,0),('Nakamori Hazuki','kbsJ0tlFaf','80-9928-3732','nakamori89@gmail.com',1,0),('Mike Parker','fwRAQwHLfi','(1865) 20 7890','parker426@icloud.com',1,0),('Shibata Yota','9Eoilojmh3','7293 138107','yotashibata519@outlook.com',1,0),('Sheh Ming','OUWDZebR31','52-250-8567','shehm@mail.com',1,0),('Lei Shihan','XXpXuQKV3S','212-255-1264','shihale90@icloud.com',1,0),('Xue Xiuying','0itCBW9Crm','5128 126935','xuex@icloud.com',1,0),('Sit Chi Ming','3RymwVDjyK','(121) 367 6585','chiming619@mail.com',1,0),('Meng Tsz Ching','b0oOjrqxpQ','330-591-7570','tsme1990@icloud.com',1,0),('Benjamin Howard','cYE87A0EcL','70-9448-1767','benjhoward@gmail.com',1,0),('Barry Garcia','MyhgmLySMP','718-314-5428','barry06@gmail.com',1,0),('William Dunn','ko106c26sK','718-205-8979','dwilliam804@gmail.com',1,0),('Pang Wai Man','P9z7XzBAKR','66-253-6049','waimanpang@gmail.com',1,0),('Sugiyama Kasumi','pVOVLK5oVn','718-269-3813','sugiyama1002@yahoo.com',1,0),('Murakami Kasumi','GGJJ8UbgTq','90-4054-2370','kasumimurakami729@hotmail.com',1,0),('Judith Gray','PvlLqQRIDp','7056 198899','gray98@gmail.com',1,0),('Andrew Baker','0O62ItiIQW','10-4036-7090','andrew7@gmail.com',1,0),('Christine Tran','F8l3I2LT1c','330-063-2792','tc510@yahoo.com',1,0),('Mildred Patterson','20iDEFR6Bi','838-426-4552','mpatterson69@mail.com',1,0),('Laura Reed','8pZF6nnfyK','52-555-2915','laurar7@yahoo.com',1,0),('Jeffrey Castro','DF5KvdM8he','66-157-7546','jeffreyc20@icloud.com',1,0),('Mui Kar Yan','vKCCciu1nV','(121) 781 6969','karyanmu@outlook.com',1,0),('Lui Chi Ming','gxCKRZQS1M','(1865) 90 9108','luicm@icloud.com',1,0),('Meng Yunxi','H4b8PilQRj','(121) 194 5375','yunxi506@icloud.com',1,0),('Shen Anqi','8cVFozKSr0','330-589-0799','anqi09@gmail.com',1,0),('Ono Miu','vhHF8XtpRQ','312-133-2930','onomiu9@icloud.com',1,0),('Bruce Gardner','IUrOrcpnK5','755-885-7383','brucegard@icloud.com',1,0),('Lori Palmer','plzqqm7GqA','212-091-0314','palmlori2@outlook.com',1,0),('Emily Phillips','JtDtBy0L5z','(161) 582 4799','phillipsemily@outlook.com',1,0),('Nakagawa Yuito','42TkyUWUQW','11-418-6136','yuito1955@outlook.com',1,0),('Pang Chun Yu','LaWusd0g2h','163-0282-0786','pang2019@gmail.com',1,0),('Fan Yuning','n1bCQfzoqV','(20) 5024 3278','yuning12@gmail.com',1,0),('Au Sai Wing','RcbLM5sn9r','11-729-2595','ausw76@outlook.com',1,0),('Yamamoto Minato','Mlccc1GeEE','70-5110-6689','myamamoto@gmail.com',1,0),('Wong Sum Wing','OfDJfV4tTQ','5011 926970','sumwingwong42@yahoo.com',1,0),('Monica Clark','Qbev2q9UYG','7512 316370','clarkmonica@yahoo.com',1,0),('Yuen Chiu Wai','xUnAA4HT5n','146-2345-0533','ychiuwai@outlook.com',1,0),('Lin Yunxi','qTrIp891eS','74-562-1917','linyunxi1106@mail.com',1,0),('Aoki Ren','AYz8bVvzZf','52-424-4906','ren2@gmail.com',1,0),('Jeffery Moreno','cwwEpvIOfp','80-8756-9318','jefferymoreno@mail.com',1,0),('Wayne Ward','jahBBmo0yH','28-882-4456','waynewa6@yahoo.com',1,0),('Sit Wai Lam','q8rC1YGLDB','312-512-8616','wailamsit@icloud.com',1,0),('Xie Yunxi','WifWBRmZCm','197-5869-7420','xieyun@outlook.com',1,0),('Du Yuning','tThPnyjgky','614-756-2652','ydu@outlook.com',1,0),('Otsuka Takuya','NPoCJaquX7','163-3170-5455','tots612@icloud.com',1,0),('Mike Lopez','AXjjlfLFze','7506 124090','miklopez@gmail.com',1,0),('Cui Xiaoming','2PUAhcxuKx','70-4158-3816','xiaomingcui@outlook.com',1,0),('Tina Henderson','ZroewMDy3N','172-1270-1337','tinahenderson@yahoo.com',1,0),('He Rui','KlNTTKgmEH','11-658-8986','rui7@gmail.com',1,0),('Xu Xiuying','iqovJxVc6A','5649 112686','xuxiuying@mail.com',1,0),('Fong Yun Fat','6AQ0fI2xOD','80-6336-3497','yffong@gmail.com',1,0),('Chang Lan','CNdR0AQA0E','3-9650-0481','lchang@gmail.com',1,0),('Willie Nguyen','uB6i2bpkvi','10-9428-5141','nguyw@mail.com',1,0),('Lai Ting Fung','Z3d2xPIQvE','90-1044-1743','tingfungla1996@gmail.com',1,0),('Hsuan Tin Wing','4cT6LZBoeT','5130 285958','twhsuan8@gmail.com',1,0),('Taniguchi Aoi','W5AMxsxfig','718-269-1231','aot1204@icloud.com',1,0),('Sheila Allen','gUBDW2xSw3','5360 979795','allen1974@outlook.com',1,0),('Ogawa Kenta','5QZPXTOAW5','90-9396-3079','kenta10@gmail.com',1,0),('Siu Ka Man','O8vnvXCzOd','614-579-9625','skaman2@gmail.com',1,0),('Norman Harris','EQn4OqivvO','312-441-4251','norman76@outlook.com',1,0),('Irene Jones','8XbMhlmJBa','7050 151787','jonesiren@outlook.com',1,0),('Miyamoto Kasumi','UPWJNpyHqG','74-206-9315','kasumim@outlook.com',1,0),('Cynthia Moreno','962suURChs','20-9204-5157','cynthiamoreno06@icloud.com',1,0),('Tong Wai Yee','smESITkd9A','74-676-9431','towaiyee@gmail.com',1,0),('Kinoshita Airi','kcNQrbLhEO','7056 124117','airik@icloud.com',1,0),('Ma Xiaoming','O7h3cN7HEV','330-527-6547','xima@mail.com',1,0),('Kono Ryota','ezl55kwz8W','312-889-7570','ryk@gmail.com',1,0),('Yoshida Ryota','RAckDbMQ6n','312-947-7696','yoshidar@outlook.com',1,0),('Maruyama Mio','a3Nh2CD0No','157-8660-1311','miomar1113@icloud.com',1,0),('Jesse Cole','HfWbyZ2Dbs','167-6628-7670','coleje@gmail.com',1,0),('Mao Anqi','y2VX7sejp3','28-686-6704','maoa1129@hotmail.com',1,0),('Yu Rui','XGiud5zpRw','3-3022-7430','ruiy129@icloud.com',1,0),('Sato Ayano','Rfsxh7OHKh','330-003-0210','saaya41@hotmail.com',1,0),('Xia Yuning','jG2SJL5Mul','7759 598166','xiayuning@mail.com',1,0),('Meng Ming Sze','mUQMVRE99w','(116) 341 3304','mengms5@icloud.com',1,0),('Ogawa Ryota','AfR5oi2B2x','11-699-5530','or1122@gmail.com',1,0),('Nakagawa Ren','xAa39MRRUv','312-686-3094','ren10@mail.com',1,0),('Yu Ziyi','3SOFCX4RI1','5104 772851','ziyiyu@gmail.com',1,0),('Fujiwara Eita','kw0BMpkvgk','312-778-4679','eitafuj@outlook.com',1,0),('Mo Jiehong','GemFiZJWa7','7708 060907','jiehong604@yahoo.com',1,0),('Lau Fu Shing','PSsXy5OzyP','(151) 627 0510','fsl@gmail.com',1,0),('Johnny Hill','RCUqcu7bRg','3-9212-1272','jhil@gmail.com',1,0),('Kwan Chun Yu','tLpxombIpc','66-020-8253','kchunyu@icloud.com',1,0),('Martha Gray','vYcx9GJqJD','21-3969-4553','graymartha67@yahoo.com',1,0),('Hao Shihan','Xy8TARmKuY','21-214-1116','shihhao99@gmail.com',1,0),('Jean Phillips','R3Eht6AThA','(151) 380 2159','philljean@mail.com',1,0),('Tong Ting Fung','64pVoyiLgy','66-890-4780','tftong@outlook.com',1,0),('Tsui Sau Man','8qLbWqGzhN','90-7575-9719','tsui73@gmail.com',1,0),('Nakamura Airi','sOjc7IhCEm','20-6851-8056','airin@outlook.com',1,0),('Yan Zitao','6Zp3oyCD1r','614-764-6873','yan8@outlook.com',1,0);
/*!40000 ALTER TABLE `tbl_addaccount` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_addbook`
--

DROP TABLE IF EXISTS `tbl_addbook`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_addbook` (
  `title` varchar(255) DEFAULT NULL,
  `bookID` varchar(255) DEFAULT NULL,
  `author` varchar(255) DEFAULT NULL,
  `publisher` varchar(255) DEFAULT NULL,
  `isAvail` tinyint DEFAULT '1',
  KEY `bookID` (`bookID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_addbook`
--

LOCK TABLES `tbl_addbook` WRITE;
/*!40000 ALTER TABLE `tbl_addbook` DISABLE KEYS */;
INSERT INTO `tbl_addbook` VALUES ('Mr.','qFWEoxLeVU','Peter Myers','Wing Fat Electronic Limited',1),('Ms.','EIAmwFXf4P','Peter Silva','Ayato Logistic Corporation',0),('Ms.','iw0YXfpX3p','Julia Bennett','Rice Inc.',0),('Ms.','tvsRzqqXRC','James Myers','Fong Kee Property Limited',0),('Miss.','9qSIXGNq89','Wang Zitao','Ma Company Limited',1),('Mrs.','8PMI6us8sT','Chow Ming Sze','Takuya Network Systems Corporation',1),('Prof.','j4oEEIxmLV','Dai Ziyi','Saito Corporation',1),('Miss.','DhnjulIDEN','Yau Wai San','Goto Residence Corporation',1),('Prof.','zK5m5JVgmr','Shimada Nanami','Hsuan Kee Limited',1),('Mr.','FBP9BL8v2L','Brenda Shaw','Tsz Ching Property Limited',1),('Prof.','29ALNAvFuN','Qian Ziyi','Tse\'s Limited',1),('Miss.','9xmN4UQn4L','Bonnie Parker','Hana Network Systems Corporation',1),('Mrs.','rTPpeAtt0S','Saito Takuya','Ayato Pharmaceutical Corporation',1),('Mr.','oMwh1rIedE','Kwong Lik Sun','Patel\'s Pharmaceutical Inc.',1),('Miss.','bhtB27Vj9k','Du Ziyi','Hara Corporation',1),('Miss.','iAiXbEBwra','Mo Sze Yu','Hazuki Corporation',1),('Miss.','CYiCJ8MSb9','Dale Chen','Zitao Company Limited',1),('Mr.','mbILOZ50r8','Gu Zhennan','Mao Kee Industrial Company Limited',1),('Mr.','mEYZxSWTOo','Qin Lu','Tsang\'s Limited',1),('Miss.','YyRya83zTM','Tang Jiehong','Okada Consultants Corporation',1),('Miss.','OtX8zo0Twh','Lui Wai Han','Momoe Toy Corporation',1),('Ms.','mTRKa6lssP','Arimura Momoka','Cheng Kee Pharmaceutical Limited',1),('Prof.','BKPKvGPjsg','Ellen Cruz','Nanami Consultants Corporation',1),('Mrs.','rSTumh8fRC','He Zitao','Tak Wah Network Systems Limited',1),('Ms.','8WGYvVAsBd','Nakajima Ikki','Zhennan Company Limited',1),('Mrs.','8KDZV7HD0y','Paul Gray','Zeng Kee Electronic Company Limited',1),('Miss.','9DoXXpQdwe','Taniguchi Mai','Chen Kee Trading Company Limited',1),('Prof.','kHsGUk7UbP','Crystal Payne','Xiuying Technology Company Limited',1),('Ms.','qhGKJnP7O7','Yao Zhiyuan','Hiu Tung Electronic Limited',1),('Miss.','e78V38ct0s','Shen Zhennan','Matsui Food Corporation',1),('Miss.','igTHQ4uOQg','Brenda Lee','Shihan Company Limited',1),('Mrs.','FEVLUIq66I','Murakami Aoshi','Yang Consultants Company Limited',1),('Mrs.','QTLwsXGaRJ','Randy Palmer','Yang Network Systems Company Limited',1),('Prof.','p2SN01UKD4','Abe Yota','Jones Food LLC',1),('Mrs.','GkKxim6Dkn','Chung Kwok Wing','Vargas Brothers Logistic Inc.',1),('Mrs.','wZUnXPP7PJ','Dawn Romero','Fung Kee Toy Limited',1),('Prof.','x1I6CmLOvt','Morita Misaki','Xiaoming Electronic Company Limited',1),('Miss.','lS77hntYVV','Nicholas Gutierrez','Chi Ming Limited',1),('Mr.','B69tsUHw0V','Mario Campbell','Morgan Inc.',1),('Mr.','Tj5hEhjqZY','Kong Chun Yu','Tang\'s Food Limited',1),('Mr.','Gt46lKlxN6','Wei Rui','Wei Kee Electronic Company Limited',1),('Prof.','jZtqOByiDn','Pak Kwok Kuen','Zhennan Company Limited',1),('Ms.','BnPfCaFjMO','Hou Zhennan','Aaron Inc.',1),('Ms.','T7cBhiUmj0','Carrie White','Han Kee Food Limited',1),('Mr.','uNUqYWO75M','Tsang Cho Yee','Hana Technology Corporation',1),('Prof.','OgFPkX2gXw','Chiang Tsz Ching','Ka Ling Property Limited',1),('Miss.','OTLeNaJhhX','Ota Airi','Yu Kee Electronic Company Limited',1),('Miss.','pMUel3pWCP','Hui Ling Ling','Zou Kee Company Limited',1),('Mrs.','dV5JskEwCw','Hashimoto Momoe','Yin Company Limited',1),('Ms.','8Qn7mfJKbp','Fong Hiu Tung','Lan Toy Company Limited',1),('Miss.','Scn3OiH6eu','Wu Jialun','Koon\'s Telecommunication Limited',1),('Ms.','3D0ZQ6NEXC','Tong Tin Wing','Rin Corporation',1),('Mrs.','9SaN6ky7sT','Shibata Hazuki','Hok Yau Limited',1),('Mr.','ipTX9qkEkx','Lee Wai Han','Olson Brothers Inc.',1),('Ms.','IUlV9fDugD','Ying Lik Sun','Yang Kee Communications Company Limited',1),('Prof.','eWAdVIgod3','Chiba Ayato','Cao Kee Company Limited',1),('Prof.','QRoGyOIOnz','Iwasaki Yamato','Murray Brothers Engineering LLC',1),('Miss.','X1UW9jiACR','George Rose','Shannon Network Systems Inc.',1),('Prof.','Vauo7KxIBo','Christina Hernandez','Lin Engineering Company Limited',1),('Mr.','kxrA5xibRh','Miu Ching Wan','Zhou Kee Company Limited',1),('Prof.','mUgHAv8sLM','Rodney Rice','Yeung Kee Limited',1),('Miss.','ALlWhOdeTG','Endo Aoi','Su Kee Pharmaceutical Company Limited',1),('Mr.','k5wWi8JjsI','Harada Yuna','Yunxi Company Limited',1),('Prof.','dfkXmoOZaU','Keith Perry','Yunxi Industrial Company Limited',1),('Ms.','JDMOVAmJcU','Shen Xiuying','Kennedy\'s LLC',1),('Ms.','yxdXxaRs6b','Kondo Momoe','Wai Yee Technology Limited',1),('Mrs.','nng43T95IO','Deng Anqi','Long Kee Telecommunication Company Limited',1),('Ms.','ikmBV1GlN8','Kato Yuto','Heung Kee Limited',1),('Mrs.','JsHF4T61hK','Ishikawa Mio','Guo Company Limited',1),('Prof.','UYtcABwKcS','Chan Kwok Ming','Song Kee Industrial Company Limited',1),('Mrs.','rNrwWCAs5c','Lau Sau Man','Hikaru Corporation',1),('Mrs.','gidmu6k6Jr','Gu Yuning','Ching Wan Logistic Limited',1),('Mr.','QIg64eOqpM','Steven Ellis','Siu\'s Telecommunication Limited',1),('Miss.','1EYHqdjM5d','Ye Xiaoming','George Engineering Inc.',1),('Ms.','1QCrUmObEK','Shao Rui','Hao Kee Electronic Company Limited',1),('Ms.','CuUGQjQhtb','Dong Rui','Ito Residence Corporation',1),('Mrs.','N2j2jh0PlM','Wendy Watson','Mak\'s Limited',1),('Mr.','aeOhFZdp2Q','Chan Ming','Matsumoto Corporation',1),('Mr.','Ij5TvcQPEz','Kim Ramos','Porter\'s Network Systems Inc.',1),('Mrs.','FxmTOmicNn','Ishida Itsuki','Stephens\'s Pharmaceutical Inc.',1),('Mr.','S0Y96dPmT1','Zhong Zhennan','Che\'s Telecommunication Limited',1),('Miss.','My8dg9whhz','Endo Kenta','Xiuying Technology Company Limited',1),('Mrs.','ZZ2dGlpLPA','Lu Yuning','Kwan Kee Limited',1),('Ms.','Wn489QFr4O','Wei Zhennan','Takeda Pharmaceutical Corporation',1),('Prof.','TzQcGOZSLN','Takagi Daichi','Zitao Communications Company Limited',1),('Prof.','ztDOOm4l2c','Goto Aoshi','Reyes Electronic LLC',1),('Prof.','8XZmTY8uDl','Saito Tsubasa','Hiu Tung Limited',1),('Mrs.','J44kzKD9p8','Patrick Moreno','Theodore Communications Inc.',1),('Prof.','P1QFYJvMFU','Han Ka Ling','Morgan\'s Inc.',1),('Mr.','SnFe95veLi','Tse Chun Yu','Lee\'s LLC',1),('Miss.','Ob3Hh8cLod','Wong Chiu Wai','Willie Inc.',1),('Miss.','n9v1uoJWUK','Nakayama Aoi','Yuning Engineering Company Limited',1),('Mr.','teBZwHdDbJ','Shi Lan','Dai Company Limited',1),('Mr.','fcnTUq9m5F','Yin Ming','Chu Kee Limited',1),('Mr.','uQ2nBxqBHi','Joseph Wilson','Stewart Logistic Inc.',1),('Mrs.','vVhHw7yD8L','Ernest Alexander','Wing Sze Limited',1),('Mrs.','czEP7QWa0l','Heather Simpson','Lan Company Limited',1),('Mr.','nBT1Mf1InS','Cheung Wing Suen','Yuning Technology Company Limited',1),('Miss.','UD5HNoXz9n','John Scott','Tao Trading Company Limited',1),('Miss.','SWbMwfThJE','Matsumoto Mai','Xiaoming Company Limited',1);
/*!40000 ALTER TABLE `tbl_addbook` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_issue`
--

DROP TABLE IF EXISTS `tbl_issue`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_issue` (
  `book_id` varchar(255) DEFAULT NULL,
  `account_id` varchar(255) DEFAULT NULL,
  `issueTime` timestamp NULL DEFAULT NULL,
  `renewCount` int DEFAULT '0',
  KEY `book_id` (`book_id`),
  KEY `account_id` (`account_id`),
  CONSTRAINT `tbl_issue_ibfk_1` FOREIGN KEY (`book_id`) REFERENCES `tbl_addbook` (`bookID`),
  CONSTRAINT `tbl_issue_ibfk_2` FOREIGN KEY (`account_id`) REFERENCES `tbl_addaccount` (`accountID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_issue`
--

LOCK TABLES `tbl_issue` WRITE;
/*!40000 ALTER TABLE `tbl_issue` DISABLE KEYS */;
INSERT INTO `tbl_issue` VALUES ('EIAmwFXf4P','1mlztg6uwx','2023-12-06 12:59:37',0),('iw0YXfpX3p','1mlztg6uwx','2023-12-06 12:59:44',0),('tvsRzqqXRC','1mlztg6uwx','2023-12-06 12:59:52',0);
/*!40000 ALTER TABLE `tbl_issue` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-12-06 21:18:13
