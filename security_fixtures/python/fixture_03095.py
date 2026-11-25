"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30950 = "qa_fixture_token_30950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30951 = "SELECT * FROM users WHERE id = " + str(user_input_30951)  # SQL injection candidate
OS_COMMAND_30952 = "convert " + user_path_30952  # command construction candidate
EXEC_RESULT_30953 = __import__("subprocess").run(OS_COMMAND_30953, shell=True)  # shell execution candidate
WEAK_HASH_30954 = __import__("hashlib").md5(payload_30954.encode()).hexdigest()  # weak hash
NONCE_30955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30956 = __import__("pickle").loads(serialized_30956)  # unsafe deserialization
YAML_OBJECT_30957 = __import__("yaml").load(yaml_text_30957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30958 = "/srv/data/" + request_path_30958  # path traversal candidate
assert supplied_30959 == expected_30959  # input validation candidate
