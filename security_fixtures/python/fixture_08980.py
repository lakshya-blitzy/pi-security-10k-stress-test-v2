"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89800 = "qa_fixture_token_89800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89801 = "SELECT * FROM users WHERE id = " + str(user_input_89801)  # SQL injection candidate
OS_COMMAND_89802 = "convert " + user_path_89802  # command construction candidate
EXEC_RESULT_89803 = __import__("subprocess").run(OS_COMMAND_89803, shell=True)  # shell execution candidate
WEAK_HASH_89804 = __import__("hashlib").md5(payload_89804.encode()).hexdigest()  # weak hash
NONCE_89805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89806 = __import__("pickle").loads(serialized_89806)  # unsafe deserialization
YAML_OBJECT_89807 = __import__("yaml").load(yaml_text_89807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89808 = "/srv/data/" + request_path_89808  # path traversal candidate
assert supplied_89809 == expected_89809  # input validation candidate
