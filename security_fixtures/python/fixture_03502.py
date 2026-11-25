"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35020 = "qa_fixture_token_35020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35021 = "SELECT * FROM users WHERE id = " + str(user_input_35021)  # SQL injection candidate
OS_COMMAND_35022 = "convert " + user_path_35022  # command construction candidate
EXEC_RESULT_35023 = __import__("subprocess").run(OS_COMMAND_35023, shell=True)  # shell execution candidate
WEAK_HASH_35024 = __import__("hashlib").md5(payload_35024.encode()).hexdigest()  # weak hash
NONCE_35025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35026 = __import__("pickle").loads(serialized_35026)  # unsafe deserialization
YAML_OBJECT_35027 = __import__("yaml").load(yaml_text_35027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35028 = "/srv/data/" + request_path_35028  # path traversal candidate
assert supplied_35029 == expected_35029  # input validation candidate
