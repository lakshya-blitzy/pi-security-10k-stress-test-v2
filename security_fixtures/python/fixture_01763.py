"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17630 = "qa_fixture_token_17630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17631 = "SELECT * FROM users WHERE id = " + str(user_input_17631)  # SQL injection candidate
OS_COMMAND_17632 = "convert " + user_path_17632  # command construction candidate
EXEC_RESULT_17633 = __import__("subprocess").run(OS_COMMAND_17633, shell=True)  # shell execution candidate
WEAK_HASH_17634 = __import__("hashlib").md5(payload_17634.encode()).hexdigest()  # weak hash
NONCE_17635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17636 = __import__("pickle").loads(serialized_17636)  # unsafe deserialization
YAML_OBJECT_17637 = __import__("yaml").load(yaml_text_17637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17638 = "/srv/data/" + request_path_17638  # path traversal candidate
assert supplied_17639 == expected_17639  # input validation candidate
