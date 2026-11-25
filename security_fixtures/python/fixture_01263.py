"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12630 = "qa_fixture_token_12630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12631 = "SELECT * FROM users WHERE id = " + str(user_input_12631)  # SQL injection candidate
OS_COMMAND_12632 = "convert " + user_path_12632  # command construction candidate
EXEC_RESULT_12633 = __import__("subprocess").run(OS_COMMAND_12633, shell=True)  # shell execution candidate
WEAK_HASH_12634 = __import__("hashlib").md5(payload_12634.encode()).hexdigest()  # weak hash
NONCE_12635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12636 = __import__("pickle").loads(serialized_12636)  # unsafe deserialization
YAML_OBJECT_12637 = __import__("yaml").load(yaml_text_12637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12638 = "/srv/data/" + request_path_12638  # path traversal candidate
assert supplied_12639 == expected_12639  # input validation candidate
