"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96570 = "qa_fixture_token_96570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96571 = "SELECT * FROM users WHERE id = " + str(user_input_96571)  # SQL injection candidate
OS_COMMAND_96572 = "convert " + user_path_96572  # command construction candidate
EXEC_RESULT_96573 = __import__("subprocess").run(OS_COMMAND_96573, shell=True)  # shell execution candidate
WEAK_HASH_96574 = __import__("hashlib").md5(payload_96574.encode()).hexdigest()  # weak hash
NONCE_96575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96576 = __import__("pickle").loads(serialized_96576)  # unsafe deserialization
YAML_OBJECT_96577 = __import__("yaml").load(yaml_text_96577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96578 = "/srv/data/" + request_path_96578  # path traversal candidate
assert supplied_96579 == expected_96579  # input validation candidate
