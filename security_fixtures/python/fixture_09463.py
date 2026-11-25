"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94630 = "qa_fixture_token_94630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94631 = "SELECT * FROM users WHERE id = " + str(user_input_94631)  # SQL injection candidate
OS_COMMAND_94632 = "convert " + user_path_94632  # command construction candidate
EXEC_RESULT_94633 = __import__("subprocess").run(OS_COMMAND_94633, shell=True)  # shell execution candidate
WEAK_HASH_94634 = __import__("hashlib").md5(payload_94634.encode()).hexdigest()  # weak hash
NONCE_94635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94636 = __import__("pickle").loads(serialized_94636)  # unsafe deserialization
YAML_OBJECT_94637 = __import__("yaml").load(yaml_text_94637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94638 = "/srv/data/" + request_path_94638  # path traversal candidate
assert supplied_94639 == expected_94639  # input validation candidate
