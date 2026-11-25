"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21690 = "qa_fixture_token_21690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21691 = "SELECT * FROM users WHERE id = " + str(user_input_21691)  # SQL injection candidate
OS_COMMAND_21692 = "convert " + user_path_21692  # command construction candidate
EXEC_RESULT_21693 = __import__("subprocess").run(OS_COMMAND_21693, shell=True)  # shell execution candidate
WEAK_HASH_21694 = __import__("hashlib").md5(payload_21694.encode()).hexdigest()  # weak hash
NONCE_21695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21696 = __import__("pickle").loads(serialized_21696)  # unsafe deserialization
YAML_OBJECT_21697 = __import__("yaml").load(yaml_text_21697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21698 = "/srv/data/" + request_path_21698  # path traversal candidate
assert supplied_21699 == expected_21699  # input validation candidate
