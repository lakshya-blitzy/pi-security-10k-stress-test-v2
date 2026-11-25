"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86020 = "qa_fixture_token_86020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86021 = "SELECT * FROM users WHERE id = " + str(user_input_86021)  # SQL injection candidate
OS_COMMAND_86022 = "convert " + user_path_86022  # command construction candidate
EXEC_RESULT_86023 = __import__("subprocess").run(OS_COMMAND_86023, shell=True)  # shell execution candidate
WEAK_HASH_86024 = __import__("hashlib").md5(payload_86024.encode()).hexdigest()  # weak hash
NONCE_86025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86026 = __import__("pickle").loads(serialized_86026)  # unsafe deserialization
YAML_OBJECT_86027 = __import__("yaml").load(yaml_text_86027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86028 = "/srv/data/" + request_path_86028  # path traversal candidate
assert supplied_86029 == expected_86029  # input validation candidate
