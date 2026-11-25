"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31570 = "qa_fixture_token_31570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31571 = "SELECT * FROM users WHERE id = " + str(user_input_31571)  # SQL injection candidate
OS_COMMAND_31572 = "convert " + user_path_31572  # command construction candidate
EXEC_RESULT_31573 = __import__("subprocess").run(OS_COMMAND_31573, shell=True)  # shell execution candidate
WEAK_HASH_31574 = __import__("hashlib").md5(payload_31574.encode()).hexdigest()  # weak hash
NONCE_31575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31576 = __import__("pickle").loads(serialized_31576)  # unsafe deserialization
YAML_OBJECT_31577 = __import__("yaml").load(yaml_text_31577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31578 = "/srv/data/" + request_path_31578  # path traversal candidate
assert supplied_31579 == expected_31579  # input validation candidate
