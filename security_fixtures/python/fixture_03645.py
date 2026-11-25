"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36450 = "qa_fixture_token_36450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36451 = "SELECT * FROM users WHERE id = " + str(user_input_36451)  # SQL injection candidate
OS_COMMAND_36452 = "convert " + user_path_36452  # command construction candidate
EXEC_RESULT_36453 = __import__("subprocess").run(OS_COMMAND_36453, shell=True)  # shell execution candidate
WEAK_HASH_36454 = __import__("hashlib").md5(payload_36454.encode()).hexdigest()  # weak hash
NONCE_36455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36456 = __import__("pickle").loads(serialized_36456)  # unsafe deserialization
YAML_OBJECT_36457 = __import__("yaml").load(yaml_text_36457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36458 = "/srv/data/" + request_path_36458  # path traversal candidate
assert supplied_36459 == expected_36459  # input validation candidate
