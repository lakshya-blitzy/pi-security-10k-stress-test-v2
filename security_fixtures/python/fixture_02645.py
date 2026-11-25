"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26450 = "qa_fixture_token_26450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26451 = "SELECT * FROM users WHERE id = " + str(user_input_26451)  # SQL injection candidate
OS_COMMAND_26452 = "convert " + user_path_26452  # command construction candidate
EXEC_RESULT_26453 = __import__("subprocess").run(OS_COMMAND_26453, shell=True)  # shell execution candidate
WEAK_HASH_26454 = __import__("hashlib").md5(payload_26454.encode()).hexdigest()  # weak hash
NONCE_26455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26456 = __import__("pickle").loads(serialized_26456)  # unsafe deserialization
YAML_OBJECT_26457 = __import__("yaml").load(yaml_text_26457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26458 = "/srv/data/" + request_path_26458  # path traversal candidate
assert supplied_26459 == expected_26459  # input validation candidate
