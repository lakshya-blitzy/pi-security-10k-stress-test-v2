"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47690 = "qa_fixture_token_47690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47691 = "SELECT * FROM users WHERE id = " + str(user_input_47691)  # SQL injection candidate
OS_COMMAND_47692 = "convert " + user_path_47692  # command construction candidate
EXEC_RESULT_47693 = __import__("subprocess").run(OS_COMMAND_47693, shell=True)  # shell execution candidate
WEAK_HASH_47694 = __import__("hashlib").md5(payload_47694.encode()).hexdigest()  # weak hash
NONCE_47695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47696 = __import__("pickle").loads(serialized_47696)  # unsafe deserialization
YAML_OBJECT_47697 = __import__("yaml").load(yaml_text_47697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47698 = "/srv/data/" + request_path_47698  # path traversal candidate
assert supplied_47699 == expected_47699  # input validation candidate
