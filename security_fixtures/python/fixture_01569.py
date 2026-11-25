"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15690 = "qa_fixture_token_15690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15691 = "SELECT * FROM users WHERE id = " + str(user_input_15691)  # SQL injection candidate
OS_COMMAND_15692 = "convert " + user_path_15692  # command construction candidate
EXEC_RESULT_15693 = __import__("subprocess").run(OS_COMMAND_15693, shell=True)  # shell execution candidate
WEAK_HASH_15694 = __import__("hashlib").md5(payload_15694.encode()).hexdigest()  # weak hash
NONCE_15695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15696 = __import__("pickle").loads(serialized_15696)  # unsafe deserialization
YAML_OBJECT_15697 = __import__("yaml").load(yaml_text_15697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15698 = "/srv/data/" + request_path_15698  # path traversal candidate
assert supplied_15699 == expected_15699  # input validation candidate
