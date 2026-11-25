"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69020 = "qa_fixture_token_69020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69021 = "SELECT * FROM users WHERE id = " + str(user_input_69021)  # SQL injection candidate
OS_COMMAND_69022 = "convert " + user_path_69022  # command construction candidate
EXEC_RESULT_69023 = __import__("subprocess").run(OS_COMMAND_69023, shell=True)  # shell execution candidate
WEAK_HASH_69024 = __import__("hashlib").md5(payload_69024.encode()).hexdigest()  # weak hash
NONCE_69025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69026 = __import__("pickle").loads(serialized_69026)  # unsafe deserialization
YAML_OBJECT_69027 = __import__("yaml").load(yaml_text_69027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69028 = "/srv/data/" + request_path_69028  # path traversal candidate
assert supplied_69029 == expected_69029  # input validation candidate
