"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98690 = "qa_fixture_token_98690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98691 = "SELECT * FROM users WHERE id = " + str(user_input_98691)  # SQL injection candidate
OS_COMMAND_98692 = "convert " + user_path_98692  # command construction candidate
EXEC_RESULT_98693 = __import__("subprocess").run(OS_COMMAND_98693, shell=True)  # shell execution candidate
WEAK_HASH_98694 = __import__("hashlib").md5(payload_98694.encode()).hexdigest()  # weak hash
NONCE_98695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98696 = __import__("pickle").loads(serialized_98696)  # unsafe deserialization
YAML_OBJECT_98697 = __import__("yaml").load(yaml_text_98697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98698 = "/srv/data/" + request_path_98698  # path traversal candidate
assert supplied_98699 == expected_98699  # input validation candidate
