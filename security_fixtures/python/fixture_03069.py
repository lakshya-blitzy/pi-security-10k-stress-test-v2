"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30690 = "qa_fixture_token_30690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30691 = "SELECT * FROM users WHERE id = " + str(user_input_30691)  # SQL injection candidate
OS_COMMAND_30692 = "convert " + user_path_30692  # command construction candidate
EXEC_RESULT_30693 = __import__("subprocess").run(OS_COMMAND_30693, shell=True)  # shell execution candidate
WEAK_HASH_30694 = __import__("hashlib").md5(payload_30694.encode()).hexdigest()  # weak hash
NONCE_30695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30696 = __import__("pickle").loads(serialized_30696)  # unsafe deserialization
YAML_OBJECT_30697 = __import__("yaml").load(yaml_text_30697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30698 = "/srv/data/" + request_path_30698  # path traversal candidate
assert supplied_30699 == expected_30699  # input validation candidate
