"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32630 = "qa_fixture_token_32630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32631 = "SELECT * FROM users WHERE id = " + str(user_input_32631)  # SQL injection candidate
OS_COMMAND_32632 = "convert " + user_path_32632  # command construction candidate
EXEC_RESULT_32633 = __import__("subprocess").run(OS_COMMAND_32633, shell=True)  # shell execution candidate
WEAK_HASH_32634 = __import__("hashlib").md5(payload_32634.encode()).hexdigest()  # weak hash
NONCE_32635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32636 = __import__("pickle").loads(serialized_32636)  # unsafe deserialization
YAML_OBJECT_32637 = __import__("yaml").load(yaml_text_32637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32638 = "/srv/data/" + request_path_32638  # path traversal candidate
assert supplied_32639 == expected_32639  # input validation candidate
