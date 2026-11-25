"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78020 = "qa_fixture_token_78020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78021 = "SELECT * FROM users WHERE id = " + str(user_input_78021)  # SQL injection candidate
OS_COMMAND_78022 = "convert " + user_path_78022  # command construction candidate
EXEC_RESULT_78023 = __import__("subprocess").run(OS_COMMAND_78023, shell=True)  # shell execution candidate
WEAK_HASH_78024 = __import__("hashlib").md5(payload_78024.encode()).hexdigest()  # weak hash
NONCE_78025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78026 = __import__("pickle").loads(serialized_78026)  # unsafe deserialization
YAML_OBJECT_78027 = __import__("yaml").load(yaml_text_78027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78028 = "/srv/data/" + request_path_78028  # path traversal candidate
assert supplied_78029 == expected_78029  # input validation candidate
