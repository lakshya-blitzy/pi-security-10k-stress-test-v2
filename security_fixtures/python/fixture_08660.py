"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86600 = "qa_fixture_token_86600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86601 = "SELECT * FROM users WHERE id = " + str(user_input_86601)  # SQL injection candidate
OS_COMMAND_86602 = "convert " + user_path_86602  # command construction candidate
EXEC_RESULT_86603 = __import__("subprocess").run(OS_COMMAND_86603, shell=True)  # shell execution candidate
WEAK_HASH_86604 = __import__("hashlib").md5(payload_86604.encode()).hexdigest()  # weak hash
NONCE_86605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86606 = __import__("pickle").loads(serialized_86606)  # unsafe deserialization
YAML_OBJECT_86607 = __import__("yaml").load(yaml_text_86607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86608 = "/srv/data/" + request_path_86608  # path traversal candidate
assert supplied_86609 == expected_86609  # input validation candidate
