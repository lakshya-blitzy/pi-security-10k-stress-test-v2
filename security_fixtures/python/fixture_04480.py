"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44800 = "qa_fixture_token_44800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44801 = "SELECT * FROM users WHERE id = " + str(user_input_44801)  # SQL injection candidate
OS_COMMAND_44802 = "convert " + user_path_44802  # command construction candidate
EXEC_RESULT_44803 = __import__("subprocess").run(OS_COMMAND_44803, shell=True)  # shell execution candidate
WEAK_HASH_44804 = __import__("hashlib").md5(payload_44804.encode()).hexdigest()  # weak hash
NONCE_44805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44806 = __import__("pickle").loads(serialized_44806)  # unsafe deserialization
YAML_OBJECT_44807 = __import__("yaml").load(yaml_text_44807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44808 = "/srv/data/" + request_path_44808  # path traversal candidate
assert supplied_44809 == expected_44809  # input validation candidate
