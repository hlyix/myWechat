/*
 Navicat Premium Data Transfer

 Source Server         : mysql
 Source Server Type    : MySQL
 Source Server Version : 50721
 Source Host           : localhost:3306
 Source Schema         : myWechat

 Target Server Type    : MySQL
 Target Server Version : 50721
 File Encoding         : 65001

 Date: 21/06/2019 15:30:07
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for tbUser
-- ----------------------------
DROP TABLE IF EXISTS `tbUser`;
CREATE TABLE `tbUser` (
  `wcid` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `longitude` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `latitude` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `characteristics` text COLLATE utf8_unicode_ci,
  `state` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `serverStr` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `mode` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`wcid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of tbUser
-- ----------------------------
BEGIN;
INSERT INTO `tbUser` VALUES ('oo1IZ52-Ocjrf6KOfCDvYYyCLL5Y', '112.945511', '28.174850', '{\'长期性牙痛\': 0, \'牙痛史\': 0, \'牙龈红肿\': 5, \'出生年份\': 2001, \'symptom\': [\'牙痛\'], \'牙龈出血\': 0, \'sickness\': [\'深龋\'], \'敏感性牙痛\': 10, \'口臭\': 0, \'多发牙痛\': 0, \'性别\': \'男\'}', '3', '等待定位', '医疗');
INSERT INTO `tbUser` VALUES ('testUser1', '112.95223', '28.180968', '{\'牙痛史\': 0, \'性别\': \'男\', \'牙龈红肿\': 0, \'口臭\': 0, \'牙龈出血\': 5, \'敏感性牙痛\': 5, \'长期性牙痛\': 3, \'出生年份\': 1994, \'多发牙痛\': 0, \'symptom\': [\'牙痛\'], \'sickness\': [\'菌斑性龈炎\']}', '3', '等待定位', '医疗');
INSERT INTO `tbUser` VALUES ('testUser2', '112.945511', '28.174850', '{\'牙龈红肿\': 0, \'牙痛史\': 10, \'性别\': \'女\', \'symptom\': [\'牙痛\'], \'口臭\': 5, \'sickness\': [\'慢性牙髓炎\'], \'敏感性牙痛\': 10, \'长期性牙痛\': 0, \'出生年份\': 1995, \'多发牙痛\': 0, \'牙龈出血\': 0}', '3', '等待定位', '医疗');
INSERT INTO `tbUser` VALUES ('testUser3', '112.945511', '28.174850', '{\'symptom\': [\'牙痛\'], \'牙龈出血\': 0, \'长期性牙痛\': 10, \'口臭\': 0, \'性别\': \'女\', \'牙痛史\': 10, \'sickness\': [\'慢性牙髓炎\'], \'多发牙痛\': 10, \'牙龈红肿\': 0, \'出生年份\': 2003, \'敏感性牙痛\': 0}', '3', '等待定位', '医疗');
INSERT INTO `tbUser` VALUES ('testUser4', '112.945511', '28.174850', '{\'多发牙痛\': 0, \'牙龈红肿\': 0, \'性别\': \'男\', \'长期性牙痛\': 10, \'sickness\': [\'菌斑性龈炎\'], \'出生年份\': 1994, \'牙痛史\': 0, \'口臭\': 10, \'symptom\': [\'牙痛\'], \'牙龈出血\': 5, \'敏感性牙痛\': 0}', '3', '等待定位', '医疗');
INSERT INTO `tbUser` VALUES ('testUser5', '112.95223', '28.174850', '{\'牙痛史\': 0, \'性别\': \'男\', \'长期性牙痛\': 0, \'多发牙痛\': 0, \'sickness\': [\'菌斑性龈炎\'], \'出生年份\': 1994, \'敏感性牙痛\': 5, \'口臭\': 0, \'symptom\': [\'牙痛\'], \'牙龈红肿\': 5, \'牙龈出血\': 5}', '3', '等待定位', '医疗');
INSERT INTO `tbUser` VALUES ('testUser6', '112.95223', '28.180968', '{\'sickness\': [\'牙周脓肿\'], \'口臭\': 0, \'牙龈出血\': 0, \'symptom\': [\'牙痛\'], \'牙痛史\': 0, \'性别\': \'女\', \'长期性牙痛\': 10, \'牙龈红肿\': 5, \'出生年份\': 2004, \'多发牙痛\': 5, \'敏感性牙痛\': 0}', '3', '等待定位', '医疗');
INSERT INTO `tbUser` VALUES ('testUser7', '112.95223', '28.180968', '{\'sickness\': [\'深龋\'], \'牙龈出血\': 0, \'symptom\': [\'牙痛\'], \'多发牙痛\': 3, \'性别\': \'男\', \'牙痛史\': 0, \'出生年份\': 1989, \'口臭\': 0, \'敏感性牙痛\': 10, \'牙龈红肿\': 2, \'长期性牙痛\': 0}', '3', '等待定位', '医疗');
INSERT INTO `tbUser` VALUES ('testUser8', '112.95223', '28.180968', '{\'出生年份\': 1995, \'sickness\': [\'深龋\'], \'牙痛史\': 0, \'symptom\': [\'牙痛\'], \'口臭\': 0, \'多发牙痛\': 0, \'牙龈出血\': 2, \'长期性牙痛\': 2, \'牙龈红肿\': 1, \'性别\': \'男\', \'敏感性牙痛\': 6}', '3', '等待定位', '医疗');
INSERT INTO `tbUser` VALUES ('testUser9', '112.95223', '28.180968', '{\'敏感性牙痛\': 10, \'长期性牙痛\': 5, \'symptom\': [\'牙痛\'], \'牙龈红肿\': 0, \'性别\': \'女\', \'牙痛史\': 10, \'多发牙痛\': 2, \'出生年份\': 1981, \'牙龈出血\': 0, \'sickness\': [\'慢性牙髓炎\'], \'口臭\': 0}', '3', '等待定位', '医疗');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
