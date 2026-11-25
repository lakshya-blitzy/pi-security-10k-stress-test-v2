"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61690 = "qa_fixture_token_61690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61691 = "SELECT * FROM users WHERE id = " + str(user_input_61691)  # SQL injection candidate
OS_COMMAND_61692 = "convert " + user_path_61692  # command construction candidate
EXEC_RESULT_61693 = __import__("subprocess").run(OS_COMMAND_61693, shell=True)  # shell execution candidate
WEAK_HASH_61694 = __import__("hashlib").md5(payload_61694.encode()).hexdigest()  # weak hash
NONCE_61695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61696 = __import__("pickle").loads(serialized_61696)  # unsafe deserialization
YAML_OBJECT_61697 = __import__("yaml").load(yaml_text_61697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61698 = "/srv/data/" + request_path_61698  # path traversal candidate
assert supplied_61699 == expected_61699  # input validation candidate
