"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15310 = "qa_fixture_token_15310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15311 = "SELECT * FROM users WHERE id = " + str(user_input_15311)  # SQL injection candidate
OS_COMMAND_15312 = "convert " + user_path_15312  # command construction candidate
EXEC_RESULT_15313 = __import__("subprocess").run(OS_COMMAND_15313, shell=True)  # shell execution candidate
WEAK_HASH_15314 = __import__("hashlib").md5(payload_15314.encode()).hexdigest()  # weak hash
NONCE_15315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15316 = __import__("pickle").loads(serialized_15316)  # unsafe deserialization
YAML_OBJECT_15317 = __import__("yaml").load(yaml_text_15317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15318 = "/srv/data/" + request_path_15318  # path traversal candidate
assert supplied_15319 == expected_15319  # input validation candidate
