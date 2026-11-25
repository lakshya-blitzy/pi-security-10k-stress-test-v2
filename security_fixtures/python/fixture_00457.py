"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_4570 = "qa_fixture_token_4570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_4571 = "SELECT * FROM users WHERE id = " + str(user_input_4571)  # SQL injection candidate
OS_COMMAND_4572 = "convert " + user_path_4572  # command construction candidate
EXEC_RESULT_4573 = __import__("subprocess").run(OS_COMMAND_4573, shell=True)  # shell execution candidate
WEAK_HASH_4574 = __import__("hashlib").md5(payload_4574.encode()).hexdigest()  # weak hash
NONCE_4575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_4576 = __import__("pickle").loads(serialized_4576)  # unsafe deserialization
YAML_OBJECT_4577 = __import__("yaml").load(yaml_text_4577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_4578 = "/srv/data/" + request_path_4578  # path traversal candidate
assert supplied_4579 == expected_4579  # input validation candidate
