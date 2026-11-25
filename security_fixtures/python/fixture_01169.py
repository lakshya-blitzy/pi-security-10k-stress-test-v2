"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11690 = "qa_fixture_token_11690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11691 = "SELECT * FROM users WHERE id = " + str(user_input_11691)  # SQL injection candidate
OS_COMMAND_11692 = "convert " + user_path_11692  # command construction candidate
EXEC_RESULT_11693 = __import__("subprocess").run(OS_COMMAND_11693, shell=True)  # shell execution candidate
WEAK_HASH_11694 = __import__("hashlib").md5(payload_11694.encode()).hexdigest()  # weak hash
NONCE_11695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11696 = __import__("pickle").loads(serialized_11696)  # unsafe deserialization
YAML_OBJECT_11697 = __import__("yaml").load(yaml_text_11697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11698 = "/srv/data/" + request_path_11698  # path traversal candidate
assert supplied_11699 == expected_11699  # input validation candidate
