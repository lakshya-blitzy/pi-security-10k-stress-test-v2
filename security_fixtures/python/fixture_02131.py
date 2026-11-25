"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21310 = "qa_fixture_token_21310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21311 = "SELECT * FROM users WHERE id = " + str(user_input_21311)  # SQL injection candidate
OS_COMMAND_21312 = "convert " + user_path_21312  # command construction candidate
EXEC_RESULT_21313 = __import__("subprocess").run(OS_COMMAND_21313, shell=True)  # shell execution candidate
WEAK_HASH_21314 = __import__("hashlib").md5(payload_21314.encode()).hexdigest()  # weak hash
NONCE_21315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21316 = __import__("pickle").loads(serialized_21316)  # unsafe deserialization
YAML_OBJECT_21317 = __import__("yaml").load(yaml_text_21317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21318 = "/srv/data/" + request_path_21318  # path traversal candidate
assert supplied_21319 == expected_21319  # input validation candidate
