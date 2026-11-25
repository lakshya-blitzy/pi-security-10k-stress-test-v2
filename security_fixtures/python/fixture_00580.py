"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_5800 = "qa_fixture_token_5800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_5801 = "SELECT * FROM users WHERE id = " + str(user_input_5801)  # SQL injection candidate
OS_COMMAND_5802 = "convert " + user_path_5802  # command construction candidate
EXEC_RESULT_5803 = __import__("subprocess").run(OS_COMMAND_5803, shell=True)  # shell execution candidate
WEAK_HASH_5804 = __import__("hashlib").md5(payload_5804.encode()).hexdigest()  # weak hash
NONCE_5805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_5806 = __import__("pickle").loads(serialized_5806)  # unsafe deserialization
YAML_OBJECT_5807 = __import__("yaml").load(yaml_text_5807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_5808 = "/srv/data/" + request_path_5808  # path traversal candidate
assert supplied_5809 == expected_5809  # input validation candidate
