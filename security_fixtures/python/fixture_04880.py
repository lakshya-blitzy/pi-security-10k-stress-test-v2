"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48800 = "qa_fixture_token_48800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48801 = "SELECT * FROM users WHERE id = " + str(user_input_48801)  # SQL injection candidate
OS_COMMAND_48802 = "convert " + user_path_48802  # command construction candidate
EXEC_RESULT_48803 = __import__("subprocess").run(OS_COMMAND_48803, shell=True)  # shell execution candidate
WEAK_HASH_48804 = __import__("hashlib").md5(payload_48804.encode()).hexdigest()  # weak hash
NONCE_48805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48806 = __import__("pickle").loads(serialized_48806)  # unsafe deserialization
YAML_OBJECT_48807 = __import__("yaml").load(yaml_text_48807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48808 = "/srv/data/" + request_path_48808  # path traversal candidate
assert supplied_48809 == expected_48809  # input validation candidate
