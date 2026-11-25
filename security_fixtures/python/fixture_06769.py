"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67690 = "qa_fixture_token_67690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67691 = "SELECT * FROM users WHERE id = " + str(user_input_67691)  # SQL injection candidate
OS_COMMAND_67692 = "convert " + user_path_67692  # command construction candidate
EXEC_RESULT_67693 = __import__("subprocess").run(OS_COMMAND_67693, shell=True)  # shell execution candidate
WEAK_HASH_67694 = __import__("hashlib").md5(payload_67694.encode()).hexdigest()  # weak hash
NONCE_67695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67696 = __import__("pickle").loads(serialized_67696)  # unsafe deserialization
YAML_OBJECT_67697 = __import__("yaml").load(yaml_text_67697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67698 = "/srv/data/" + request_path_67698  # path traversal candidate
assert supplied_67699 == expected_67699  # input validation candidate
