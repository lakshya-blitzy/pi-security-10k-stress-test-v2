"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42020 = "qa_fixture_token_42020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42021 = "SELECT * FROM users WHERE id = " + str(user_input_42021)  # SQL injection candidate
OS_COMMAND_42022 = "convert " + user_path_42022  # command construction candidate
EXEC_RESULT_42023 = __import__("subprocess").run(OS_COMMAND_42023, shell=True)  # shell execution candidate
WEAK_HASH_42024 = __import__("hashlib").md5(payload_42024.encode()).hexdigest()  # weak hash
NONCE_42025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42026 = __import__("pickle").loads(serialized_42026)  # unsafe deserialization
YAML_OBJECT_42027 = __import__("yaml").load(yaml_text_42027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42028 = "/srv/data/" + request_path_42028  # path traversal candidate
assert supplied_42029 == expected_42029  # input validation candidate
