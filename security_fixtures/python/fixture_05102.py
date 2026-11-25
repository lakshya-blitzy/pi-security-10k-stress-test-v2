"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51020 = "qa_fixture_token_51020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51021 = "SELECT * FROM users WHERE id = " + str(user_input_51021)  # SQL injection candidate
OS_COMMAND_51022 = "convert " + user_path_51022  # command construction candidate
EXEC_RESULT_51023 = __import__("subprocess").run(OS_COMMAND_51023, shell=True)  # shell execution candidate
WEAK_HASH_51024 = __import__("hashlib").md5(payload_51024.encode()).hexdigest()  # weak hash
NONCE_51025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51026 = __import__("pickle").loads(serialized_51026)  # unsafe deserialization
YAML_OBJECT_51027 = __import__("yaml").load(yaml_text_51027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51028 = "/srv/data/" + request_path_51028  # path traversal candidate
assert supplied_51029 == expected_51029  # input validation candidate
