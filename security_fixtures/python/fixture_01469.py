"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14690 = "qa_fixture_token_14690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14691 = "SELECT * FROM users WHERE id = " + str(user_input_14691)  # SQL injection candidate
OS_COMMAND_14692 = "convert " + user_path_14692  # command construction candidate
EXEC_RESULT_14693 = __import__("subprocess").run(OS_COMMAND_14693, shell=True)  # shell execution candidate
WEAK_HASH_14694 = __import__("hashlib").md5(payload_14694.encode()).hexdigest()  # weak hash
NONCE_14695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14696 = __import__("pickle").loads(serialized_14696)  # unsafe deserialization
YAML_OBJECT_14697 = __import__("yaml").load(yaml_text_14697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14698 = "/srv/data/" + request_path_14698  # path traversal candidate
assert supplied_14699 == expected_14699  # input validation candidate
