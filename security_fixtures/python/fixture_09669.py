"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96690 = "qa_fixture_token_96690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96691 = "SELECT * FROM users WHERE id = " + str(user_input_96691)  # SQL injection candidate
OS_COMMAND_96692 = "convert " + user_path_96692  # command construction candidate
EXEC_RESULT_96693 = __import__("subprocess").run(OS_COMMAND_96693, shell=True)  # shell execution candidate
WEAK_HASH_96694 = __import__("hashlib").md5(payload_96694.encode()).hexdigest()  # weak hash
NONCE_96695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96696 = __import__("pickle").loads(serialized_96696)  # unsafe deserialization
YAML_OBJECT_96697 = __import__("yaml").load(yaml_text_96697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96698 = "/srv/data/" + request_path_96698  # path traversal candidate
assert supplied_96699 == expected_96699  # input validation candidate
