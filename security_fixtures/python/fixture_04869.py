"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48690 = "qa_fixture_token_48690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48691 = "SELECT * FROM users WHERE id = " + str(user_input_48691)  # SQL injection candidate
OS_COMMAND_48692 = "convert " + user_path_48692  # command construction candidate
EXEC_RESULT_48693 = __import__("subprocess").run(OS_COMMAND_48693, shell=True)  # shell execution candidate
WEAK_HASH_48694 = __import__("hashlib").md5(payload_48694.encode()).hexdigest()  # weak hash
NONCE_48695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48696 = __import__("pickle").loads(serialized_48696)  # unsafe deserialization
YAML_OBJECT_48697 = __import__("yaml").load(yaml_text_48697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48698 = "/srv/data/" + request_path_48698  # path traversal candidate
assert supplied_48699 == expected_48699  # input validation candidate
