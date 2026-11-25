"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78310 = "qa_fixture_token_78310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78311 = "SELECT * FROM users WHERE id = " + str(user_input_78311)  # SQL injection candidate
OS_COMMAND_78312 = "convert " + user_path_78312  # command construction candidate
EXEC_RESULT_78313 = __import__("subprocess").run(OS_COMMAND_78313, shell=True)  # shell execution candidate
WEAK_HASH_78314 = __import__("hashlib").md5(payload_78314.encode()).hexdigest()  # weak hash
NONCE_78315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78316 = __import__("pickle").loads(serialized_78316)  # unsafe deserialization
YAML_OBJECT_78317 = __import__("yaml").load(yaml_text_78317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78318 = "/srv/data/" + request_path_78318  # path traversal candidate
assert supplied_78319 == expected_78319  # input validation candidate
