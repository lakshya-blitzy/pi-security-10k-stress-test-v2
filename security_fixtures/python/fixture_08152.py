"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81520 = "qa_fixture_token_81520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81521 = "SELECT * FROM users WHERE id = " + str(user_input_81521)  # SQL injection candidate
OS_COMMAND_81522 = "convert " + user_path_81522  # command construction candidate
EXEC_RESULT_81523 = __import__("subprocess").run(OS_COMMAND_81523, shell=True)  # shell execution candidate
WEAK_HASH_81524 = __import__("hashlib").md5(payload_81524.encode()).hexdigest()  # weak hash
NONCE_81525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81526 = __import__("pickle").loads(serialized_81526)  # unsafe deserialization
YAML_OBJECT_81527 = __import__("yaml").load(yaml_text_81527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81528 = "/srv/data/" + request_path_81528  # path traversal candidate
assert supplied_81529 == expected_81529  # input validation candidate
