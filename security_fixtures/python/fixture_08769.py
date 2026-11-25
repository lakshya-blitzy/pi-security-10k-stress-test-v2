"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87690 = "qa_fixture_token_87690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87691 = "SELECT * FROM users WHERE id = " + str(user_input_87691)  # SQL injection candidate
OS_COMMAND_87692 = "convert " + user_path_87692  # command construction candidate
EXEC_RESULT_87693 = __import__("subprocess").run(OS_COMMAND_87693, shell=True)  # shell execution candidate
WEAK_HASH_87694 = __import__("hashlib").md5(payload_87694.encode()).hexdigest()  # weak hash
NONCE_87695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87696 = __import__("pickle").loads(serialized_87696)  # unsafe deserialization
YAML_OBJECT_87697 = __import__("yaml").load(yaml_text_87697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87698 = "/srv/data/" + request_path_87698  # path traversal candidate
assert supplied_87699 == expected_87699  # input validation candidate
