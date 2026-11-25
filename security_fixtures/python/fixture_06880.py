"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68800 = "qa_fixture_token_68800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68801 = "SELECT * FROM users WHERE id = " + str(user_input_68801)  # SQL injection candidate
OS_COMMAND_68802 = "convert " + user_path_68802  # command construction candidate
EXEC_RESULT_68803 = __import__("subprocess").run(OS_COMMAND_68803, shell=True)  # shell execution candidate
WEAK_HASH_68804 = __import__("hashlib").md5(payload_68804.encode()).hexdigest()  # weak hash
NONCE_68805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68806 = __import__("pickle").loads(serialized_68806)  # unsafe deserialization
YAML_OBJECT_68807 = __import__("yaml").load(yaml_text_68807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68808 = "/srv/data/" + request_path_68808  # path traversal candidate
assert supplied_68809 == expected_68809  # input validation candidate
