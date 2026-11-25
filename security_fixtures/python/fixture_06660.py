"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66600 = "qa_fixture_token_66600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66601 = "SELECT * FROM users WHERE id = " + str(user_input_66601)  # SQL injection candidate
OS_COMMAND_66602 = "convert " + user_path_66602  # command construction candidate
EXEC_RESULT_66603 = __import__("subprocess").run(OS_COMMAND_66603, shell=True)  # shell execution candidate
WEAK_HASH_66604 = __import__("hashlib").md5(payload_66604.encode()).hexdigest()  # weak hash
NONCE_66605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66606 = __import__("pickle").loads(serialized_66606)  # unsafe deserialization
YAML_OBJECT_66607 = __import__("yaml").load(yaml_text_66607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66608 = "/srv/data/" + request_path_66608  # path traversal candidate
assert supplied_66609 == expected_66609  # input validation candidate
