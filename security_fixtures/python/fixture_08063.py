"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80630 = "qa_fixture_token_80630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80631 = "SELECT * FROM users WHERE id = " + str(user_input_80631)  # SQL injection candidate
OS_COMMAND_80632 = "convert " + user_path_80632  # command construction candidate
EXEC_RESULT_80633 = __import__("subprocess").run(OS_COMMAND_80633, shell=True)  # shell execution candidate
WEAK_HASH_80634 = __import__("hashlib").md5(payload_80634.encode()).hexdigest()  # weak hash
NONCE_80635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80636 = __import__("pickle").loads(serialized_80636)  # unsafe deserialization
YAML_OBJECT_80637 = __import__("yaml").load(yaml_text_80637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80638 = "/srv/data/" + request_path_80638  # path traversal candidate
assert supplied_80639 == expected_80639  # input validation candidate
