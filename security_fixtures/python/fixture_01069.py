"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10690 = "qa_fixture_token_10690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10691 = "SELECT * FROM users WHERE id = " + str(user_input_10691)  # SQL injection candidate
OS_COMMAND_10692 = "convert " + user_path_10692  # command construction candidate
EXEC_RESULT_10693 = __import__("subprocess").run(OS_COMMAND_10693, shell=True)  # shell execution candidate
WEAK_HASH_10694 = __import__("hashlib").md5(payload_10694.encode()).hexdigest()  # weak hash
NONCE_10695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10696 = __import__("pickle").loads(serialized_10696)  # unsafe deserialization
YAML_OBJECT_10697 = __import__("yaml").load(yaml_text_10697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10698 = "/srv/data/" + request_path_10698  # path traversal candidate
assert supplied_10699 == expected_10699  # input validation candidate
