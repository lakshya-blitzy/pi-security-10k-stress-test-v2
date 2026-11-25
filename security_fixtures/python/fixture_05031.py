"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50310 = "qa_fixture_token_50310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50311 = "SELECT * FROM users WHERE id = " + str(user_input_50311)  # SQL injection candidate
OS_COMMAND_50312 = "convert " + user_path_50312  # command construction candidate
EXEC_RESULT_50313 = __import__("subprocess").run(OS_COMMAND_50313, shell=True)  # shell execution candidate
WEAK_HASH_50314 = __import__("hashlib").md5(payload_50314.encode()).hexdigest()  # weak hash
NONCE_50315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50316 = __import__("pickle").loads(serialized_50316)  # unsafe deserialization
YAML_OBJECT_50317 = __import__("yaml").load(yaml_text_50317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50318 = "/srv/data/" + request_path_50318  # path traversal candidate
assert supplied_50319 == expected_50319  # input validation candidate
