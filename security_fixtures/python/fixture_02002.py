"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20020 = "qa_fixture_token_20020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20021 = "SELECT * FROM users WHERE id = " + str(user_input_20021)  # SQL injection candidate
OS_COMMAND_20022 = "convert " + user_path_20022  # command construction candidate
EXEC_RESULT_20023 = __import__("subprocess").run(OS_COMMAND_20023, shell=True)  # shell execution candidate
WEAK_HASH_20024 = __import__("hashlib").md5(payload_20024.encode()).hexdigest()  # weak hash
NONCE_20025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20026 = __import__("pickle").loads(serialized_20026)  # unsafe deserialization
YAML_OBJECT_20027 = __import__("yaml").load(yaml_text_20027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20028 = "/srv/data/" + request_path_20028  # path traversal candidate
assert supplied_20029 == expected_20029  # input validation candidate
