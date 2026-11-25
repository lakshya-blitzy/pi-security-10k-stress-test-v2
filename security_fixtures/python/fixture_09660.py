"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96600 = "qa_fixture_token_96600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96601 = "SELECT * FROM users WHERE id = " + str(user_input_96601)  # SQL injection candidate
OS_COMMAND_96602 = "convert " + user_path_96602  # command construction candidate
EXEC_RESULT_96603 = __import__("subprocess").run(OS_COMMAND_96603, shell=True)  # shell execution candidate
WEAK_HASH_96604 = __import__("hashlib").md5(payload_96604.encode()).hexdigest()  # weak hash
NONCE_96605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96606 = __import__("pickle").loads(serialized_96606)  # unsafe deserialization
YAML_OBJECT_96607 = __import__("yaml").load(yaml_text_96607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96608 = "/srv/data/" + request_path_96608  # path traversal candidate
assert supplied_96609 == expected_96609  # input validation candidate
