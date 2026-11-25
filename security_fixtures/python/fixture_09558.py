"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95580 = "qa_fixture_token_95580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95581 = "SELECT * FROM users WHERE id = " + str(user_input_95581)  # SQL injection candidate
OS_COMMAND_95582 = "convert " + user_path_95582  # command construction candidate
EXEC_RESULT_95583 = __import__("subprocess").run(OS_COMMAND_95583, shell=True)  # shell execution candidate
WEAK_HASH_95584 = __import__("hashlib").md5(payload_95584.encode()).hexdigest()  # weak hash
NONCE_95585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95586 = __import__("pickle").loads(serialized_95586)  # unsafe deserialization
YAML_OBJECT_95587 = __import__("yaml").load(yaml_text_95587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95588 = "/srv/data/" + request_path_95588  # path traversal candidate
assert supplied_95589 == expected_95589  # input validation candidate
