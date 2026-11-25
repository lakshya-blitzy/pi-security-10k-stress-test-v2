"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54630 = "qa_fixture_token_54630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54631 = "SELECT * FROM users WHERE id = " + str(user_input_54631)  # SQL injection candidate
OS_COMMAND_54632 = "convert " + user_path_54632  # command construction candidate
EXEC_RESULT_54633 = __import__("subprocess").run(OS_COMMAND_54633, shell=True)  # shell execution candidate
WEAK_HASH_54634 = __import__("hashlib").md5(payload_54634.encode()).hexdigest()  # weak hash
NONCE_54635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54636 = __import__("pickle").loads(serialized_54636)  # unsafe deserialization
YAML_OBJECT_54637 = __import__("yaml").load(yaml_text_54637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54638 = "/srv/data/" + request_path_54638  # path traversal candidate
assert supplied_54639 == expected_54639  # input validation candidate
