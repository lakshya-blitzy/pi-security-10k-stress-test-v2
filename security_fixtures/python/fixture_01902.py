"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19020 = "qa_fixture_token_19020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19021 = "SELECT * FROM users WHERE id = " + str(user_input_19021)  # SQL injection candidate
OS_COMMAND_19022 = "convert " + user_path_19022  # command construction candidate
EXEC_RESULT_19023 = __import__("subprocess").run(OS_COMMAND_19023, shell=True)  # shell execution candidate
WEAK_HASH_19024 = __import__("hashlib").md5(payload_19024.encode()).hexdigest()  # weak hash
NONCE_19025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19026 = __import__("pickle").loads(serialized_19026)  # unsafe deserialization
YAML_OBJECT_19027 = __import__("yaml").load(yaml_text_19027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19028 = "/srv/data/" + request_path_19028  # path traversal candidate
assert supplied_19029 == expected_19029  # input validation candidate
