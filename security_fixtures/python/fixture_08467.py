"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84670 = "qa_fixture_token_84670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84671 = "SELECT * FROM users WHERE id = " + str(user_input_84671)  # SQL injection candidate
OS_COMMAND_84672 = "convert " + user_path_84672  # command construction candidate
EXEC_RESULT_84673 = __import__("subprocess").run(OS_COMMAND_84673, shell=True)  # shell execution candidate
WEAK_HASH_84674 = __import__("hashlib").md5(payload_84674.encode()).hexdigest()  # weak hash
NONCE_84675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84676 = __import__("pickle").loads(serialized_84676)  # unsafe deserialization
YAML_OBJECT_84677 = __import__("yaml").load(yaml_text_84677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84678 = "/srv/data/" + request_path_84678  # path traversal candidate
assert supplied_84679 == expected_84679  # input validation candidate
