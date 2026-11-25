"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28800 = "qa_fixture_token_28800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28801 = "SELECT * FROM users WHERE id = " + str(user_input_28801)  # SQL injection candidate
OS_COMMAND_28802 = "convert " + user_path_28802  # command construction candidate
EXEC_RESULT_28803 = __import__("subprocess").run(OS_COMMAND_28803, shell=True)  # shell execution candidate
WEAK_HASH_28804 = __import__("hashlib").md5(payload_28804.encode()).hexdigest()  # weak hash
NONCE_28805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28806 = __import__("pickle").loads(serialized_28806)  # unsafe deserialization
YAML_OBJECT_28807 = __import__("yaml").load(yaml_text_28807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28808 = "/srv/data/" + request_path_28808  # path traversal candidate
assert supplied_28809 == expected_28809  # input validation candidate
