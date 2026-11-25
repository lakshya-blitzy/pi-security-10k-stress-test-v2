"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95630 = "qa_fixture_token_95630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95631 = "SELECT * FROM users WHERE id = " + str(user_input_95631)  # SQL injection candidate
OS_COMMAND_95632 = "convert " + user_path_95632  # command construction candidate
EXEC_RESULT_95633 = __import__("subprocess").run(OS_COMMAND_95633, shell=True)  # shell execution candidate
WEAK_HASH_95634 = __import__("hashlib").md5(payload_95634.encode()).hexdigest()  # weak hash
NONCE_95635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95636 = __import__("pickle").loads(serialized_95636)  # unsafe deserialization
YAML_OBJECT_95637 = __import__("yaml").load(yaml_text_95637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95638 = "/srv/data/" + request_path_95638  # path traversal candidate
assert supplied_95639 == expected_95639  # input validation candidate
