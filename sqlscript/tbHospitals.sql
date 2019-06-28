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

 Date: 21/06/2019 15:29:44
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for tbHospitals
-- ----------------------------
DROP TABLE IF EXISTS `tbHospitals`;
CREATE TABLE `tbHospitals` (
  `id` int(9) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `scale` int(20) DEFAULT NULL,
  `type` varchar(20) DEFAULT NULL,
  `advantage` varchar(20) DEFAULT NULL,
  `region` varchar(20) DEFAULT NULL,
  `longitude` varchar(20) DEFAULT NULL,
  `latitude` varchar(20) DEFAULT NULL,
  `t1` varchar(20) DEFAULT NULL,
  `t2` varchar(20) DEFAULT NULL,
  `t3` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=73 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of tbHospitals
-- ----------------------------
BEGIN;
INSERT INTO `tbHospitals` VALUES (1, '湘雅医院 ', 32, '综合 ', '综合大型 ', '开福区', '112.991041', '28.217917', NULL, NULL, NULL);
INSERT INTO `tbHospitals` VALUES (2, '湘雅二医院 ', 32, '综合 ', '综合大型 ', '芙蓉区', '113.001942', '28.19169', NULL, NULL, NULL);
INSERT INTO `tbHospitals` VALUES (3, '湘雅三医院', 32, '综合 ', '综合大型 ', '岳麓区', '112.951701', '28.224387', NULL, NULL, NULL);
INSERT INTO `tbHospitals` VALUES (4, '湖南省人民医院', 32, '综合 ', '综合大型 ', '芙蓉区 ', '112.988423', '28.196129', NULL, NULL, NULL);
INSERT INTO `tbHospitals` VALUES (5, '湖南省第二人民医院 ', 32, '综合 ', '0', '雨花区', '112.99255', '28.160819', NULL, NULL, NULL);
INSERT INTO `tbHospitals` VALUES (6, '长沙市中心医院', 32, '综合 ', '0', '天心区', '113.004791', '28.148269', NULL, NULL, NULL);
INSERT INTO `tbHospitals` VALUES (7, '长沙市一医院', 32, '综合 ', '0', '开福区', '112.988817', '28.210389', NULL, NULL, NULL);
INSERT INTO `tbHospitals` VALUES (8, '湖南省人民医院马王堆院区', 32, '综合 ', '0', '芙蓉区', '113.035973', '28.212601', NULL, NULL, NULL);
INSERT INTO `tbHospitals` VALUES (9, '浏阳市中医院', 32, '中医', '0', '浏阳市', '113.635348', '28.149252', NULL, NULL, NULL);
INSERT INTO `tbHospitals` VALUES (10, '湖南省肿瘤医院 ', 32, '肿瘤', '肿瘤', '岳麓区', '112.944065', '28.221332', NULL, NULL, NULL);
INSERT INTO `tbHospitals` VALUES (11, '湖南省中医附一医院', 32, '中医 ', '中医 ', '雨花区', '113.002139', '28.170966', NULL, NULL, NULL);
INSERT INTO `tbHospitals` VALUES (12, '湖南省中医院 ', 32, '中医 ', '中医 ', '开福区', '112.987524', '28.209091', NULL, NULL, NULL);
INSERT INTO `tbHospitals` VALUES (13, '湖南省中医药研究院附属医院', 32, '中医 ', '中医 ', '岳麓区', '112.955636', '28.201475', NULL, NULL, NULL);
INSERT INTO `tbHospitals` VALUES (14, '宁乡市中医医院', 32, '中医 ', '0', '宁乡市', '112.551862', '28.257197', NULL, NULL, NULL);
INSERT INTO `tbHospitals` VALUES (15, '长沙市中医院', 32, '中医', '0', '长沙县', '113.093476', '28.24124', NULL, NULL, NULL);
INSERT INTO `tbHospitals` VALUES (16, '湖南省妇幼保健院', 32, '妇幼', '妇幼', '开福区', '112.989797', '28.213659', NULL, NULL, NULL);
INSERT INTO `tbHospitals` VALUES (17, '长沙市妇幼保健院 ', 32, '妇幼', '0', '雨花区', '113.004798', '28.185612', NULL, NULL, NULL);
INSERT INTO `tbHospitals` VALUES (18, '湖南省儿童医院 ', 32, '儿童', '0', '雨花区', '112.995577', '28.179477', NULL, NULL, NULL);
INSERT INTO `tbHospitals` VALUES (19, '湖南省结核病医院', 32, '传染 ', '传染 ', '岳麓区', '112.94096', '28.215388', NULL, NULL, NULL);
INSERT INTO `tbHospitals` VALUES (20, '长沙市第四医院', 31, '综合 ', '0', '岳麓区', '112.956059', '28.200147', NULL, NULL, NULL);
INSERT INTO `tbHospitals` VALUES (21, '长沙市三医院', 31, '综合 ', '0', '天心区', '112.984055', '28.180952', NULL, NULL, NULL);
INSERT INTO `tbHospitals` VALUES (22, '浏阳市人民医院', 31, '综合 ', '0', '浏阳市', '113.637325', '28.145302', NULL, NULL, NULL);
INSERT INTO `tbHospitals` VALUES (23, '解放军第163医院', 31, '综合 ', '0', '开福区', '113.022882', '28.251045', NULL, NULL, NULL);
INSERT INTO `tbHospitals` VALUES (24, '长沙口腔医院 ', 31, '口腔 ', '口腔 ', '天心区', '112.996642', '28.129836', NULL, NULL, NULL);
INSERT INTO `tbHospitals` VALUES (25, '宁乡市人民医院', 22, '综合 ', '0', '宁乡市', '112.553586', '28.272266', NULL, NULL, NULL);
INSERT INTO `tbHospitals` VALUES (26, '望城县人民医院', 22, '综合 ', '0', '望城区', '112.82037', '28.378274', NULL, NULL, NULL);
INSERT INTO `tbHospitals` VALUES (27, '湖南航天医院 ', 22, '综合 ', '0', '岳麓区', '112.908538', '28.212739', NULL, NULL, NULL);
INSERT INTO `tbHospitals` VALUES (28, '长沙市中医康复医院', 22, '中医 ', '0', '雨花区', '113.00668', '28.191032', NULL, NULL, NULL);
INSERT INTO `tbHospitals` VALUES (29, '浏阳市妇幼保健院', 22, '妇幼', '0', '浏阳市', '113.633585', '28.155612', NULL, NULL, NULL);
INSERT INTO `tbHospitals` VALUES (30, '长沙县妇幼保健院', 22, '妇幼', '0', '长沙县', '113.132937', '28.249793', NULL, NULL, NULL);
INSERT INTO `tbHospitals` VALUES (31, '湖南省地矿医院', 21, '综合 ', '0', '雨花区', '112.998345', '28.157011', NULL, NULL, NULL);
INSERT INTO `tbHospitals` VALUES (32, '湖南省交通医院', 21, '综合 ', '0', '开福区', '112.997388', '28.203922', NULL, NULL, NULL);
INSERT INTO `tbHospitals` VALUES (33, '长沙县第二人民医院', 21, '综合 ', '0', '长沙县', '113.117253', '28.188558', NULL, NULL, NULL);
INSERT INTO `tbHospitals` VALUES (34, '湖南省荣军医院 ', 21, '综合 ', '0', '天心区', '112.98477', '28.031924', NULL, NULL, NULL);
INSERT INTO `tbHospitals` VALUES (35, '长沙县星沙医院 ', 21, '综合 ', '0', '长沙县', '113.095637', '28.251888', NULL, NULL, NULL);
INSERT INTO `tbHospitals` VALUES (36, '长沙县第一人民医院', 21, '综合 ', '0', '长沙县', '113.294722', '28.404097', NULL, NULL, NULL);
INSERT INTO `tbHospitals` VALUES (37, '湖南省财贸医院 ', 21, '综合 ', '0', '天心区', '112.98105', '28.196017', NULL, NULL, NULL);
INSERT INTO `tbHospitals` VALUES (38, '长沙县第三人民医院', 21, '综合 ', '0', '长沙县', '113.294246', '28.404287', NULL, NULL, NULL);
INSERT INTO `tbHospitals` VALUES (39, '中南大学湘雅口腔医院', 21, '口腔 ', '口腔 ', '开福区', '112.990569', '28.219544', NULL, NULL, NULL);
INSERT INTO `tbHospitals` VALUES (40, '宁乡县妇幼保健医院', 21, '妇幼', '0', '宁乡县', '112.55257', '28.244254', NULL, NULL, NULL);
INSERT INTO `tbHospitals` VALUES (41, '浏阳市集里医院', 12, '综合 ', '0', '浏阳市', '113.621059', '28.158604', NULL, NULL, NULL);
INSERT INTO `tbHospitals` VALUES (42, '长沙市天心区大托卫生院 ', 12, '综合 ', '0', '天心区', '112.977662', '28.092009', NULL, NULL, NULL);
INSERT INTO `tbHospitals` VALUES (43, '岳麓区妇幼保健所 ', 12, '妇幼', '0', '岳麓区', '112.961695', '28.210704', NULL, NULL, NULL);
INSERT INTO `tbHospitals` VALUES (44, '长沙市雨花区东山街道社区卫生服务中心', 11, '综合 ', '0', '雨花区', '113.065276', '28.142119', NULL, NULL, NULL);
INSERT INTO `tbHospitals` VALUES (45, '坝塘镇卫生院', 11, '综合 ', '0', '宁乡市', '112.486636', '28.185045', NULL, NULL, NULL);
INSERT INTO `tbHospitals` VALUES (46, '古港镇卫生院', 11, '综合 ', '0', '浏阳市', '113.759591', '28.28493', NULL, NULL, NULL);
INSERT INTO `tbHospitals` VALUES (47, '长沙市岳麓区天顶街道社区卫生服务中心', 0, '综合 ', '0', '岳麓区', '112.8972', '28.202233', NULL, NULL, NULL);
INSERT INTO `tbHospitals` VALUES (48, '坡子街社区卫生服务中心', 0, '综合 ', '0', '天心区', '112.983235', '28.183218', NULL, NULL, NULL);
INSERT INTO `tbHospitals` VALUES (49, '雨花区东塘街道社区卫生服务中心', 0, '综合 ', '0', '雨花区', '112.997766', '28.166857', NULL, NULL, NULL);
INSERT INTO `tbHospitals` VALUES (50, '开福区青竹湖街道社区卫生服务中心', 0, '综合 ', '0', '开福区', '113.014626', '28.257734', NULL, NULL, NULL);
INSERT INTO `tbHospitals` VALUES (51, '岳麓区咸嘉湖社区卫生服务中心', 0, '综合 ', '0', '岳麓区', '112.936369', '28.220901', NULL, NULL, NULL);
INSERT INTO `tbHospitals` VALUES (52, '岳麓区西湖街道社区卫生服务中心', 0, '综合 ', '0', '岳麓区', '112.944131', '28.217782', NULL, NULL, NULL);
INSERT INTO `tbHospitals` VALUES (53, '雨花区高桥街道社区卫生服务中心', 0, '综合 ', '0', '雨花区', '113.034553', '28.185552', NULL, NULL, NULL);
INSERT INTO `tbHospitals` VALUES (54, '长沙县湘龙街道社区卫生服务中心', 0, '综合 ', '0', '长沙县', '113.075871', '28.269335', NULL, NULL, NULL);
INSERT INTO `tbHospitals` VALUES (55, '芙蓉区火星街道社区卫生服务中心', 0, '综合 ', '0', '芙蓉区', '113.029693', '28.211154', NULL, NULL, NULL);
INSERT INTO `tbHospitals` VALUES (56, '芙蓉区定王台街道社区卫生服务中心', 0, '综合 ', '0', '芙蓉区', '112.989279', '28.204602', NULL, NULL, NULL);
INSERT INTO `tbHospitals` VALUES (57, '芙蓉区马王堆街道社区卫生服务中心', 0, '综合 ', '0', '芙蓉区', '113.032226', '28.206439', NULL, NULL, NULL);
INSERT INTO `tbHospitals` VALUES (58, '宁乡县大成桥镇永盛村卫生室', 0, '综合 ', '0', '宁乡县', '112.40317', '28.201361', NULL, NULL, NULL);
INSERT INTO `tbHospitals` VALUES (59, '宁乡县煤炭坝镇贺石桥村卫生室', 0, '综合 ', '0', '宁乡县', '112.423923', '28.282681', NULL, NULL, NULL);
INSERT INTO `tbHospitals` VALUES (60, '宁乡市煤炭坝镇卫生院', 0, '综合 ', '0', '宁乡县', '112.394017', '28.252004', NULL, NULL, NULL);
INSERT INTO `tbHospitals` VALUES (61, '坝塘镇坝塘社区卫生室', 0, '综合 ', '0', '宁乡县', '112.480559', '28.154947', NULL, NULL, NULL);
INSERT INTO `tbHospitals` VALUES (62, '坝塘镇卫生院沩乌医院', 0, '综合 ', '0', '宁乡县', '112.486636', '28.185045', NULL, NULL, NULL);
INSERT INTO `tbHospitals` VALUES (63, '宁乡市回龙铺镇卫生院', 0, '综合 ', '0', '宁乡县', '112.459386', '28.215882', NULL, NULL, NULL);
INSERT INTO `tbHospitals` VALUES (64, '长沙优伢仕口腔医院', 0, '口腔', '0', '开福区', '113.013853', '28.235334', NULL, NULL, NULL);
INSERT INTO `tbHospitals` VALUES (65, '拜博口腔', 0, '口腔', '0', '芙蓉区', '112.987376', '28.192772', NULL, NULL, NULL);
INSERT INTO `tbHospitals` VALUES (66, '长沙美奥口腔医院（人民路院）', 0, '口腔', '0', '芙蓉区', '113.016829', '28.18967', NULL, NULL, NULL);
INSERT INTO `tbHospitals` VALUES (67, '长沙美奥口腔医院(河西院)', 0, '口腔', '0', '岳麓区', '112.938395', '28.21617', NULL, NULL, NULL);
INSERT INTO `tbHospitals` VALUES (68, '周医生牙科', 0, '口腔', '0', '长沙县', '113.087771', '28.248546', NULL, NULL, NULL);
INSERT INTO `tbHospitals` VALUES (69, '德皓口腔连锁宁乡旗舰店', 0, '口腔', '0', '宁乡市', '112.551305', '28.249871', NULL, NULL, NULL);
INSERT INTO `tbHospitals` VALUES (70, '范凯口腔科诊所', 0, '口腔', '0', '宁乡市', '112.563895', '28.257247', NULL, NULL, NULL);
INSERT INTO `tbHospitals` VALUES (71, '天马医院', 11, '综合', '0', '岳麓区', '112.956044', '28.168025', NULL, NULL, NULL);
INSERT INTO `tbHospitals` VALUES (72, '赵英口腔专科', 0, '口腔', '0', '岳麓区', '112.951475', '28.181276', NULL, NULL, NULL);
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
