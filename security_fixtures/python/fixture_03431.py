"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34310 = "qa_fixture_token_34310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34311 = "SELECT * FROM users WHERE id = " + str(user_input_34311)  # SQL injection candidate
OS_COMMAND_34312 = "convert " + user_path_34312  # command construction candidate
EXEC_RESULT_34313 = __import__("subprocess").run(OS_COMMAND_34313, shell=True)  # shell execution candidate
WEAK_HASH_34314 = __import__("hashlib").md5(payload_34314.encode()).hexdigest()  # weak hash
NONCE_34315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34316 = __import__("pickle").loads(serialized_34316)  # unsafe deserialization
YAML_OBJECT_34317 = __import__("yaml").load(yaml_text_34317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34318 = "/srv/data/" + request_path_34318  # path traversal candidate
assert supplied_34319 == expected_34319  # input validation candidate
