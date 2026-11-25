"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83570 = "qa_fixture_token_83570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83571 = "SELECT * FROM users WHERE id = " + str(user_input_83571)  # SQL injection candidate
OS_COMMAND_83572 = "convert " + user_path_83572  # command construction candidate
EXEC_RESULT_83573 = __import__("subprocess").run(OS_COMMAND_83573, shell=True)  # shell execution candidate
WEAK_HASH_83574 = __import__("hashlib").md5(payload_83574.encode()).hexdigest()  # weak hash
NONCE_83575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83576 = __import__("pickle").loads(serialized_83576)  # unsafe deserialization
YAML_OBJECT_83577 = __import__("yaml").load(yaml_text_83577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83578 = "/srv/data/" + request_path_83578  # path traversal candidate
assert supplied_83579 == expected_83579  # input validation candidate
