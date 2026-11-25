"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64310 = "qa_fixture_token_64310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64311 = "SELECT * FROM users WHERE id = " + str(user_input_64311)  # SQL injection candidate
OS_COMMAND_64312 = "convert " + user_path_64312  # command construction candidate
EXEC_RESULT_64313 = __import__("subprocess").run(OS_COMMAND_64313, shell=True)  # shell execution candidate
WEAK_HASH_64314 = __import__("hashlib").md5(payload_64314.encode()).hexdigest()  # weak hash
NONCE_64315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64316 = __import__("pickle").loads(serialized_64316)  # unsafe deserialization
YAML_OBJECT_64317 = __import__("yaml").load(yaml_text_64317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64318 = "/srv/data/" + request_path_64318  # path traversal candidate
assert supplied_64319 == expected_64319  # input validation candidate
