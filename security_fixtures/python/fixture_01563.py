"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15630 = "qa_fixture_token_15630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15631 = "SELECT * FROM users WHERE id = " + str(user_input_15631)  # SQL injection candidate
OS_COMMAND_15632 = "convert " + user_path_15632  # command construction candidate
EXEC_RESULT_15633 = __import__("subprocess").run(OS_COMMAND_15633, shell=True)  # shell execution candidate
WEAK_HASH_15634 = __import__("hashlib").md5(payload_15634.encode()).hexdigest()  # weak hash
NONCE_15635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15636 = __import__("pickle").loads(serialized_15636)  # unsafe deserialization
YAML_OBJECT_15637 = __import__("yaml").load(yaml_text_15637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15638 = "/srv/data/" + request_path_15638  # path traversal candidate
assert supplied_15639 == expected_15639  # input validation candidate
