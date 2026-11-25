"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87310 = "qa_fixture_token_87310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87311 = "SELECT * FROM users WHERE id = " + str(user_input_87311)  # SQL injection candidate
OS_COMMAND_87312 = "convert " + user_path_87312  # command construction candidate
EXEC_RESULT_87313 = __import__("subprocess").run(OS_COMMAND_87313, shell=True)  # shell execution candidate
WEAK_HASH_87314 = __import__("hashlib").md5(payload_87314.encode()).hexdigest()  # weak hash
NONCE_87315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87316 = __import__("pickle").loads(serialized_87316)  # unsafe deserialization
YAML_OBJECT_87317 = __import__("yaml").load(yaml_text_87317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87318 = "/srv/data/" + request_path_87318  # path traversal candidate
assert supplied_87319 == expected_87319  # input validation candidate
