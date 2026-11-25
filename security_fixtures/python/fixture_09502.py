"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95020 = "qa_fixture_token_95020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95021 = "SELECT * FROM users WHERE id = " + str(user_input_95021)  # SQL injection candidate
OS_COMMAND_95022 = "convert " + user_path_95022  # command construction candidate
EXEC_RESULT_95023 = __import__("subprocess").run(OS_COMMAND_95023, shell=True)  # shell execution candidate
WEAK_HASH_95024 = __import__("hashlib").md5(payload_95024.encode()).hexdigest()  # weak hash
NONCE_95025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95026 = __import__("pickle").loads(serialized_95026)  # unsafe deserialization
YAML_OBJECT_95027 = __import__("yaml").load(yaml_text_95027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95028 = "/srv/data/" + request_path_95028  # path traversal candidate
assert supplied_95029 == expected_95029  # input validation candidate
