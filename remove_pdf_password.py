#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PDF密碼移除工具
此腳本可以移除PDF文件的密碼保護，並創建一個新的無密碼PDF文件
"""

import PyPDF2
import os
import sys

def remove_pdf_password(input_file, output_file, password):
    """
    移除PDF密碼並創建新的無密碼PDF文件
    
    Args:
        input_file (str): 輸入的受密碼保護的PDF文件路徑
        output_file (str): 輸出的無密碼PDF文件路徑
        password (str): PDF文件的密碼
    
    Returns:
        bool: 成功返回True，失敗返回False
    """
    try:
        # 檢查輸入文件是否存在
        if not os.path.exists(input_file):
            print(f"錯誤：找不到輸入文件 {input_file}")
            return False
        
        # 打開受密碼保護的PDF文件
        with open(input_file, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            
            # 檢查PDF是否有密碼保護
            if pdf_reader.is_encrypted:
                print("PDF文件已加密，正在嘗試解密...")
                
                # 嘗試使用提供的密碼解密
                if pdf_reader.decrypt(password):
                    print("密碼正確！正在移除密碼保護...")
                else:
                    print("錯誤：密碼不正確，無法解密PDF文件")
                    return False
            else:
                print("PDF文件沒有密碼保護")
            
            # 創建新的PDF寫入器
            pdf_writer = PyPDF2.PdfWriter()
            
            # 將所有頁面複製到新的PDF
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                pdf_writer.add_page(page)
            
            # 寫入新的無密碼PDF文件
            with open(output_file, 'wb') as output:
                pdf_writer.write(output)
            
            print(f"成功！無密碼PDF文件已保存為：{output_file}")
            return True
            
    except Exception as e:
        print(f"處理過程中發生錯誤：{str(e)}")
        return False

def main():
    """主函數"""
    print("=== PDF密碼移除工具 ===")
    print()
    
    # 獲取當前目錄中的PDF文件
    current_dir = os.getcwd()
    pdf_files = [f for f in os.listdir(current_dir) if f.lower().endswith('.pdf')]
    
    if not pdf_files:
        print("當前目錄中沒有找到PDF文件")
        return
    
    print("找到以下PDF文件：")
    for i, pdf_file in enumerate(pdf_files, 1):
        print(f"{i}. {pdf_file}")
    
    # 讓用戶選擇PDF文件
    while True:
        try:
            choice = input("\n請選擇要處理的PDF文件編號：")
            file_index = int(choice) - 1
            if 0 <= file_index < len(pdf_files):
                input_file = pdf_files[file_index]
                break
            else:
                print("無效的選擇，請重新輸入")
        except ValueError:
            print("請輸入有效的數字")
    
    # 獲取密碼
    password = input(f"\n請輸入 {input_file} 的密碼：")
    
    # 生成輸出文件名
    base_name = os.path.splitext(input_file)[0]
    output_file = f"{base_name}_無密碼.pdf"
    
    # 確保輸出文件名不會覆蓋現有文件
    counter = 1
    while os.path.exists(output_file):
        output_file = f"{base_name}_無密碼_{counter}.pdf"
        counter += 1
    
    print(f"\n輸入文件：{input_file}")
    print(f"輸出文件：{output_file}")
    print()
    
    # 執行密碼移除
    success = remove_pdf_password(input_file, output_file, password)
    
    if success:
        print("\n操作完成！")
        print(f"原始文件：{input_file}")
        print(f"新文件：{output_file}")
        print("新文件已移除密碼保護，可以直接打開")
    else:
        print("\n操作失敗，請檢查密碼是否正確或文件是否損壞")

if __name__ == "__main__":
    main()
