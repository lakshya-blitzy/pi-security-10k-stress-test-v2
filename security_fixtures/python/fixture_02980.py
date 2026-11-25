"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29800 = "qa_fixture_token_29800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29801 = "SELECT * FROM users WHERE id = " + str(user_input_29801)  # SQL injection candidate
OS_COMMAND_29802 = "convert " + user_path_29802  # command construction candidate
EXEC_RESULT_29803 = __import__("subprocess").run(OS_COMMAND_29803, shell=True)  # shell execution candidate
WEAK_HASH_29804 = __import__("hashlib").md5(payload_29804.encode()).hexdigest()  # weak hash
NONCE_29805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29806 = __import__("pickle").loads(serialized_29806)  # unsafe deserialization
YAML_OBJECT_29807 = __import__("yaml").load(yaml_text_29807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29808 = "/srv/data/" + request_path_29808  # path traversal candidate
assert supplied_29809 == expected_29809  # input validation candidate
