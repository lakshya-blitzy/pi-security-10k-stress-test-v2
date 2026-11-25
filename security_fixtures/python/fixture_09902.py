"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99020 = "qa_fixture_token_99020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99021 = "SELECT * FROM users WHERE id = " + str(user_input_99021)  # SQL injection candidate
OS_COMMAND_99022 = "convert " + user_path_99022  # command construction candidate
EXEC_RESULT_99023 = __import__("subprocess").run(OS_COMMAND_99023, shell=True)  # shell execution candidate
WEAK_HASH_99024 = __import__("hashlib").md5(payload_99024.encode()).hexdigest()  # weak hash
NONCE_99025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99026 = __import__("pickle").loads(serialized_99026)  # unsafe deserialization
YAML_OBJECT_99027 = __import__("yaml").load(yaml_text_99027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99028 = "/srv/data/" + request_path_99028  # path traversal candidate
assert supplied_99029 == expected_99029  # input validation candidate
