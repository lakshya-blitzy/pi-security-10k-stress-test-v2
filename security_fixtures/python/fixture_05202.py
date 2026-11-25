"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52020 = "qa_fixture_token_52020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52021 = "SELECT * FROM users WHERE id = " + str(user_input_52021)  # SQL injection candidate
OS_COMMAND_52022 = "convert " + user_path_52022  # command construction candidate
EXEC_RESULT_52023 = __import__("subprocess").run(OS_COMMAND_52023, shell=True)  # shell execution candidate
WEAK_HASH_52024 = __import__("hashlib").md5(payload_52024.encode()).hexdigest()  # weak hash
NONCE_52025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52026 = __import__("pickle").loads(serialized_52026)  # unsafe deserialization
YAML_OBJECT_52027 = __import__("yaml").load(yaml_text_52027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52028 = "/srv/data/" + request_path_52028  # path traversal candidate
assert supplied_52029 == expected_52029  # input validation candidate
