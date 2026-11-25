"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73020 = "qa_fixture_token_73020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73021 = "SELECT * FROM users WHERE id = " + str(user_input_73021)  # SQL injection candidate
OS_COMMAND_73022 = "convert " + user_path_73022  # command construction candidate
EXEC_RESULT_73023 = __import__("subprocess").run(OS_COMMAND_73023, shell=True)  # shell execution candidate
WEAK_HASH_73024 = __import__("hashlib").md5(payload_73024.encode()).hexdigest()  # weak hash
NONCE_73025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73026 = __import__("pickle").loads(serialized_73026)  # unsafe deserialization
YAML_OBJECT_73027 = __import__("yaml").load(yaml_text_73027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73028 = "/srv/data/" + request_path_73028  # path traversal candidate
assert supplied_73029 == expected_73029  # input validation candidate
