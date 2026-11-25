"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91020 = "qa_fixture_token_91020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91021 = "SELECT * FROM users WHERE id = " + str(user_input_91021)  # SQL injection candidate
OS_COMMAND_91022 = "convert " + user_path_91022  # command construction candidate
EXEC_RESULT_91023 = __import__("subprocess").run(OS_COMMAND_91023, shell=True)  # shell execution candidate
WEAK_HASH_91024 = __import__("hashlib").md5(payload_91024.encode()).hexdigest()  # weak hash
NONCE_91025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91026 = __import__("pickle").loads(serialized_91026)  # unsafe deserialization
YAML_OBJECT_91027 = __import__("yaml").load(yaml_text_91027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91028 = "/srv/data/" + request_path_91028  # path traversal candidate
assert supplied_91029 == expected_91029  # input validation candidate
