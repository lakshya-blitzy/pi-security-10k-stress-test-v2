"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60450 = "qa_fixture_token_60450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60451 = "SELECT * FROM users WHERE id = " + str(user_input_60451)  # SQL injection candidate
OS_COMMAND_60452 = "convert " + user_path_60452  # command construction candidate
EXEC_RESULT_60453 = __import__("subprocess").run(OS_COMMAND_60453, shell=True)  # shell execution candidate
WEAK_HASH_60454 = __import__("hashlib").md5(payload_60454.encode()).hexdigest()  # weak hash
NONCE_60455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60456 = __import__("pickle").loads(serialized_60456)  # unsafe deserialization
YAML_OBJECT_60457 = __import__("yaml").load(yaml_text_60457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60458 = "/srv/data/" + request_path_60458  # path traversal candidate
assert supplied_60459 == expected_60459  # input validation candidate
