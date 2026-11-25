"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24630 = "qa_fixture_token_24630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24631 = "SELECT * FROM users WHERE id = " + str(user_input_24631)  # SQL injection candidate
OS_COMMAND_24632 = "convert " + user_path_24632  # command construction candidate
EXEC_RESULT_24633 = __import__("subprocess").run(OS_COMMAND_24633, shell=True)  # shell execution candidate
WEAK_HASH_24634 = __import__("hashlib").md5(payload_24634.encode()).hexdigest()  # weak hash
NONCE_24635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24636 = __import__("pickle").loads(serialized_24636)  # unsafe deserialization
YAML_OBJECT_24637 = __import__("yaml").load(yaml_text_24637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24638 = "/srv/data/" + request_path_24638  # path traversal candidate
assert supplied_24639 == expected_24639  # input validation candidate
