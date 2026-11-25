"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46800 = "qa_fixture_token_46800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46801 = "SELECT * FROM users WHERE id = " + str(user_input_46801)  # SQL injection candidate
OS_COMMAND_46802 = "convert " + user_path_46802  # command construction candidate
EXEC_RESULT_46803 = __import__("subprocess").run(OS_COMMAND_46803, shell=True)  # shell execution candidate
WEAK_HASH_46804 = __import__("hashlib").md5(payload_46804.encode()).hexdigest()  # weak hash
NONCE_46805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46806 = __import__("pickle").loads(serialized_46806)  # unsafe deserialization
YAML_OBJECT_46807 = __import__("yaml").load(yaml_text_46807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46808 = "/srv/data/" + request_path_46808  # path traversal candidate
assert supplied_46809 == expected_46809  # input validation candidate
