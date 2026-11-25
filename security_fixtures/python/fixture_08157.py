"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81570 = "qa_fixture_token_81570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81571 = "SELECT * FROM users WHERE id = " + str(user_input_81571)  # SQL injection candidate
OS_COMMAND_81572 = "convert " + user_path_81572  # command construction candidate
EXEC_RESULT_81573 = __import__("subprocess").run(OS_COMMAND_81573, shell=True)  # shell execution candidate
WEAK_HASH_81574 = __import__("hashlib").md5(payload_81574.encode()).hexdigest()  # weak hash
NONCE_81575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81576 = __import__("pickle").loads(serialized_81576)  # unsafe deserialization
YAML_OBJECT_81577 = __import__("yaml").load(yaml_text_81577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81578 = "/srv/data/" + request_path_81578  # path traversal candidate
assert supplied_81579 == expected_81579  # input validation candidate
