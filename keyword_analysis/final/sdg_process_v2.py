#pip install datetime, pymysql, pandas, xlrd

#!/usr/bin/python
#coding:utf-8
import sys
import re
import os
import datetime
import pandas as pd
import pymysql
# pymysql.install_as_MySQLdb() # Enable import MySQLdb like in vertsion 2.X

# 建立關鍵字詞庫的資料到資料庫中
def set_sdgs_term(db, lang):
	try:
		# Delete old data with specific language
		cursor = db.cursor()
		sql = "DELETE FROM sdgs_term WHERE language = %s;"
		cursor.execute(sql, (lang))
		db.commit()

		# Insert new data
		df = pd.read_excel('/Users/tuntzu/Documents/NTU_SDGs/Phase1/raw_data/關鍵字詞庫 lin.xlsx', index_col=0, na_filter=False)
		for i in range(1,18):
			terms = zip(df['SDG %s' % i].tolist(), df['WEIGHT-%s' % i].tolist())
			for term in terms:
				if len(term[0].replace(' ', '')) > 0:
					sql = "INSERT INTO sdgs_term (category_id, term, weight, language) VALUES (%s, %s, %s, %s);"
					cursor.execute(sql, (i, term[0], term[1], lang))
					db.commit()
	except:
		print ('An exception occurred.')

# 根據類別獲取關鍵字
def get_sdgs_term_list(cursor, category_id, lang):
	sql = "SELECT id, category_id, term, weight FROM sdgs_term WHERE category_id = %s AND language = %s;"
	cursor.execute(sql, (category_id, lang))
	return cursor.fetchall()

# 將 input 紀錄到資料庫中
def insert_input(db):
	try:
		df = pd.read_excel('/Users/tuntzu/Documents/NTU_SDGs/Phase1/raw_data/107-2課程大綱.xls', na_filter=False)
		cursor = db.cursor()
		for row in range(df.shape[0]):
			text_code = df.iat[row, 0] + '_' + df.iat[row, 4].replace(' ', '') + ('_' + df.iat[row, 5] if (df.iat[row, 5] != '') else '')
			class_name = df.iat[row, 6]
			teacher_name = df.iat[row, 8]
			# Remain original context
			# text_content = (df.iat[row, 9] + df.iat[row, 11]).replace('\n', '').replace('\r', '').replace('\t', '').replace(' ', '')
			text_content = df.iat[row, 9] + df.iat[row, 11]
			
			sql = "INSERT INTO input (text_code, class_name, teacher_name, text_content, text_length) VALUES (%s, %s, %s, %s, %s);"
			cursor.execute(sql, (text_code, class_name, teacher_name, text_content, len(list(text_content))))
			db.commit()
	except:
		print ('An exception occurred.')

# 將分析細節紀錄到資料庫中
def insert_process_detail(cursor, text_code, term_id, frequency, lang, create_time):
	try:
		sql = "INSERT INTO process_detail (text_code, term_id, frequency, language, create_time) VALUES (%s, %s, %s, %s, %s);"
		cursor.execute(sql, (text_code, term_id, frequency, lang, create_time))
	except:
		print ('An exception occurred in insert_process_detail.')

# 將分析結果紀錄到資料庫中
def insert_output(cursor, text_code, category_id, score, lang, create_time):
	try:
		sql = "INSERT INTO output (text_code, category_id, score, language, create_time) VALUES (%s, %s, %s, %s, %s);"
		cursor.execute(sql, (text_code, category_id, score, lang, create_time))
	except:
		print ('An exception occurred in insert_output.')

# 分析 input
def process_input(db, lang, execute_time):
	cursor = db.cursor()

	# 從資料庫取得 SDGs 類別 id
	sql = "SELECT id FROM sdgs_category;"
	cursor.execute(sql)
	sdgs_category = cursor.fetchall()	

	# 從資料庫取得所有類別的 SDGs 關鍵字及權重
	sdgs_term_lists = [get_sdgs_term_list(cursor, sdgs_id, lang) for sdgs_id in (sdgs_category)]

	# 以第一個類別找到的詞庫長度為判斷基準，若陣列長度為零，則視為這個語言的詞庫尚未建立，直接結束
	if (len(sdgs_term_lists[0]) == 0):
		print('Terms in this language cannot be found.')
		return;

	# 從資料庫取得 input
	sql = "SELECT text_code, text_content FROM input;"
	cursor.execute(sql)
	input_list = cursor.fetchall()

	# 每個 input 進行處理
	for row in input_list:
		# 每個 SDGs 類別進行關鍵字運算
		for sdgs_term_list in sdgs_term_lists:
			category_id = sdgs_term_list[0][1]
			score = 0
			# 每個 SDGs 關鍵字權重分數計算
			for term in sdgs_term_list:
				match = re.findall(term[2], row[1], flags=re.IGNORECASE)
				# 在內文找到 pattern 出現的頻率至少一次才做計算與紀錄到資料庫
				if (len(match) > 0):
					frequency = len(match)
					score += term[3] * frequency
					insert_process_detail(cursor, row[0], term[0], frequency, lang, execute_time)	
			# 最終運算結果紀錄到資料庫
			insert_output(cursor, row[0], category_id, score, lang, execute_time)
		db.commit()


def main(argv):
	execute_time = datetime.datetime.now()
	cmd = argv.split(':')

	db = pymysql.connect(host='localhost', port=3306, user='sdgs', passwd='sdgs', db='sdgs', charset='utf8')
	if (cmd[0] == '1'):
		set_sdgs_term(db, cmd[1])
	if (cmd[0] == '2'):
		insert_input(db)
	if (cmd[0] == '3'):
		process_input(db, cmd[1], execute_time)
	db.close()

if __name__ == '__main__':
	if (len(sys.argv) > 1):
		main(sys.argv[1])
	else:
		print('Please key parameter!\n1:CH => insert sdgs-terms(Chinise)\n1:EN => insert sdgs-terms(English)\n2 => insert_input\n3:CH => process input with Chinese terms\n3:EN => process input with English terms')

