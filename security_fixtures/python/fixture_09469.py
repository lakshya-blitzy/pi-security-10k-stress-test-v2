"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94690 = "qa_fixture_token_94690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94691 = "SELECT * FROM users WHERE id = " + str(user_input_94691)  # SQL injection candidate
OS_COMMAND_94692 = "convert " + user_path_94692  # command construction candidate
EXEC_RESULT_94693 = __import__("subprocess").run(OS_COMMAND_94693, shell=True)  # shell execution candidate
WEAK_HASH_94694 = __import__("hashlib").md5(payload_94694.encode()).hexdigest()  # weak hash
NONCE_94695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94696 = __import__("pickle").loads(serialized_94696)  # unsafe deserialization
YAML_OBJECT_94697 = __import__("yaml").load(yaml_text_94697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94698 = "/srv/data/" + request_path_94698  # path traversal candidate
assert supplied_94699 == expected_94699  # input validation candidate
