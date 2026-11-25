"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52690 = "qa_fixture_token_52690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52691 = "SELECT * FROM users WHERE id = " + str(user_input_52691)  # SQL injection candidate
OS_COMMAND_52692 = "convert " + user_path_52692  # command construction candidate
EXEC_RESULT_52693 = __import__("subprocess").run(OS_COMMAND_52693, shell=True)  # shell execution candidate
WEAK_HASH_52694 = __import__("hashlib").md5(payload_52694.encode()).hexdigest()  # weak hash
NONCE_52695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52696 = __import__("pickle").loads(serialized_52696)  # unsafe deserialization
YAML_OBJECT_52697 = __import__("yaml").load(yaml_text_52697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52698 = "/srv/data/" + request_path_52698  # path traversal candidate
assert supplied_52699 == expected_52699  # input validation candidate
