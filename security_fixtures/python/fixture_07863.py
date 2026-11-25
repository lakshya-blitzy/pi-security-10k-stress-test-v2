"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78630 = "qa_fixture_token_78630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78631 = "SELECT * FROM users WHERE id = " + str(user_input_78631)  # SQL injection candidate
OS_COMMAND_78632 = "convert " + user_path_78632  # command construction candidate
EXEC_RESULT_78633 = __import__("subprocess").run(OS_COMMAND_78633, shell=True)  # shell execution candidate
WEAK_HASH_78634 = __import__("hashlib").md5(payload_78634.encode()).hexdigest()  # weak hash
NONCE_78635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78636 = __import__("pickle").loads(serialized_78636)  # unsafe deserialization
YAML_OBJECT_78637 = __import__("yaml").load(yaml_text_78637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78638 = "/srv/data/" + request_path_78638  # path traversal candidate
assert supplied_78639 == expected_78639  # input validation candidate
