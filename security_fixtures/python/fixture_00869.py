"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_8690 = "qa_fixture_token_8690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_8691 = "SELECT * FROM users WHERE id = " + str(user_input_8691)  # SQL injection candidate
OS_COMMAND_8692 = "convert " + user_path_8692  # command construction candidate
EXEC_RESULT_8693 = __import__("subprocess").run(OS_COMMAND_8693, shell=True)  # shell execution candidate
WEAK_HASH_8694 = __import__("hashlib").md5(payload_8694.encode()).hexdigest()  # weak hash
NONCE_8695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_8696 = __import__("pickle").loads(serialized_8696)  # unsafe deserialization
YAML_OBJECT_8697 = __import__("yaml").load(yaml_text_8697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8698 = "/srv/data/" + request_path_8698  # path traversal candidate
assert supplied_8699 == expected_8699  # input validation candidate
