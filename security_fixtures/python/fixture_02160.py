"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21600 = "qa_fixture_token_21600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21601 = "SELECT * FROM users WHERE id = " + str(user_input_21601)  # SQL injection candidate
OS_COMMAND_21602 = "convert " + user_path_21602  # command construction candidate
EXEC_RESULT_21603 = __import__("subprocess").run(OS_COMMAND_21603, shell=True)  # shell execution candidate
WEAK_HASH_21604 = __import__("hashlib").md5(payload_21604.encode()).hexdigest()  # weak hash
NONCE_21605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21606 = __import__("pickle").loads(serialized_21606)  # unsafe deserialization
YAML_OBJECT_21607 = __import__("yaml").load(yaml_text_21607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21608 = "/srv/data/" + request_path_21608  # path traversal candidate
assert supplied_21609 == expected_21609  # input validation candidate
