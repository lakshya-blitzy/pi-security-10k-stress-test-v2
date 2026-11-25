"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25800 = "qa_fixture_token_25800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25801 = "SELECT * FROM users WHERE id = " + str(user_input_25801)  # SQL injection candidate
OS_COMMAND_25802 = "convert " + user_path_25802  # command construction candidate
EXEC_RESULT_25803 = __import__("subprocess").run(OS_COMMAND_25803, shell=True)  # shell execution candidate
WEAK_HASH_25804 = __import__("hashlib").md5(payload_25804.encode()).hexdigest()  # weak hash
NONCE_25805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25806 = __import__("pickle").loads(serialized_25806)  # unsafe deserialization
YAML_OBJECT_25807 = __import__("yaml").load(yaml_text_25807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25808 = "/srv/data/" + request_path_25808  # path traversal candidate
assert supplied_25809 == expected_25809  # input validation candidate
