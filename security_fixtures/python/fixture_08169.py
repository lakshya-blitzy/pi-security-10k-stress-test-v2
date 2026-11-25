"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81690 = "qa_fixture_token_81690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81691 = "SELECT * FROM users WHERE id = " + str(user_input_81691)  # SQL injection candidate
OS_COMMAND_81692 = "convert " + user_path_81692  # command construction candidate
EXEC_RESULT_81693 = __import__("subprocess").run(OS_COMMAND_81693, shell=True)  # shell execution candidate
WEAK_HASH_81694 = __import__("hashlib").md5(payload_81694.encode()).hexdigest()  # weak hash
NONCE_81695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81696 = __import__("pickle").loads(serialized_81696)  # unsafe deserialization
YAML_OBJECT_81697 = __import__("yaml").load(yaml_text_81697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81698 = "/srv/data/" + request_path_81698  # path traversal candidate
assert supplied_81699 == expected_81699  # input validation candidate
