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

 Date: 21/06/2019 15:30:17
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for tbUserAction
-- ----------------------------
DROP TABLE IF EXISTS `tbUserAction`;
CREATE TABLE `tbUserAction` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `wcid` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `level` int(2) DEFAULT NULL,
  `object` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  `rate` int(2) DEFAULT NULL,
  `price` float(10,0) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of tbUserAction
-- ----------------------------
BEGIN;
INSERT INTO `tbUserAction` VALUES (2, 'testUser2', 4, '长沙市第四医院 口腔科', 8, NULL);
INSERT INTO `tbUserAction` VALUES (3, 'testUser3', 4, NULL, NULL, NULL);
INSERT INTO `tbUserAction` VALUES (4, 'testUser4', 4, NULL, NULL, NULL);
INSERT INTO `tbUserAction` VALUES (5, 'testUser5', 3, NULL, NULL, NULL);
INSERT INTO `tbUserAction` VALUES (6, 'testUser6', 4, NULL, NULL, NULL);
INSERT INTO `tbUserAction` VALUES (7, 'testUser7', 2, NULL, NULL, NULL);
INSERT INTO `tbUserAction` VALUES (8, 'testUser8', 4, NULL, NULL, NULL);
INSERT INTO `tbUserAction` VALUES (9, 'testUser9', 4, NULL, NULL, NULL);
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
