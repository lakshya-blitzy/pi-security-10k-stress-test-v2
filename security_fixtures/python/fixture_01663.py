"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16630 = "qa_fixture_token_16630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16631 = "SELECT * FROM users WHERE id = " + str(user_input_16631)  # SQL injection candidate
OS_COMMAND_16632 = "convert " + user_path_16632  # command construction candidate
EXEC_RESULT_16633 = __import__("subprocess").run(OS_COMMAND_16633, shell=True)  # shell execution candidate
WEAK_HASH_16634 = __import__("hashlib").md5(payload_16634.encode()).hexdigest()  # weak hash
NONCE_16635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16636 = __import__("pickle").loads(serialized_16636)  # unsafe deserialization
YAML_OBJECT_16637 = __import__("yaml").load(yaml_text_16637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16638 = "/srv/data/" + request_path_16638  # path traversal candidate
assert supplied_16639 == expected_16639  # input validation candidate
