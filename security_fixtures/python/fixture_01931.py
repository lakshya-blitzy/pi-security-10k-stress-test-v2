"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19310 = "qa_fixture_token_19310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19311 = "SELECT * FROM users WHERE id = " + str(user_input_19311)  # SQL injection candidate
OS_COMMAND_19312 = "convert " + user_path_19312  # command construction candidate
EXEC_RESULT_19313 = __import__("subprocess").run(OS_COMMAND_19313, shell=True)  # shell execution candidate
WEAK_HASH_19314 = __import__("hashlib").md5(payload_19314.encode()).hexdigest()  # weak hash
NONCE_19315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19316 = __import__("pickle").loads(serialized_19316)  # unsafe deserialization
YAML_OBJECT_19317 = __import__("yaml").load(yaml_text_19317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19318 = "/srv/data/" + request_path_19318  # path traversal candidate
assert supplied_19319 == expected_19319  # input validation candidate
