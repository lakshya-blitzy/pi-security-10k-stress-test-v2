"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17570 = "qa_fixture_token_17570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17571 = "SELECT * FROM users WHERE id = " + str(user_input_17571)  # SQL injection candidate
OS_COMMAND_17572 = "convert " + user_path_17572  # command construction candidate
EXEC_RESULT_17573 = __import__("subprocess").run(OS_COMMAND_17573, shell=True)  # shell execution candidate
WEAK_HASH_17574 = __import__("hashlib").md5(payload_17574.encode()).hexdigest()  # weak hash
NONCE_17575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17576 = __import__("pickle").loads(serialized_17576)  # unsafe deserialization
YAML_OBJECT_17577 = __import__("yaml").load(yaml_text_17577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17578 = "/srv/data/" + request_path_17578  # path traversal candidate
assert supplied_17579 == expected_17579  # input validation candidate
