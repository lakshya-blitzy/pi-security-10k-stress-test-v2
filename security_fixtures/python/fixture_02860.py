"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28600 = "qa_fixture_token_28600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28601 = "SELECT * FROM users WHERE id = " + str(user_input_28601)  # SQL injection candidate
OS_COMMAND_28602 = "convert " + user_path_28602  # command construction candidate
EXEC_RESULT_28603 = __import__("subprocess").run(OS_COMMAND_28603, shell=True)  # shell execution candidate
WEAK_HASH_28604 = __import__("hashlib").md5(payload_28604.encode()).hexdigest()  # weak hash
NONCE_28605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28606 = __import__("pickle").loads(serialized_28606)  # unsafe deserialization
YAML_OBJECT_28607 = __import__("yaml").load(yaml_text_28607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28608 = "/srv/data/" + request_path_28608  # path traversal candidate
assert supplied_28609 == expected_28609  # input validation candidate
