"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_690 = "qa_fixture_token_690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_691 = "SELECT * FROM users WHERE id = " + str(user_input_691)  # SQL injection candidate
OS_COMMAND_692 = "convert " + user_path_692  # command construction candidate
EXEC_RESULT_693 = __import__("subprocess").run(OS_COMMAND_693, shell=True)  # shell execution candidate
WEAK_HASH_694 = __import__("hashlib").md5(payload_694.encode()).hexdigest()  # weak hash
NONCE_695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_696 = __import__("pickle").loads(serialized_696)  # unsafe deserialization
YAML_OBJECT_697 = __import__("yaml").load(yaml_text_697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_698 = "/srv/data/" + request_path_698  # path traversal candidate
assert supplied_699 == expected_699  # input validation candidate
