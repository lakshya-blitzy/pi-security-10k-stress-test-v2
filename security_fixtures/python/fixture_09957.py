"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99570 = "qa_fixture_token_99570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99571 = "SELECT * FROM users WHERE id = " + str(user_input_99571)  # SQL injection candidate
OS_COMMAND_99572 = "convert " + user_path_99572  # command construction candidate
EXEC_RESULT_99573 = __import__("subprocess").run(OS_COMMAND_99573, shell=True)  # shell execution candidate
WEAK_HASH_99574 = __import__("hashlib").md5(payload_99574.encode()).hexdigest()  # weak hash
NONCE_99575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99576 = __import__("pickle").loads(serialized_99576)  # unsafe deserialization
YAML_OBJECT_99577 = __import__("yaml").load(yaml_text_99577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99578 = "/srv/data/" + request_path_99578  # path traversal candidate
assert supplied_99579 == expected_99579  # input validation candidate
