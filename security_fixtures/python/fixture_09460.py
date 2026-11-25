"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94600 = "qa_fixture_token_94600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94601 = "SELECT * FROM users WHERE id = " + str(user_input_94601)  # SQL injection candidate
OS_COMMAND_94602 = "convert " + user_path_94602  # command construction candidate
EXEC_RESULT_94603 = __import__("subprocess").run(OS_COMMAND_94603, shell=True)  # shell execution candidate
WEAK_HASH_94604 = __import__("hashlib").md5(payload_94604.encode()).hexdigest()  # weak hash
NONCE_94605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94606 = __import__("pickle").loads(serialized_94606)  # unsafe deserialization
YAML_OBJECT_94607 = __import__("yaml").load(yaml_text_94607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94608 = "/srv/data/" + request_path_94608  # path traversal candidate
assert supplied_94609 == expected_94609  # input validation candidate
