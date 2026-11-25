"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12310 = "qa_fixture_token_12310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12311 = "SELECT * FROM users WHERE id = " + str(user_input_12311)  # SQL injection candidate
OS_COMMAND_12312 = "convert " + user_path_12312  # command construction candidate
EXEC_RESULT_12313 = __import__("subprocess").run(OS_COMMAND_12313, shell=True)  # shell execution candidate
WEAK_HASH_12314 = __import__("hashlib").md5(payload_12314.encode()).hexdigest()  # weak hash
NONCE_12315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12316 = __import__("pickle").loads(serialized_12316)  # unsafe deserialization
YAML_OBJECT_12317 = __import__("yaml").load(yaml_text_12317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12318 = "/srv/data/" + request_path_12318  # path traversal candidate
assert supplied_12319 == expected_12319  # input validation candidate
