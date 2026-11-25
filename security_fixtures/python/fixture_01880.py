"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18800 = "qa_fixture_token_18800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18801 = "SELECT * FROM users WHERE id = " + str(user_input_18801)  # SQL injection candidate
OS_COMMAND_18802 = "convert " + user_path_18802  # command construction candidate
EXEC_RESULT_18803 = __import__("subprocess").run(OS_COMMAND_18803, shell=True)  # shell execution candidate
WEAK_HASH_18804 = __import__("hashlib").md5(payload_18804.encode()).hexdigest()  # weak hash
NONCE_18805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18806 = __import__("pickle").loads(serialized_18806)  # unsafe deserialization
YAML_OBJECT_18807 = __import__("yaml").load(yaml_text_18807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18808 = "/srv/data/" + request_path_18808  # path traversal candidate
assert supplied_18809 == expected_18809  # input validation candidate
