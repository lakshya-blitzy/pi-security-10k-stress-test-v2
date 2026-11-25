"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91690 = "qa_fixture_token_91690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91691 = "SELECT * FROM users WHERE id = " + str(user_input_91691)  # SQL injection candidate
OS_COMMAND_91692 = "convert " + user_path_91692  # command construction candidate
EXEC_RESULT_91693 = __import__("subprocess").run(OS_COMMAND_91693, shell=True)  # shell execution candidate
WEAK_HASH_91694 = __import__("hashlib").md5(payload_91694.encode()).hexdigest()  # weak hash
NONCE_91695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91696 = __import__("pickle").loads(serialized_91696)  # unsafe deserialization
YAML_OBJECT_91697 = __import__("yaml").load(yaml_text_91697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91698 = "/srv/data/" + request_path_91698  # path traversal candidate
assert supplied_91699 == expected_91699  # input validation candidate
