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

 Date: 21/06/2019 15:29:59
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for tbSickSymp
-- ----------------------------
DROP TABLE IF EXISTS `tbSickSymp`;
CREATE TABLE `tbSickSymp` (
  `name` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `question` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL,
  `choice` text COLLATE utf8_unicode_ci,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of tbSickSymp
-- ----------------------------
BEGIN;
INSERT INTO `tbSickSymp` VALUES ('出生年份', '请问您今年多大了?', NULL);
INSERT INTO `tbSickSymp` VALUES ('口臭', '是否会有口臭现象？', '[[\"有\",10],[\"没有\",0],[\"不知道\",5]]');
INSERT INTO `tbSickSymp` VALUES ('多发牙痛', '存在多处疼痛吗？', '[[\"是的\",10],[\"不是\",0]]');
INSERT INTO `tbSickSymp` VALUES ('性别', '请问您的性别?', '[[\"男\",10],[\"女\",0]]');
INSERT INTO `tbSickSymp` VALUES ('敏感性牙痛', '是否会在刷牙或食用冷热酸时牙痛？', '[[\"是的\",10],[\"感觉没有联系\",0]]');
INSERT INTO `tbSickSymp` VALUES ('牙痛史', '以前也会痛吗？', '[[\"是的\",10],[\"不是，最近才感觉痛\",0]]');
INSERT INTO `tbSickSymp` VALUES ('牙龈出血', '有没有出现牙龈出血情况？', '[[\"有\",10],[\"没有\",0]]');
INSERT INTO `tbSickSymp` VALUES ('牙龈红肿', '牙龈是否有红肿现象？', '[[\"有\",10],[\"好像有一点\",5],[\"没有\",0]]');
INSERT INTO `tbSickSymp` VALUES ('长期性牙痛', '一整天都会牙痛吗？', '[[\"是的\",10],[\"偶尔会痛,没什么规律\",5],[\"吃东西或刷牙时候会痛\",0]]');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
