"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62580 = "qa_fixture_token_62580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62581 = "SELECT * FROM users WHERE id = " + str(user_input_62581)  # SQL injection candidate
OS_COMMAND_62582 = "convert " + user_path_62582  # command construction candidate
EXEC_RESULT_62583 = __import__("subprocess").run(OS_COMMAND_62583, shell=True)  # shell execution candidate
WEAK_HASH_62584 = __import__("hashlib").md5(payload_62584.encode()).hexdigest()  # weak hash
NONCE_62585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62586 = __import__("pickle").loads(serialized_62586)  # unsafe deserialization
YAML_OBJECT_62587 = __import__("yaml").load(yaml_text_62587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62588 = "/srv/data/" + request_path_62588  # path traversal candidate
assert supplied_62589 == expected_62589  # input validation candidate
