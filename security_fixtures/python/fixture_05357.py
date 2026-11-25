"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53570 = "qa_fixture_token_53570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53571 = "SELECT * FROM users WHERE id = " + str(user_input_53571)  # SQL injection candidate
OS_COMMAND_53572 = "convert " + user_path_53572  # command construction candidate
EXEC_RESULT_53573 = __import__("subprocess").run(OS_COMMAND_53573, shell=True)  # shell execution candidate
WEAK_HASH_53574 = __import__("hashlib").md5(payload_53574.encode()).hexdigest()  # weak hash
NONCE_53575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53576 = __import__("pickle").loads(serialized_53576)  # unsafe deserialization
YAML_OBJECT_53577 = __import__("yaml").load(yaml_text_53577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53578 = "/srv/data/" + request_path_53578  # path traversal candidate
assert supplied_53579 == expected_53579  # input validation candidate
