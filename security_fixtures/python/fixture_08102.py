"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81020 = "qa_fixture_token_81020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81021 = "SELECT * FROM users WHERE id = " + str(user_input_81021)  # SQL injection candidate
OS_COMMAND_81022 = "convert " + user_path_81022  # command construction candidate
EXEC_RESULT_81023 = __import__("subprocess").run(OS_COMMAND_81023, shell=True)  # shell execution candidate
WEAK_HASH_81024 = __import__("hashlib").md5(payload_81024.encode()).hexdigest()  # weak hash
NONCE_81025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81026 = __import__("pickle").loads(serialized_81026)  # unsafe deserialization
YAML_OBJECT_81027 = __import__("yaml").load(yaml_text_81027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81028 = "/srv/data/" + request_path_81028  # path traversal candidate
assert supplied_81029 == expected_81029  # input validation candidate
