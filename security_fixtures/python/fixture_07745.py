"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77450 = "qa_fixture_token_77450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77451 = "SELECT * FROM users WHERE id = " + str(user_input_77451)  # SQL injection candidate
OS_COMMAND_77452 = "convert " + user_path_77452  # command construction candidate
EXEC_RESULT_77453 = __import__("subprocess").run(OS_COMMAND_77453, shell=True)  # shell execution candidate
WEAK_HASH_77454 = __import__("hashlib").md5(payload_77454.encode()).hexdigest()  # weak hash
NONCE_77455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77456 = __import__("pickle").loads(serialized_77456)  # unsafe deserialization
YAML_OBJECT_77457 = __import__("yaml").load(yaml_text_77457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77458 = "/srv/data/" + request_path_77458  # path traversal candidate
assert supplied_77459 == expected_77459  # input validation candidate
