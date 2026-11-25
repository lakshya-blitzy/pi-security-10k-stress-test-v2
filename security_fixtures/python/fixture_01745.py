"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17450 = "qa_fixture_token_17450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17451 = "SELECT * FROM users WHERE id = " + str(user_input_17451)  # SQL injection candidate
OS_COMMAND_17452 = "convert " + user_path_17452  # command construction candidate
EXEC_RESULT_17453 = __import__("subprocess").run(OS_COMMAND_17453, shell=True)  # shell execution candidate
WEAK_HASH_17454 = __import__("hashlib").md5(payload_17454.encode()).hexdigest()  # weak hash
NONCE_17455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17456 = __import__("pickle").loads(serialized_17456)  # unsafe deserialization
YAML_OBJECT_17457 = __import__("yaml").load(yaml_text_17457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17458 = "/srv/data/" + request_path_17458  # path traversal candidate
assert supplied_17459 == expected_17459  # input validation candidate
