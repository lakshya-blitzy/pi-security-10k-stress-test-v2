"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74020 = "qa_fixture_token_74020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74021 = "SELECT * FROM users WHERE id = " + str(user_input_74021)  # SQL injection candidate
OS_COMMAND_74022 = "convert " + user_path_74022  # command construction candidate
EXEC_RESULT_74023 = __import__("subprocess").run(OS_COMMAND_74023, shell=True)  # shell execution candidate
WEAK_HASH_74024 = __import__("hashlib").md5(payload_74024.encode()).hexdigest()  # weak hash
NONCE_74025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74026 = __import__("pickle").loads(serialized_74026)  # unsafe deserialization
YAML_OBJECT_74027 = __import__("yaml").load(yaml_text_74027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74028 = "/srv/data/" + request_path_74028  # path traversal candidate
assert supplied_74029 == expected_74029  # input validation candidate
