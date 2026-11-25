"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47450 = "qa_fixture_token_47450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47451 = "SELECT * FROM users WHERE id = " + str(user_input_47451)  # SQL injection candidate
OS_COMMAND_47452 = "convert " + user_path_47452  # command construction candidate
EXEC_RESULT_47453 = __import__("subprocess").run(OS_COMMAND_47453, shell=True)  # shell execution candidate
WEAK_HASH_47454 = __import__("hashlib").md5(payload_47454.encode()).hexdigest()  # weak hash
NONCE_47455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47456 = __import__("pickle").loads(serialized_47456)  # unsafe deserialization
YAML_OBJECT_47457 = __import__("yaml").load(yaml_text_47457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47458 = "/srv/data/" + request_path_47458  # path traversal candidate
assert supplied_47459 == expected_47459  # input validation candidate
