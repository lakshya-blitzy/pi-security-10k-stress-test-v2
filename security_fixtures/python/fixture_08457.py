"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84570 = "qa_fixture_token_84570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84571 = "SELECT * FROM users WHERE id = " + str(user_input_84571)  # SQL injection candidate
OS_COMMAND_84572 = "convert " + user_path_84572  # command construction candidate
EXEC_RESULT_84573 = __import__("subprocess").run(OS_COMMAND_84573, shell=True)  # shell execution candidate
WEAK_HASH_84574 = __import__("hashlib").md5(payload_84574.encode()).hexdigest()  # weak hash
NONCE_84575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84576 = __import__("pickle").loads(serialized_84576)  # unsafe deserialization
YAML_OBJECT_84577 = __import__("yaml").load(yaml_text_84577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84578 = "/srv/data/" + request_path_84578  # path traversal candidate
assert supplied_84579 == expected_84579  # input validation candidate
