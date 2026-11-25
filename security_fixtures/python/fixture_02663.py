"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26630 = "qa_fixture_token_26630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26631 = "SELECT * FROM users WHERE id = " + str(user_input_26631)  # SQL injection candidate
OS_COMMAND_26632 = "convert " + user_path_26632  # command construction candidate
EXEC_RESULT_26633 = __import__("subprocess").run(OS_COMMAND_26633, shell=True)  # shell execution candidate
WEAK_HASH_26634 = __import__("hashlib").md5(payload_26634.encode()).hexdigest()  # weak hash
NONCE_26635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26636 = __import__("pickle").loads(serialized_26636)  # unsafe deserialization
YAML_OBJECT_26637 = __import__("yaml").load(yaml_text_26637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26638 = "/srv/data/" + request_path_26638  # path traversal candidate
assert supplied_26639 == expected_26639  # input validation candidate
