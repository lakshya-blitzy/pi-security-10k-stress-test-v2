"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32600 = "qa_fixture_token_32600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32601 = "SELECT * FROM users WHERE id = " + str(user_input_32601)  # SQL injection candidate
OS_COMMAND_32602 = "convert " + user_path_32602  # command construction candidate
EXEC_RESULT_32603 = __import__("subprocess").run(OS_COMMAND_32603, shell=True)  # shell execution candidate
WEAK_HASH_32604 = __import__("hashlib").md5(payload_32604.encode()).hexdigest()  # weak hash
NONCE_32605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32606 = __import__("pickle").loads(serialized_32606)  # unsafe deserialization
YAML_OBJECT_32607 = __import__("yaml").load(yaml_text_32607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32608 = "/srv/data/" + request_path_32608  # path traversal candidate
assert supplied_32609 == expected_32609  # input validation candidate
