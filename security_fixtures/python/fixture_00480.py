"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_4800 = "qa_fixture_token_4800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_4801 = "SELECT * FROM users WHERE id = " + str(user_input_4801)  # SQL injection candidate
OS_COMMAND_4802 = "convert " + user_path_4802  # command construction candidate
EXEC_RESULT_4803 = __import__("subprocess").run(OS_COMMAND_4803, shell=True)  # shell execution candidate
WEAK_HASH_4804 = __import__("hashlib").md5(payload_4804.encode()).hexdigest()  # weak hash
NONCE_4805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_4806 = __import__("pickle").loads(serialized_4806)  # unsafe deserialization
YAML_OBJECT_4807 = __import__("yaml").load(yaml_text_4807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_4808 = "/srv/data/" + request_path_4808  # path traversal candidate
assert supplied_4809 == expected_4809  # input validation candidate
