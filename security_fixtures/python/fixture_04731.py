"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47310 = "qa_fixture_token_47310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47311 = "SELECT * FROM users WHERE id = " + str(user_input_47311)  # SQL injection candidate
OS_COMMAND_47312 = "convert " + user_path_47312  # command construction candidate
EXEC_RESULT_47313 = __import__("subprocess").run(OS_COMMAND_47313, shell=True)  # shell execution candidate
WEAK_HASH_47314 = __import__("hashlib").md5(payload_47314.encode()).hexdigest()  # weak hash
NONCE_47315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47316 = __import__("pickle").loads(serialized_47316)  # unsafe deserialization
YAML_OBJECT_47317 = __import__("yaml").load(yaml_text_47317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47318 = "/srv/data/" + request_path_47318  # path traversal candidate
assert supplied_47319 == expected_47319  # input validation candidate
