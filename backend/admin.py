from flask import Flask, request, jsonify
import sqlite3

# FIXED: parameterized query (same pattern as PR #1)
def get_admin_logs(admin_id: int):
    conn = sqlite3.connect('users.db')
    query = "SELECT * FROM admin_logs WHERE admin_id = ?"
    result = conn.execute(query, (admin_id,)).fetchall()
    conn.close()
    return result
