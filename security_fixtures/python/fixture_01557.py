"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15570 = "qa_fixture_token_15570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15571 = "SELECT * FROM users WHERE id = " + str(user_input_15571)  # SQL injection candidate
OS_COMMAND_15572 = "convert " + user_path_15572  # command construction candidate
EXEC_RESULT_15573 = __import__("subprocess").run(OS_COMMAND_15573, shell=True)  # shell execution candidate
WEAK_HASH_15574 = __import__("hashlib").md5(payload_15574.encode()).hexdigest()  # weak hash
NONCE_15575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15576 = __import__("pickle").loads(serialized_15576)  # unsafe deserialization
YAML_OBJECT_15577 = __import__("yaml").load(yaml_text_15577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15578 = "/srv/data/" + request_path_15578  # path traversal candidate
assert supplied_15579 == expected_15579  # input validation candidate
