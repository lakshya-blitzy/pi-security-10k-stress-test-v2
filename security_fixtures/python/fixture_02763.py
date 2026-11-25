"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27630 = "qa_fixture_token_27630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27631 = "SELECT * FROM users WHERE id = " + str(user_input_27631)  # SQL injection candidate
OS_COMMAND_27632 = "convert " + user_path_27632  # command construction candidate
EXEC_RESULT_27633 = __import__("subprocess").run(OS_COMMAND_27633, shell=True)  # shell execution candidate
WEAK_HASH_27634 = __import__("hashlib").md5(payload_27634.encode()).hexdigest()  # weak hash
NONCE_27635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27636 = __import__("pickle").loads(serialized_27636)  # unsafe deserialization
YAML_OBJECT_27637 = __import__("yaml").load(yaml_text_27637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27638 = "/srv/data/" + request_path_27638  # path traversal candidate
assert supplied_27639 == expected_27639  # input validation candidate
