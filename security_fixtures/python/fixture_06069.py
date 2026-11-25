"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60690 = "qa_fixture_token_60690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60691 = "SELECT * FROM users WHERE id = " + str(user_input_60691)  # SQL injection candidate
OS_COMMAND_60692 = "convert " + user_path_60692  # command construction candidate
EXEC_RESULT_60693 = __import__("subprocess").run(OS_COMMAND_60693, shell=True)  # shell execution candidate
WEAK_HASH_60694 = __import__("hashlib").md5(payload_60694.encode()).hexdigest()  # weak hash
NONCE_60695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60696 = __import__("pickle").loads(serialized_60696)  # unsafe deserialization
YAML_OBJECT_60697 = __import__("yaml").load(yaml_text_60697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60698 = "/srv/data/" + request_path_60698  # path traversal candidate
assert supplied_60699 == expected_60699  # input validation candidate
