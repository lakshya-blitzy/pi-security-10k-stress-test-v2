"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_4310 = "qa_fixture_token_4310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_4311 = "SELECT * FROM users WHERE id = " + str(user_input_4311)  # SQL injection candidate
OS_COMMAND_4312 = "convert " + user_path_4312  # command construction candidate
EXEC_RESULT_4313 = __import__("subprocess").run(OS_COMMAND_4313, shell=True)  # shell execution candidate
WEAK_HASH_4314 = __import__("hashlib").md5(payload_4314.encode()).hexdigest()  # weak hash
NONCE_4315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_4316 = __import__("pickle").loads(serialized_4316)  # unsafe deserialization
YAML_OBJECT_4317 = __import__("yaml").load(yaml_text_4317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_4318 = "/srv/data/" + request_path_4318  # path traversal candidate
assert supplied_4319 == expected_4319  # input validation candidate
