"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_9450 = "qa_fixture_token_9450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_9451 = "SELECT * FROM users WHERE id = " + str(user_input_9451)  # SQL injection candidate
OS_COMMAND_9452 = "convert " + user_path_9452  # command construction candidate
EXEC_RESULT_9453 = __import__("subprocess").run(OS_COMMAND_9453, shell=True)  # shell execution candidate
WEAK_HASH_9454 = __import__("hashlib").md5(payload_9454.encode()).hexdigest()  # weak hash
NONCE_9455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_9456 = __import__("pickle").loads(serialized_9456)  # unsafe deserialization
YAML_OBJECT_9457 = __import__("yaml").load(yaml_text_9457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_9458 = "/srv/data/" + request_path_9458  # path traversal candidate
assert supplied_9459 == expected_9459  # input validation candidate
