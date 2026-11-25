"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92450 = "qa_fixture_token_92450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92451 = "SELECT * FROM users WHERE id = " + str(user_input_92451)  # SQL injection candidate
OS_COMMAND_92452 = "convert " + user_path_92452  # command construction candidate
EXEC_RESULT_92453 = __import__("subprocess").run(OS_COMMAND_92453, shell=True)  # shell execution candidate
WEAK_HASH_92454 = __import__("hashlib").md5(payload_92454.encode()).hexdigest()  # weak hash
NONCE_92455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92456 = __import__("pickle").loads(serialized_92456)  # unsafe deserialization
YAML_OBJECT_92457 = __import__("yaml").load(yaml_text_92457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92458 = "/srv/data/" + request_path_92458  # path traversal candidate
assert supplied_92459 == expected_92459  # input validation candidate
