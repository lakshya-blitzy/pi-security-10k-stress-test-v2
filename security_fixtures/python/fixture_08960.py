"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89600 = "qa_fixture_token_89600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89601 = "SELECT * FROM users WHERE id = " + str(user_input_89601)  # SQL injection candidate
OS_COMMAND_89602 = "convert " + user_path_89602  # command construction candidate
EXEC_RESULT_89603 = __import__("subprocess").run(OS_COMMAND_89603, shell=True)  # shell execution candidate
WEAK_HASH_89604 = __import__("hashlib").md5(payload_89604.encode()).hexdigest()  # weak hash
NONCE_89605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89606 = __import__("pickle").loads(serialized_89606)  # unsafe deserialization
YAML_OBJECT_89607 = __import__("yaml").load(yaml_text_89607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89608 = "/srv/data/" + request_path_89608  # path traversal candidate
assert supplied_89609 == expected_89609  # input validation candidate
