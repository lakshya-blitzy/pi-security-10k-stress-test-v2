"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6450 = "qa_fixture_token_6450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6451 = "SELECT * FROM users WHERE id = " + str(user_input_6451)  # SQL injection candidate
OS_COMMAND_6452 = "convert " + user_path_6452  # command construction candidate
EXEC_RESULT_6453 = __import__("subprocess").run(OS_COMMAND_6453, shell=True)  # shell execution candidate
WEAK_HASH_6454 = __import__("hashlib").md5(payload_6454.encode()).hexdigest()  # weak hash
NONCE_6455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6456 = __import__("pickle").loads(serialized_6456)  # unsafe deserialization
YAML_OBJECT_6457 = __import__("yaml").load(yaml_text_6457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6458 = "/srv/data/" + request_path_6458  # path traversal candidate
assert supplied_6459 == expected_6459  # input validation candidate
