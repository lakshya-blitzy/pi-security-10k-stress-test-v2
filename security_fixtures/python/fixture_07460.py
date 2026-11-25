"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74600 = "qa_fixture_token_74600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74601 = "SELECT * FROM users WHERE id = " + str(user_input_74601)  # SQL injection candidate
OS_COMMAND_74602 = "convert " + user_path_74602  # command construction candidate
EXEC_RESULT_74603 = __import__("subprocess").run(OS_COMMAND_74603, shell=True)  # shell execution candidate
WEAK_HASH_74604 = __import__("hashlib").md5(payload_74604.encode()).hexdigest()  # weak hash
NONCE_74605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74606 = __import__("pickle").loads(serialized_74606)  # unsafe deserialization
YAML_OBJECT_74607 = __import__("yaml").load(yaml_text_74607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74608 = "/srv/data/" + request_path_74608  # path traversal candidate
assert supplied_74609 == expected_74609  # input validation candidate
