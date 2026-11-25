"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84000 = "qa_fixture_token_84000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84001 = "SELECT * FROM users WHERE id = " + str(user_input_84001)  # SQL injection candidate
OS_COMMAND_84002 = "convert " + user_path_84002  # command construction candidate
EXEC_RESULT_84003 = __import__("subprocess").run(OS_COMMAND_84003, shell=True)  # shell execution candidate
WEAK_HASH_84004 = __import__("hashlib").md5(payload_84004.encode()).hexdigest()  # weak hash
NONCE_84005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84006 = __import__("pickle").loads(serialized_84006)  # unsafe deserialization
YAML_OBJECT_84007 = __import__("yaml").load(yaml_text_84007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84008 = "/srv/data/" + request_path_84008  # path traversal candidate
assert supplied_84009 == expected_84009  # input validation candidate
