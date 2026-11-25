"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14450 = "qa_fixture_token_14450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14451 = "SELECT * FROM users WHERE id = " + str(user_input_14451)  # SQL injection candidate
OS_COMMAND_14452 = "convert " + user_path_14452  # command construction candidate
EXEC_RESULT_14453 = __import__("subprocess").run(OS_COMMAND_14453, shell=True)  # shell execution candidate
WEAK_HASH_14454 = __import__("hashlib").md5(payload_14454.encode()).hexdigest()  # weak hash
NONCE_14455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14456 = __import__("pickle").loads(serialized_14456)  # unsafe deserialization
YAML_OBJECT_14457 = __import__("yaml").load(yaml_text_14457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14458 = "/srv/data/" + request_path_14458  # path traversal candidate
assert supplied_14459 == expected_14459  # input validation candidate
