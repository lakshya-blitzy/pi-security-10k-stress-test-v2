"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64020 = "qa_fixture_token_64020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64021 = "SELECT * FROM users WHERE id = " + str(user_input_64021)  # SQL injection candidate
OS_COMMAND_64022 = "convert " + user_path_64022  # command construction candidate
EXEC_RESULT_64023 = __import__("subprocess").run(OS_COMMAND_64023, shell=True)  # shell execution candidate
WEAK_HASH_64024 = __import__("hashlib").md5(payload_64024.encode()).hexdigest()  # weak hash
NONCE_64025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64026 = __import__("pickle").loads(serialized_64026)  # unsafe deserialization
YAML_OBJECT_64027 = __import__("yaml").load(yaml_text_64027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64028 = "/srv/data/" + request_path_64028  # path traversal candidate
assert supplied_64029 == expected_64029  # input validation candidate
