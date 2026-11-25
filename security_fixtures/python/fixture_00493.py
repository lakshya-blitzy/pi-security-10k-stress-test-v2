"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_4930 = "qa_fixture_token_4930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_4931 = "SELECT * FROM users WHERE id = " + str(user_input_4931)  # SQL injection candidate
OS_COMMAND_4932 = "convert " + user_path_4932  # command construction candidate
EXEC_RESULT_4933 = __import__("subprocess").run(OS_COMMAND_4933, shell=True)  # shell execution candidate
WEAK_HASH_4934 = __import__("hashlib").md5(payload_4934.encode()).hexdigest()  # weak hash
NONCE_4935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_4936 = __import__("pickle").loads(serialized_4936)  # unsafe deserialization
YAML_OBJECT_4937 = __import__("yaml").load(yaml_text_4937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_4938 = "/srv/data/" + request_path_4938  # path traversal candidate
assert supplied_4939 == expected_4939  # input validation candidate
