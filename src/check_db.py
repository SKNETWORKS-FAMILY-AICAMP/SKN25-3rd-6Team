"""
DB 확인 스크립트 - 저장된 모든 데이터를 조회합니다
사용법: python check_db.py
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from db import get_db, User, UserCard, ChatHistory, close_db

def print_separator():
    print("=" * 60)

def check_database():
    """데이터베이스의 모든 데이터를 조회하고 출력"""
    db = get_db()
    
    try:
        # Users 테이블
        print_separator()
        print("📊 USERS 테이블")
        print_separator()
        users = db.query(User).all()
        if users:
            for user in users:
                print(f"  ID: {user.user_id}")
                print(f"  사용자명: {user.username}")
                print(f"  MBTI: {user.mbti}")
                print(f"  가입일: {user.created_at}")
                print()
        else:
            print("  데이터가 없습니다.")
        
        # UserCards 테이블
        print_separator()
        print("💳 USER_CARDS 테이블")
        print_separator()
        cards = db.query(UserCard).all()
        if cards:
            for card in cards:
                user = db.query(User).filter(User.user_id == card.user_id).first()
                print(f"  카드ID: {card.card_id}")
                print(f"  사용자: {user.username if user else 'N/A'}")
                print(f"  카드명: {card.card_name}")
                print(f"  카드사: {card.company}")
                print()
        else:
            print("  데이터가 없습니다.")
        
        # ChatHistory 테이블
        print_separator()
        print("💬 CHAT_HISTORY 테이블")
        print_separator()
        chats = db.query(ChatHistory).order_by(ChatHistory.created_at).all()
        if chats:
            for chat in chats:
                user = db.query(User).filter(User.user_id == chat.user_id).first()
                print(f"  채팅ID: {chat.chat_id}")
                print(f"  사용자: {user.username if user else 'N/A'}")
                print(f"  역할: {chat.role}")
                print(f"  내용: {chat.content[:100]}...")
                print(f"  시간: {chat.created_at}")
                print()
        else:
            print("  데이터가 없습니다.")
        
        print_separator()
        print("✅ DB 확인 완료!")
        print_separator()
    
    finally:
        close_db(db)

if __name__ == "__main__":
    check_database()
