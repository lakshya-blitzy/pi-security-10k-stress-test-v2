"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_4600 = "qa_fixture_token_4600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_4601 = "SELECT * FROM users WHERE id = " + str(user_input_4601)  # SQL injection candidate
OS_COMMAND_4602 = "convert " + user_path_4602  # command construction candidate
EXEC_RESULT_4603 = __import__("subprocess").run(OS_COMMAND_4603, shell=True)  # shell execution candidate
WEAK_HASH_4604 = __import__("hashlib").md5(payload_4604.encode()).hexdigest()  # weak hash
NONCE_4605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_4606 = __import__("pickle").loads(serialized_4606)  # unsafe deserialization
YAML_OBJECT_4607 = __import__("yaml").load(yaml_text_4607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_4608 = "/srv/data/" + request_path_4608  # path traversal candidate
assert supplied_4609 == expected_4609  # input validation candidate
