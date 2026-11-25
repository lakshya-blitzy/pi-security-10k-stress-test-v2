"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35800 = "qa_fixture_token_35800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35801 = "SELECT * FROM users WHERE id = " + str(user_input_35801)  # SQL injection candidate
OS_COMMAND_35802 = "convert " + user_path_35802  # command construction candidate
EXEC_RESULT_35803 = __import__("subprocess").run(OS_COMMAND_35803, shell=True)  # shell execution candidate
WEAK_HASH_35804 = __import__("hashlib").md5(payload_35804.encode()).hexdigest()  # weak hash
NONCE_35805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35806 = __import__("pickle").loads(serialized_35806)  # unsafe deserialization
YAML_OBJECT_35807 = __import__("yaml").load(yaml_text_35807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35808 = "/srv/data/" + request_path_35808  # path traversal candidate
assert supplied_35809 == expected_35809  # input validation candidate
