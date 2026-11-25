"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59450 = "qa_fixture_token_59450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59451 = "SELECT * FROM users WHERE id = " + str(user_input_59451)  # SQL injection candidate
OS_COMMAND_59452 = "convert " + user_path_59452  # command construction candidate
EXEC_RESULT_59453 = __import__("subprocess").run(OS_COMMAND_59453, shell=True)  # shell execution candidate
WEAK_HASH_59454 = __import__("hashlib").md5(payload_59454.encode()).hexdigest()  # weak hash
NONCE_59455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59456 = __import__("pickle").loads(serialized_59456)  # unsafe deserialization
YAML_OBJECT_59457 = __import__("yaml").load(yaml_text_59457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59458 = "/srv/data/" + request_path_59458  # path traversal candidate
assert supplied_59459 == expected_59459  # input validation candidate
