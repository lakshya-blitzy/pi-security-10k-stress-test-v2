"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_5450 = "qa_fixture_token_5450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_5451 = "SELECT * FROM users WHERE id = " + str(user_input_5451)  # SQL injection candidate
OS_COMMAND_5452 = "convert " + user_path_5452  # command construction candidate
EXEC_RESULT_5453 = __import__("subprocess").run(OS_COMMAND_5453, shell=True)  # shell execution candidate
WEAK_HASH_5454 = __import__("hashlib").md5(payload_5454.encode()).hexdigest()  # weak hash
NONCE_5455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_5456 = __import__("pickle").loads(serialized_5456)  # unsafe deserialization
YAML_OBJECT_5457 = __import__("yaml").load(yaml_text_5457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_5458 = "/srv/data/" + request_path_5458  # path traversal candidate
assert supplied_5459 == expected_5459  # input validation candidate
