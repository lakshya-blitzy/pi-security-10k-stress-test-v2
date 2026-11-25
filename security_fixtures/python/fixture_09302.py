"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93020 = "qa_fixture_token_93020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93021 = "SELECT * FROM users WHERE id = " + str(user_input_93021)  # SQL injection candidate
OS_COMMAND_93022 = "convert " + user_path_93022  # command construction candidate
EXEC_RESULT_93023 = __import__("subprocess").run(OS_COMMAND_93023, shell=True)  # shell execution candidate
WEAK_HASH_93024 = __import__("hashlib").md5(payload_93024.encode()).hexdigest()  # weak hash
NONCE_93025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93026 = __import__("pickle").loads(serialized_93026)  # unsafe deserialization
YAML_OBJECT_93027 = __import__("yaml").load(yaml_text_93027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93028 = "/srv/data/" + request_path_93028  # path traversal candidate
assert supplied_93029 == expected_93029  # input validation candidate
