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

 Date: 21/06/2019 15:29:52
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for tbSickness
-- ----------------------------
DROP TABLE IF EXISTS `tbSickness`;
CREATE TABLE `tbSickness` (
  `id` int(9) NOT NULL,
  `sickName` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `dep` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `symptomCha` text COLLATE utf8_unicode_ci,
  `affectCha` text COLLATE utf8_unicode_ci,
  `examine` varchar(2000) COLLATE utf8_unicode_ci DEFAULT NULL,
  `treat` varchar(2000) COLLATE utf8_unicode_ci DEFAULT NULL,
  `times` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of tbSickness
-- ----------------------------
BEGIN;
INSERT INTO `tbSickness` VALUES (1060, '深龋', '口腔科', '[[\"长期性牙痛\",0],[\"敏感性牙痛\",10],[\"牙痛史\",0],[\"多发牙痛\",0],[\"牙龈出血\",0]]', '[\"出生年份\",\"性别\"]', '磨牙及前磨牙牙合面有较深龋洞，去净腐质后洞底位于牙本质中层或深层。牙髓温度测验正常，电活力测试，牙龈色泽正常，无松动。', '1、复合树脂直接粘接修复术；2、银汞合金充填术；3、复合体充填术；4、玻璃离子充填术； 5、嵌体等间接修复术。', '1-2次');
INSERT INTO `tbSickness` VALUES (1061, '牙周脓肿', '口腔科', '[[\"长期性牙痛\",10],[\"敏感性牙痛\",0],[\"牙痛史\",0],[\"多发牙痛\",10],[\"牙龈红肿\",10]]', '[\"出生年份\",\"性别\"]', '牙龈可见脓肿形成，伴附着丧失，可探及深牙周袋；X线片可显示明显牙槽骨吸收；如有多发脓肿还应考虑全身疾病（如糖尿病）可能性。', '1、总体治疗原则是止痛、防止感染扩散以及使脓液引流。2、脓肿初期脓液尚未形成前，可清除大块牙石，冲洗牙周袋，袋内使用防腐收敛药或抗菌药；3、脓肿后期脓液形成出现波动感时，可以进行脓肿切开引流，并彻底冲洗脓腔；4、给予含漱药物，协助控制口腔卫生，必要时给予全身抗生素或支持疗法；5、没有保留价值的患牙应在急性症状缓解后予以拔除。', '2-5次');
INSERT INTO `tbSickness` VALUES (1062, '菌斑性龈炎', '口腔科', '[[\"敏感性牙痛\",10],[\"牙龈出血\",10],[\"牙龈红肿\",10],[\"口臭\",10]]', '[\"出生年份\",\"性别\"]', '检查牙龈颜色、形态、质地的改变；牙周探诊检查不能探及附着丧失；X线片显示无牙槽骨吸收。', '1、去除病因。通过洁治术清除菌斑、牙石，去除造成菌斑滞留和刺激牙龈的因素，牙龈炎症可在一周左右改善。2、对于牙龈炎症较重的患者，可配合局部药物治疗，常用的局部药物包括0.12%氯己定，3%双氧水（医师用药）等，建议全身不使用抗生素。3、防止复发。菌斑性龈炎容易复发，在去除病因的同时，应使其能够长期保持良好的口腔卫生状况，并能够进行定期复查和治疗，这样才能保持疗效，防止复发。', '2-3次');
INSERT INTO `tbSickness` VALUES (1063, '慢性牙髓炎', '口腔科', '[[\"敏感性牙痛\",10],[\"牙痛史\",10],[\"牙龈红肿\",0]]', '[\"出生年份\",\"性别\"]', 'X线片显示患牙冠部牙本质层可有近髓腔或达髓腔的X线密度减低区（深的牙体缺损），根尖周组织无异常改变或有轻微根尖周膜增宽表现。牙体缺损、磨耗等。患牙对温度测试表现异常。', '凡确诊为不可复性牙髓炎的患牙，首选做根管治疗，需获得患者或其监护人的知情同意。', NULL);
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
