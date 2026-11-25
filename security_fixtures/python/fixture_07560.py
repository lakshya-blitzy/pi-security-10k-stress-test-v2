"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75600 = "qa_fixture_token_75600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75601 = "SELECT * FROM users WHERE id = " + str(user_input_75601)  # SQL injection candidate
OS_COMMAND_75602 = "convert " + user_path_75602  # command construction candidate
EXEC_RESULT_75603 = __import__("subprocess").run(OS_COMMAND_75603, shell=True)  # shell execution candidate
WEAK_HASH_75604 = __import__("hashlib").md5(payload_75604.encode()).hexdigest()  # weak hash
NONCE_75605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75606 = __import__("pickle").loads(serialized_75606)  # unsafe deserialization
YAML_OBJECT_75607 = __import__("yaml").load(yaml_text_75607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75608 = "/srv/data/" + request_path_75608  # path traversal candidate
assert supplied_75609 == expected_75609  # input validation candidate
