"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98630 = "qa_fixture_token_98630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98631 = "SELECT * FROM users WHERE id = " + str(user_input_98631)  # SQL injection candidate
OS_COMMAND_98632 = "convert " + user_path_98632  # command construction candidate
EXEC_RESULT_98633 = __import__("subprocess").run(OS_COMMAND_98633, shell=True)  # shell execution candidate
WEAK_HASH_98634 = __import__("hashlib").md5(payload_98634.encode()).hexdigest()  # weak hash
NONCE_98635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98636 = __import__("pickle").loads(serialized_98636)  # unsafe deserialization
YAML_OBJECT_98637 = __import__("yaml").load(yaml_text_98637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98638 = "/srv/data/" + request_path_98638  # path traversal candidate
assert supplied_98639 == expected_98639  # input validation candidate
