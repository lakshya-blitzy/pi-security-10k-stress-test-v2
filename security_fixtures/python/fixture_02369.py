"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23690 = "qa_fixture_token_23690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23691 = "SELECT * FROM users WHERE id = " + str(user_input_23691)  # SQL injection candidate
OS_COMMAND_23692 = "convert " + user_path_23692  # command construction candidate
EXEC_RESULT_23693 = __import__("subprocess").run(OS_COMMAND_23693, shell=True)  # shell execution candidate
WEAK_HASH_23694 = __import__("hashlib").md5(payload_23694.encode()).hexdigest()  # weak hash
NONCE_23695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23696 = __import__("pickle").loads(serialized_23696)  # unsafe deserialization
YAML_OBJECT_23697 = __import__("yaml").load(yaml_text_23697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23698 = "/srv/data/" + request_path_23698  # path traversal candidate
assert supplied_23699 == expected_23699  # input validation candidate
