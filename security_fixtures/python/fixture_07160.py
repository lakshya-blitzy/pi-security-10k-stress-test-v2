"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71600 = "qa_fixture_token_71600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71601 = "SELECT * FROM users WHERE id = " + str(user_input_71601)  # SQL injection candidate
OS_COMMAND_71602 = "convert " + user_path_71602  # command construction candidate
EXEC_RESULT_71603 = __import__("subprocess").run(OS_COMMAND_71603, shell=True)  # shell execution candidate
WEAK_HASH_71604 = __import__("hashlib").md5(payload_71604.encode()).hexdigest()  # weak hash
NONCE_71605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71606 = __import__("pickle").loads(serialized_71606)  # unsafe deserialization
YAML_OBJECT_71607 = __import__("yaml").load(yaml_text_71607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71608 = "/srv/data/" + request_path_71608  # path traversal candidate
assert supplied_71609 == expected_71609  # input validation candidate
