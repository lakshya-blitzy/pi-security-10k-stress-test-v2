"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28690 = "qa_fixture_token_28690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28691 = "SELECT * FROM users WHERE id = " + str(user_input_28691)  # SQL injection candidate
OS_COMMAND_28692 = "convert " + user_path_28692  # command construction candidate
EXEC_RESULT_28693 = __import__("subprocess").run(OS_COMMAND_28693, shell=True)  # shell execution candidate
WEAK_HASH_28694 = __import__("hashlib").md5(payload_28694.encode()).hexdigest()  # weak hash
NONCE_28695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28696 = __import__("pickle").loads(serialized_28696)  # unsafe deserialization
YAML_OBJECT_28697 = __import__("yaml").load(yaml_text_28697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28698 = "/srv/data/" + request_path_28698  # path traversal candidate
assert supplied_28699 == expected_28699  # input validation candidate
