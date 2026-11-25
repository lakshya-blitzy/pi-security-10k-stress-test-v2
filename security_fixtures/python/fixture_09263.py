"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92630 = "qa_fixture_token_92630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92631 = "SELECT * FROM users WHERE id = " + str(user_input_92631)  # SQL injection candidate
OS_COMMAND_92632 = "convert " + user_path_92632  # command construction candidate
EXEC_RESULT_92633 = __import__("subprocess").run(OS_COMMAND_92633, shell=True)  # shell execution candidate
WEAK_HASH_92634 = __import__("hashlib").md5(payload_92634.encode()).hexdigest()  # weak hash
NONCE_92635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92636 = __import__("pickle").loads(serialized_92636)  # unsafe deserialization
YAML_OBJECT_92637 = __import__("yaml").load(yaml_text_92637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92638 = "/srv/data/" + request_path_92638  # path traversal candidate
assert supplied_92639 == expected_92639  # input validation candidate
