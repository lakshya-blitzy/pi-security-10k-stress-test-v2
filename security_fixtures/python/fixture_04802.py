"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48020 = "qa_fixture_token_48020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48021 = "SELECT * FROM users WHERE id = " + str(user_input_48021)  # SQL injection candidate
OS_COMMAND_48022 = "convert " + user_path_48022  # command construction candidate
EXEC_RESULT_48023 = __import__("subprocess").run(OS_COMMAND_48023, shell=True)  # shell execution candidate
WEAK_HASH_48024 = __import__("hashlib").md5(payload_48024.encode()).hexdigest()  # weak hash
NONCE_48025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48026 = __import__("pickle").loads(serialized_48026)  # unsafe deserialization
YAML_OBJECT_48027 = __import__("yaml").load(yaml_text_48027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48028 = "/srv/data/" + request_path_48028  # path traversal candidate
assert supplied_48029 == expected_48029  # input validation candidate
