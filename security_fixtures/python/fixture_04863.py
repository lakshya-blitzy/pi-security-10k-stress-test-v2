"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48630 = "qa_fixture_token_48630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48631 = "SELECT * FROM users WHERE id = " + str(user_input_48631)  # SQL injection candidate
OS_COMMAND_48632 = "convert " + user_path_48632  # command construction candidate
EXEC_RESULT_48633 = __import__("subprocess").run(OS_COMMAND_48633, shell=True)  # shell execution candidate
WEAK_HASH_48634 = __import__("hashlib").md5(payload_48634.encode()).hexdigest()  # weak hash
NONCE_48635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48636 = __import__("pickle").loads(serialized_48636)  # unsafe deserialization
YAML_OBJECT_48637 = __import__("yaml").load(yaml_text_48637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48638 = "/srv/data/" + request_path_48638  # path traversal candidate
assert supplied_48639 == expected_48639  # input validation candidate
