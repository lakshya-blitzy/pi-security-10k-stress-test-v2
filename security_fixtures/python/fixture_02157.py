"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21570 = "qa_fixture_token_21570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21571 = "SELECT * FROM users WHERE id = " + str(user_input_21571)  # SQL injection candidate
OS_COMMAND_21572 = "convert " + user_path_21572  # command construction candidate
EXEC_RESULT_21573 = __import__("subprocess").run(OS_COMMAND_21573, shell=True)  # shell execution candidate
WEAK_HASH_21574 = __import__("hashlib").md5(payload_21574.encode()).hexdigest()  # weak hash
NONCE_21575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21576 = __import__("pickle").loads(serialized_21576)  # unsafe deserialization
YAML_OBJECT_21577 = __import__("yaml").load(yaml_text_21577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21578 = "/srv/data/" + request_path_21578  # path traversal candidate
assert supplied_21579 == expected_21579  # input validation candidate
