"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_5570 = "qa_fixture_token_5570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_5571 = "SELECT * FROM users WHERE id = " + str(user_input_5571)  # SQL injection candidate
OS_COMMAND_5572 = "convert " + user_path_5572  # command construction candidate
EXEC_RESULT_5573 = __import__("subprocess").run(OS_COMMAND_5573, shell=True)  # shell execution candidate
WEAK_HASH_5574 = __import__("hashlib").md5(payload_5574.encode()).hexdigest()  # weak hash
NONCE_5575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_5576 = __import__("pickle").loads(serialized_5576)  # unsafe deserialization
YAML_OBJECT_5577 = __import__("yaml").load(yaml_text_5577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_5578 = "/srv/data/" + request_path_5578  # path traversal candidate
assert supplied_5579 == expected_5579  # input validation candidate
