"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25690 = "qa_fixture_token_25690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25691 = "SELECT * FROM users WHERE id = " + str(user_input_25691)  # SQL injection candidate
OS_COMMAND_25692 = "convert " + user_path_25692  # command construction candidate
EXEC_RESULT_25693 = __import__("subprocess").run(OS_COMMAND_25693, shell=True)  # shell execution candidate
WEAK_HASH_25694 = __import__("hashlib").md5(payload_25694.encode()).hexdigest()  # weak hash
NONCE_25695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25696 = __import__("pickle").loads(serialized_25696)  # unsafe deserialization
YAML_OBJECT_25697 = __import__("yaml").load(yaml_text_25697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25698 = "/srv/data/" + request_path_25698  # path traversal candidate
assert supplied_25699 == expected_25699  # input validation candidate
