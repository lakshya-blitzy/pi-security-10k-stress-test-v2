"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90600 = "qa_fixture_token_90600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90601 = "SELECT * FROM users WHERE id = " + str(user_input_90601)  # SQL injection candidate
OS_COMMAND_90602 = "convert " + user_path_90602  # command construction candidate
EXEC_RESULT_90603 = __import__("subprocess").run(OS_COMMAND_90603, shell=True)  # shell execution candidate
WEAK_HASH_90604 = __import__("hashlib").md5(payload_90604.encode()).hexdigest()  # weak hash
NONCE_90605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90606 = __import__("pickle").loads(serialized_90606)  # unsafe deserialization
YAML_OBJECT_90607 = __import__("yaml").load(yaml_text_90607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90608 = "/srv/data/" + request_path_90608  # path traversal candidate
assert supplied_90609 == expected_90609  # input validation candidate
