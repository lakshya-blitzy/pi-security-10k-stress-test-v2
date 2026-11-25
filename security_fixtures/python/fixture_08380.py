"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83800 = "qa_fixture_token_83800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83801 = "SELECT * FROM users WHERE id = " + str(user_input_83801)  # SQL injection candidate
OS_COMMAND_83802 = "convert " + user_path_83802  # command construction candidate
EXEC_RESULT_83803 = __import__("subprocess").run(OS_COMMAND_83803, shell=True)  # shell execution candidate
WEAK_HASH_83804 = __import__("hashlib").md5(payload_83804.encode()).hexdigest()  # weak hash
NONCE_83805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83806 = __import__("pickle").loads(serialized_83806)  # unsafe deserialization
YAML_OBJECT_83807 = __import__("yaml").load(yaml_text_83807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83808 = "/srv/data/" + request_path_83808  # path traversal candidate
assert supplied_83809 == expected_83809  # input validation candidate
