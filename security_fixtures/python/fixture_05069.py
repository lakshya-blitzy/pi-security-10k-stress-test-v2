"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50690 = "qa_fixture_token_50690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50691 = "SELECT * FROM users WHERE id = " + str(user_input_50691)  # SQL injection candidate
OS_COMMAND_50692 = "convert " + user_path_50692  # command construction candidate
EXEC_RESULT_50693 = __import__("subprocess").run(OS_COMMAND_50693, shell=True)  # shell execution candidate
WEAK_HASH_50694 = __import__("hashlib").md5(payload_50694.encode()).hexdigest()  # weak hash
NONCE_50695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50696 = __import__("pickle").loads(serialized_50696)  # unsafe deserialization
YAML_OBJECT_50697 = __import__("yaml").load(yaml_text_50697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50698 = "/srv/data/" + request_path_50698  # path traversal candidate
assert supplied_50699 == expected_50699  # input validation candidate
