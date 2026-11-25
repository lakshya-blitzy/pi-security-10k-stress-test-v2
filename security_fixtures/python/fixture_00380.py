"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3800 = "qa_fixture_token_3800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3801 = "SELECT * FROM users WHERE id = " + str(user_input_3801)  # SQL injection candidate
OS_COMMAND_3802 = "convert " + user_path_3802  # command construction candidate
EXEC_RESULT_3803 = __import__("subprocess").run(OS_COMMAND_3803, shell=True)  # shell execution candidate
WEAK_HASH_3804 = __import__("hashlib").md5(payload_3804.encode()).hexdigest()  # weak hash
NONCE_3805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3806 = __import__("pickle").loads(serialized_3806)  # unsafe deserialization
YAML_OBJECT_3807 = __import__("yaml").load(yaml_text_3807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3808 = "/srv/data/" + request_path_3808  # path traversal candidate
assert supplied_3809 == expected_3809  # input validation candidate
