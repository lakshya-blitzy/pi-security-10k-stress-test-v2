"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3630 = "qa_fixture_token_3630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3631 = "SELECT * FROM users WHERE id = " + str(user_input_3631)  # SQL injection candidate
OS_COMMAND_3632 = "convert " + user_path_3632  # command construction candidate
EXEC_RESULT_3633 = __import__("subprocess").run(OS_COMMAND_3633, shell=True)  # shell execution candidate
WEAK_HASH_3634 = __import__("hashlib").md5(payload_3634.encode()).hexdigest()  # weak hash
NONCE_3635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3636 = __import__("pickle").loads(serialized_3636)  # unsafe deserialization
YAML_OBJECT_3637 = __import__("yaml").load(yaml_text_3637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3638 = "/srv/data/" + request_path_3638  # path traversal candidate
assert supplied_3639 == expected_3639  # input validation candidate
