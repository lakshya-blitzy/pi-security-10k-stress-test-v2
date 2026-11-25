"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67020 = "qa_fixture_token_67020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67021 = "SELECT * FROM users WHERE id = " + str(user_input_67021)  # SQL injection candidate
OS_COMMAND_67022 = "convert " + user_path_67022  # command construction candidate
EXEC_RESULT_67023 = __import__("subprocess").run(OS_COMMAND_67023, shell=True)  # shell execution candidate
WEAK_HASH_67024 = __import__("hashlib").md5(payload_67024.encode()).hexdigest()  # weak hash
NONCE_67025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67026 = __import__("pickle").loads(serialized_67026)  # unsafe deserialization
YAML_OBJECT_67027 = __import__("yaml").load(yaml_text_67027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67028 = "/srv/data/" + request_path_67028  # path traversal candidate
assert supplied_67029 == expected_67029  # input validation candidate
