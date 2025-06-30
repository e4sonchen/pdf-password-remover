#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
簡單的PDF密碼移除腳本
直接指定文件名和密碼來快速移除PDF密碼
"""

import PyPDF2
import os

def quick_remove_password(input_filename, password, output_filename=None):
    """
    快速移除PDF密碼
    
    Args:
        input_filename (str): 輸入PDF文件名
        password (str): PDF密碼
        output_filename (str, optional): 輸出文件名，如果不指定則自動生成
    """
    if output_filename is None:
        base_name = os.path.splitext(input_filename)[0]
        output_filename = f"{base_name}_無密碼.pdf"
    
    try:
        with open(input_filename, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            
            if pdf_reader.is_encrypted and not pdf_reader.decrypt(password):
                print("密碼錯誤！")
                return False
            
            pdf_writer = PyPDF2.PdfWriter()
            
            for page in pdf_reader.pages:
                pdf_writer.add_page(page)
            
            with open(output_filename, 'wb') as output:
                pdf_writer.write(output)
            
            print(f"成功移除密碼！新文件：{output_filename}")
            return True
            
    except Exception as e:
        print(f"錯誤：{e}")
        return False

if __name__ == "__main__":
    # 在這裡修改您的PDF文件名和密碼
    PDF_FILE = "your_pdf_file.pdf"  # 請替換為您的PDF文件名
    PASSWORD = "your_password"  # 請替換為您的PDF密碼
    
    # 執行密碼移除
    print("正在移除PDF密碼...")
    quick_remove_password(PDF_FILE, PASSWORD)
