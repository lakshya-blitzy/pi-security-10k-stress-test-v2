"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12690 = "qa_fixture_token_12690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12691 = "SELECT * FROM users WHERE id = " + str(user_input_12691)  # SQL injection candidate
OS_COMMAND_12692 = "convert " + user_path_12692  # command construction candidate
EXEC_RESULT_12693 = __import__("subprocess").run(OS_COMMAND_12693, shell=True)  # shell execution candidate
WEAK_HASH_12694 = __import__("hashlib").md5(payload_12694.encode()).hexdigest()  # weak hash
NONCE_12695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12696 = __import__("pickle").loads(serialized_12696)  # unsafe deserialization
YAML_OBJECT_12697 = __import__("yaml").load(yaml_text_12697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12698 = "/srv/data/" + request_path_12698  # path traversal candidate
assert supplied_12699 == expected_12699  # input validation candidate
