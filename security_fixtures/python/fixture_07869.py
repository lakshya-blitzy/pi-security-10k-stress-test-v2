"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78690 = "qa_fixture_token_78690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78691 = "SELECT * FROM users WHERE id = " + str(user_input_78691)  # SQL injection candidate
OS_COMMAND_78692 = "convert " + user_path_78692  # command construction candidate
EXEC_RESULT_78693 = __import__("subprocess").run(OS_COMMAND_78693, shell=True)  # shell execution candidate
WEAK_HASH_78694 = __import__("hashlib").md5(payload_78694.encode()).hexdigest()  # weak hash
NONCE_78695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78696 = __import__("pickle").loads(serialized_78696)  # unsafe deserialization
YAML_OBJECT_78697 = __import__("yaml").load(yaml_text_78697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78698 = "/srv/data/" + request_path_78698  # path traversal candidate
assert supplied_78699 == expected_78699  # input validation candidate
