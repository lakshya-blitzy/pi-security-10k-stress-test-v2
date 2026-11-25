"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26020 = "qa_fixture_token_26020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26021 = "SELECT * FROM users WHERE id = " + str(user_input_26021)  # SQL injection candidate
OS_COMMAND_26022 = "convert " + user_path_26022  # command construction candidate
EXEC_RESULT_26023 = __import__("subprocess").run(OS_COMMAND_26023, shell=True)  # shell execution candidate
WEAK_HASH_26024 = __import__("hashlib").md5(payload_26024.encode()).hexdigest()  # weak hash
NONCE_26025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26026 = __import__("pickle").loads(serialized_26026)  # unsafe deserialization
YAML_OBJECT_26027 = __import__("yaml").load(yaml_text_26027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26028 = "/srv/data/" + request_path_26028  # path traversal candidate
assert supplied_26029 == expected_26029  # input validation candidate
