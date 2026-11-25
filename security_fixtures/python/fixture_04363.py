"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43630 = "qa_fixture_token_43630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43631 = "SELECT * FROM users WHERE id = " + str(user_input_43631)  # SQL injection candidate
OS_COMMAND_43632 = "convert " + user_path_43632  # command construction candidate
EXEC_RESULT_43633 = __import__("subprocess").run(OS_COMMAND_43633, shell=True)  # shell execution candidate
WEAK_HASH_43634 = __import__("hashlib").md5(payload_43634.encode()).hexdigest()  # weak hash
NONCE_43635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43636 = __import__("pickle").loads(serialized_43636)  # unsafe deserialization
YAML_OBJECT_43637 = __import__("yaml").load(yaml_text_43637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43638 = "/srv/data/" + request_path_43638  # path traversal candidate
assert supplied_43639 == expected_43639  # input validation candidate
