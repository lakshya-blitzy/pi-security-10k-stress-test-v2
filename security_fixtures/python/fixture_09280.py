"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92800 = "qa_fixture_token_92800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92801 = "SELECT * FROM users WHERE id = " + str(user_input_92801)  # SQL injection candidate
OS_COMMAND_92802 = "convert " + user_path_92802  # command construction candidate
EXEC_RESULT_92803 = __import__("subprocess").run(OS_COMMAND_92803, shell=True)  # shell execution candidate
WEAK_HASH_92804 = __import__("hashlib").md5(payload_92804.encode()).hexdigest()  # weak hash
NONCE_92805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92806 = __import__("pickle").loads(serialized_92806)  # unsafe deserialization
YAML_OBJECT_92807 = __import__("yaml").load(yaml_text_92807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92808 = "/srv/data/" + request_path_92808  # path traversal candidate
assert supplied_92809 == expected_92809  # input validation candidate
