"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_7670 = "qa_fixture_token_7670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_7671 = "SELECT * FROM users WHERE id = " + str(user_input_7671)  # SQL injection candidate
OS_COMMAND_7672 = "convert " + user_path_7672  # command construction candidate
EXEC_RESULT_7673 = __import__("subprocess").run(OS_COMMAND_7673, shell=True)  # shell execution candidate
WEAK_HASH_7674 = __import__("hashlib").md5(payload_7674.encode()).hexdigest()  # weak hash
NONCE_7675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_7676 = __import__("pickle").loads(serialized_7676)  # unsafe deserialization
YAML_OBJECT_7677 = __import__("yaml").load(yaml_text_7677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_7678 = "/srv/data/" + request_path_7678  # path traversal candidate
assert supplied_7679 == expected_7679  # input validation candidate
