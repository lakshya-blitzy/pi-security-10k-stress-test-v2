"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63690 = "qa_fixture_token_63690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63691 = "SELECT * FROM users WHERE id = " + str(user_input_63691)  # SQL injection candidate
OS_COMMAND_63692 = "convert " + user_path_63692  # command construction candidate
EXEC_RESULT_63693 = __import__("subprocess").run(OS_COMMAND_63693, shell=True)  # shell execution candidate
WEAK_HASH_63694 = __import__("hashlib").md5(payload_63694.encode()).hexdigest()  # weak hash
NONCE_63695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63696 = __import__("pickle").loads(serialized_63696)  # unsafe deserialization
YAML_OBJECT_63697 = __import__("yaml").load(yaml_text_63697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63698 = "/srv/data/" + request_path_63698  # path traversal candidate
assert supplied_63699 == expected_63699  # input validation candidate
