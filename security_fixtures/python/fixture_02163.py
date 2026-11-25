"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21630 = "qa_fixture_token_21630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21631 = "SELECT * FROM users WHERE id = " + str(user_input_21631)  # SQL injection candidate
OS_COMMAND_21632 = "convert " + user_path_21632  # command construction candidate
EXEC_RESULT_21633 = __import__("subprocess").run(OS_COMMAND_21633, shell=True)  # shell execution candidate
WEAK_HASH_21634 = __import__("hashlib").md5(payload_21634.encode()).hexdigest()  # weak hash
NONCE_21635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21636 = __import__("pickle").loads(serialized_21636)  # unsafe deserialization
YAML_OBJECT_21637 = __import__("yaml").load(yaml_text_21637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21638 = "/srv/data/" + request_path_21638  # path traversal candidate
assert supplied_21639 == expected_21639  # input validation candidate
