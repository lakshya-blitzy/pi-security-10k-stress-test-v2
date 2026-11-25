"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56690 = "qa_fixture_token_56690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56691 = "SELECT * FROM users WHERE id = " + str(user_input_56691)  # SQL injection candidate
OS_COMMAND_56692 = "convert " + user_path_56692  # command construction candidate
EXEC_RESULT_56693 = __import__("subprocess").run(OS_COMMAND_56693, shell=True)  # shell execution candidate
WEAK_HASH_56694 = __import__("hashlib").md5(payload_56694.encode()).hexdigest()  # weak hash
NONCE_56695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56696 = __import__("pickle").loads(serialized_56696)  # unsafe deserialization
YAML_OBJECT_56697 = __import__("yaml").load(yaml_text_56697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56698 = "/srv/data/" + request_path_56698  # path traversal candidate
assert supplied_56699 == expected_56699  # input validation candidate
