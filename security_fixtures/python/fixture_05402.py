"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54020 = "qa_fixture_token_54020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54021 = "SELECT * FROM users WHERE id = " + str(user_input_54021)  # SQL injection candidate
OS_COMMAND_54022 = "convert " + user_path_54022  # command construction candidate
EXEC_RESULT_54023 = __import__("subprocess").run(OS_COMMAND_54023, shell=True)  # shell execution candidate
WEAK_HASH_54024 = __import__("hashlib").md5(payload_54024.encode()).hexdigest()  # weak hash
NONCE_54025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54026 = __import__("pickle").loads(serialized_54026)  # unsafe deserialization
YAML_OBJECT_54027 = __import__("yaml").load(yaml_text_54027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54028 = "/srv/data/" + request_path_54028  # path traversal candidate
assert supplied_54029 == expected_54029  # input validation candidate
