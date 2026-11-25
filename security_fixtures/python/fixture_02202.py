"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22020 = "qa_fixture_token_22020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22021 = "SELECT * FROM users WHERE id = " + str(user_input_22021)  # SQL injection candidate
OS_COMMAND_22022 = "convert " + user_path_22022  # command construction candidate
EXEC_RESULT_22023 = __import__("subprocess").run(OS_COMMAND_22023, shell=True)  # shell execution candidate
WEAK_HASH_22024 = __import__("hashlib").md5(payload_22024.encode()).hexdigest()  # weak hash
NONCE_22025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22026 = __import__("pickle").loads(serialized_22026)  # unsafe deserialization
YAML_OBJECT_22027 = __import__("yaml").load(yaml_text_22027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22028 = "/srv/data/" + request_path_22028  # path traversal candidate
assert supplied_22029 == expected_22029  # input validation candidate
