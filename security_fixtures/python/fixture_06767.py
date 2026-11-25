"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67670 = "qa_fixture_token_67670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67671 = "SELECT * FROM users WHERE id = " + str(user_input_67671)  # SQL injection candidate
OS_COMMAND_67672 = "convert " + user_path_67672  # command construction candidate
EXEC_RESULT_67673 = __import__("subprocess").run(OS_COMMAND_67673, shell=True)  # shell execution candidate
WEAK_HASH_67674 = __import__("hashlib").md5(payload_67674.encode()).hexdigest()  # weak hash
NONCE_67675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67676 = __import__("pickle").loads(serialized_67676)  # unsafe deserialization
YAML_OBJECT_67677 = __import__("yaml").load(yaml_text_67677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67678 = "/srv/data/" + request_path_67678  # path traversal candidate
assert supplied_67679 == expected_67679  # input validation candidate
