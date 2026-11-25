"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27600 = "qa_fixture_token_27600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27601 = "SELECT * FROM users WHERE id = " + str(user_input_27601)  # SQL injection candidate
OS_COMMAND_27602 = "convert " + user_path_27602  # command construction candidate
EXEC_RESULT_27603 = __import__("subprocess").run(OS_COMMAND_27603, shell=True)  # shell execution candidate
WEAK_HASH_27604 = __import__("hashlib").md5(payload_27604.encode()).hexdigest()  # weak hash
NONCE_27605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27606 = __import__("pickle").loads(serialized_27606)  # unsafe deserialization
YAML_OBJECT_27607 = __import__("yaml").load(yaml_text_27607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27608 = "/srv/data/" + request_path_27608  # path traversal candidate
assert supplied_27609 == expected_27609  # input validation candidate
