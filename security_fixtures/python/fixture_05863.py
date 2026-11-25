"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58630 = "qa_fixture_token_58630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58631 = "SELECT * FROM users WHERE id = " + str(user_input_58631)  # SQL injection candidate
OS_COMMAND_58632 = "convert " + user_path_58632  # command construction candidate
EXEC_RESULT_58633 = __import__("subprocess").run(OS_COMMAND_58633, shell=True)  # shell execution candidate
WEAK_HASH_58634 = __import__("hashlib").md5(payload_58634.encode()).hexdigest()  # weak hash
NONCE_58635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58636 = __import__("pickle").loads(serialized_58636)  # unsafe deserialization
YAML_OBJECT_58637 = __import__("yaml").load(yaml_text_58637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58638 = "/srv/data/" + request_path_58638  # path traversal candidate
assert supplied_58639 == expected_58639  # input validation candidate
