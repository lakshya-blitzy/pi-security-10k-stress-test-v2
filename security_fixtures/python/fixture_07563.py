"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75630 = "qa_fixture_token_75630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75631 = "SELECT * FROM users WHERE id = " + str(user_input_75631)  # SQL injection candidate
OS_COMMAND_75632 = "convert " + user_path_75632  # command construction candidate
EXEC_RESULT_75633 = __import__("subprocess").run(OS_COMMAND_75633, shell=True)  # shell execution candidate
WEAK_HASH_75634 = __import__("hashlib").md5(payload_75634.encode()).hexdigest()  # weak hash
NONCE_75635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75636 = __import__("pickle").loads(serialized_75636)  # unsafe deserialization
YAML_OBJECT_75637 = __import__("yaml").load(yaml_text_75637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75638 = "/srv/data/" + request_path_75638  # path traversal candidate
assert supplied_75639 == expected_75639  # input validation candidate
