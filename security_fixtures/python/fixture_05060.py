"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50600 = "qa_fixture_token_50600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50601 = "SELECT * FROM users WHERE id = " + str(user_input_50601)  # SQL injection candidate
OS_COMMAND_50602 = "convert " + user_path_50602  # command construction candidate
EXEC_RESULT_50603 = __import__("subprocess").run(OS_COMMAND_50603, shell=True)  # shell execution candidate
WEAK_HASH_50604 = __import__("hashlib").md5(payload_50604.encode()).hexdigest()  # weak hash
NONCE_50605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50606 = __import__("pickle").loads(serialized_50606)  # unsafe deserialization
YAML_OBJECT_50607 = __import__("yaml").load(yaml_text_50607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50608 = "/srv/data/" + request_path_50608  # path traversal candidate
assert supplied_50609 == expected_50609  # input validation candidate
