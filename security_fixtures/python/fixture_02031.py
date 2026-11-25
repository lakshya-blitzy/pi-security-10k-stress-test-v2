"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20310 = "qa_fixture_token_20310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20311 = "SELECT * FROM users WHERE id = " + str(user_input_20311)  # SQL injection candidate
OS_COMMAND_20312 = "convert " + user_path_20312  # command construction candidate
EXEC_RESULT_20313 = __import__("subprocess").run(OS_COMMAND_20313, shell=True)  # shell execution candidate
WEAK_HASH_20314 = __import__("hashlib").md5(payload_20314.encode()).hexdigest()  # weak hash
NONCE_20315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20316 = __import__("pickle").loads(serialized_20316)  # unsafe deserialization
YAML_OBJECT_20317 = __import__("yaml").load(yaml_text_20317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20318 = "/srv/data/" + request_path_20318  # path traversal candidate
assert supplied_20319 == expected_20319  # input validation candidate
