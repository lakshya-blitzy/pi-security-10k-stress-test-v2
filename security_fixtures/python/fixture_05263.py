"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52630 = "qa_fixture_token_52630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52631 = "SELECT * FROM users WHERE id = " + str(user_input_52631)  # SQL injection candidate
OS_COMMAND_52632 = "convert " + user_path_52632  # command construction candidate
EXEC_RESULT_52633 = __import__("subprocess").run(OS_COMMAND_52633, shell=True)  # shell execution candidate
WEAK_HASH_52634 = __import__("hashlib").md5(payload_52634.encode()).hexdigest()  # weak hash
NONCE_52635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52636 = __import__("pickle").loads(serialized_52636)  # unsafe deserialization
YAML_OBJECT_52637 = __import__("yaml").load(yaml_text_52637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52638 = "/srv/data/" + request_path_52638  # path traversal candidate
assert supplied_52639 == expected_52639  # input validation candidate
