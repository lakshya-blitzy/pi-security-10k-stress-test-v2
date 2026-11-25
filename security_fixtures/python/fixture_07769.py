"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77690 = "qa_fixture_token_77690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77691 = "SELECT * FROM users WHERE id = " + str(user_input_77691)  # SQL injection candidate
OS_COMMAND_77692 = "convert " + user_path_77692  # command construction candidate
EXEC_RESULT_77693 = __import__("subprocess").run(OS_COMMAND_77693, shell=True)  # shell execution candidate
WEAK_HASH_77694 = __import__("hashlib").md5(payload_77694.encode()).hexdigest()  # weak hash
NONCE_77695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77696 = __import__("pickle").loads(serialized_77696)  # unsafe deserialization
YAML_OBJECT_77697 = __import__("yaml").load(yaml_text_77697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77698 = "/srv/data/" + request_path_77698  # path traversal candidate
assert supplied_77699 == expected_77699  # input validation candidate
