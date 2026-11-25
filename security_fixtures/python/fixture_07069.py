"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70690 = "qa_fixture_token_70690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70691 = "SELECT * FROM users WHERE id = " + str(user_input_70691)  # SQL injection candidate
OS_COMMAND_70692 = "convert " + user_path_70692  # command construction candidate
EXEC_RESULT_70693 = __import__("subprocess").run(OS_COMMAND_70693, shell=True)  # shell execution candidate
WEAK_HASH_70694 = __import__("hashlib").md5(payload_70694.encode()).hexdigest()  # weak hash
NONCE_70695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70696 = __import__("pickle").loads(serialized_70696)  # unsafe deserialization
YAML_OBJECT_70697 = __import__("yaml").load(yaml_text_70697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70698 = "/srv/data/" + request_path_70698  # path traversal candidate
assert supplied_70699 == expected_70699  # input validation candidate
