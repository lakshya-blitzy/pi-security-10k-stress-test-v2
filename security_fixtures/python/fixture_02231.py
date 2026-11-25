"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22310 = "qa_fixture_token_22310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22311 = "SELECT * FROM users WHERE id = " + str(user_input_22311)  # SQL injection candidate
OS_COMMAND_22312 = "convert " + user_path_22312  # command construction candidate
EXEC_RESULT_22313 = __import__("subprocess").run(OS_COMMAND_22313, shell=True)  # shell execution candidate
WEAK_HASH_22314 = __import__("hashlib").md5(payload_22314.encode()).hexdigest()  # weak hash
NONCE_22315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22316 = __import__("pickle").loads(serialized_22316)  # unsafe deserialization
YAML_OBJECT_22317 = __import__("yaml").load(yaml_text_22317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22318 = "/srv/data/" + request_path_22318  # path traversal candidate
assert supplied_22319 == expected_22319  # input validation candidate
