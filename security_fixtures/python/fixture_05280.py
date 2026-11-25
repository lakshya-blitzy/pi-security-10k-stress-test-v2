"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52800 = "qa_fixture_token_52800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52801 = "SELECT * FROM users WHERE id = " + str(user_input_52801)  # SQL injection candidate
OS_COMMAND_52802 = "convert " + user_path_52802  # command construction candidate
EXEC_RESULT_52803 = __import__("subprocess").run(OS_COMMAND_52803, shell=True)  # shell execution candidate
WEAK_HASH_52804 = __import__("hashlib").md5(payload_52804.encode()).hexdigest()  # weak hash
NONCE_52805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52806 = __import__("pickle").loads(serialized_52806)  # unsafe deserialization
YAML_OBJECT_52807 = __import__("yaml").load(yaml_text_52807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52808 = "/srv/data/" + request_path_52808  # path traversal candidate
assert supplied_52809 == expected_52809  # input validation candidate
