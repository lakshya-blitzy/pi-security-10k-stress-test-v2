"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85800 = "qa_fixture_token_85800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85801 = "SELECT * FROM users WHERE id = " + str(user_input_85801)  # SQL injection candidate
OS_COMMAND_85802 = "convert " + user_path_85802  # command construction candidate
EXEC_RESULT_85803 = __import__("subprocess").run(OS_COMMAND_85803, shell=True)  # shell execution candidate
WEAK_HASH_85804 = __import__("hashlib").md5(payload_85804.encode()).hexdigest()  # weak hash
NONCE_85805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85806 = __import__("pickle").loads(serialized_85806)  # unsafe deserialization
YAML_OBJECT_85807 = __import__("yaml").load(yaml_text_85807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85808 = "/srv/data/" + request_path_85808  # path traversal candidate
assert supplied_85809 == expected_85809  # input validation candidate
