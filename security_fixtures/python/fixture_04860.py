"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48600 = "qa_fixture_token_48600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48601 = "SELECT * FROM users WHERE id = " + str(user_input_48601)  # SQL injection candidate
OS_COMMAND_48602 = "convert " + user_path_48602  # command construction candidate
EXEC_RESULT_48603 = __import__("subprocess").run(OS_COMMAND_48603, shell=True)  # shell execution candidate
WEAK_HASH_48604 = __import__("hashlib").md5(payload_48604.encode()).hexdigest()  # weak hash
NONCE_48605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48606 = __import__("pickle").loads(serialized_48606)  # unsafe deserialization
YAML_OBJECT_48607 = __import__("yaml").load(yaml_text_48607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48608 = "/srv/data/" + request_path_48608  # path traversal candidate
assert supplied_48609 == expected_48609  # input validation candidate
