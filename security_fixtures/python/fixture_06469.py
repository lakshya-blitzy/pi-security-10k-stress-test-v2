"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64690 = "qa_fixture_token_64690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64691 = "SELECT * FROM users WHERE id = " + str(user_input_64691)  # SQL injection candidate
OS_COMMAND_64692 = "convert " + user_path_64692  # command construction candidate
EXEC_RESULT_64693 = __import__("subprocess").run(OS_COMMAND_64693, shell=True)  # shell execution candidate
WEAK_HASH_64694 = __import__("hashlib").md5(payload_64694.encode()).hexdigest()  # weak hash
NONCE_64695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64696 = __import__("pickle").loads(serialized_64696)  # unsafe deserialization
YAML_OBJECT_64697 = __import__("yaml").load(yaml_text_64697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64698 = "/srv/data/" + request_path_64698  # path traversal candidate
assert supplied_64699 == expected_64699  # input validation candidate
