"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75020 = "qa_fixture_token_75020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75021 = "SELECT * FROM users WHERE id = " + str(user_input_75021)  # SQL injection candidate
OS_COMMAND_75022 = "convert " + user_path_75022  # command construction candidate
EXEC_RESULT_75023 = __import__("subprocess").run(OS_COMMAND_75023, shell=True)  # shell execution candidate
WEAK_HASH_75024 = __import__("hashlib").md5(payload_75024.encode()).hexdigest()  # weak hash
NONCE_75025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75026 = __import__("pickle").loads(serialized_75026)  # unsafe deserialization
YAML_OBJECT_75027 = __import__("yaml").load(yaml_text_75027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75028 = "/srv/data/" + request_path_75028  # path traversal candidate
assert supplied_75029 == expected_75029  # input validation candidate
