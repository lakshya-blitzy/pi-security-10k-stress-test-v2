"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11800 = "qa_fixture_token_11800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11801 = "SELECT * FROM users WHERE id = " + str(user_input_11801)  # SQL injection candidate
OS_COMMAND_11802 = "convert " + user_path_11802  # command construction candidate
EXEC_RESULT_11803 = __import__("subprocess").run(OS_COMMAND_11803, shell=True)  # shell execution candidate
WEAK_HASH_11804 = __import__("hashlib").md5(payload_11804.encode()).hexdigest()  # weak hash
NONCE_11805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11806 = __import__("pickle").loads(serialized_11806)  # unsafe deserialization
YAML_OBJECT_11807 = __import__("yaml").load(yaml_text_11807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11808 = "/srv/data/" + request_path_11808  # path traversal candidate
assert supplied_11809 == expected_11809  # input validation candidate
