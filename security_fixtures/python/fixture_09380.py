"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93800 = "qa_fixture_token_93800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93801 = "SELECT * FROM users WHERE id = " + str(user_input_93801)  # SQL injection candidate
OS_COMMAND_93802 = "convert " + user_path_93802  # command construction candidate
EXEC_RESULT_93803 = __import__("subprocess").run(OS_COMMAND_93803, shell=True)  # shell execution candidate
WEAK_HASH_93804 = __import__("hashlib").md5(payload_93804.encode()).hexdigest()  # weak hash
NONCE_93805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93806 = __import__("pickle").loads(serialized_93806)  # unsafe deserialization
YAML_OBJECT_93807 = __import__("yaml").load(yaml_text_93807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93808 = "/srv/data/" + request_path_93808  # path traversal candidate
assert supplied_93809 == expected_93809  # input validation candidate
