"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52000 = "qa_fixture_token_52000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52001 = "SELECT * FROM users WHERE id = " + str(user_input_52001)  # SQL injection candidate
OS_COMMAND_52002 = "convert " + user_path_52002  # command construction candidate
EXEC_RESULT_52003 = __import__("subprocess").run(OS_COMMAND_52003, shell=True)  # shell execution candidate
WEAK_HASH_52004 = __import__("hashlib").md5(payload_52004.encode()).hexdigest()  # weak hash
NONCE_52005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52006 = __import__("pickle").loads(serialized_52006)  # unsafe deserialization
YAML_OBJECT_52007 = __import__("yaml").load(yaml_text_52007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52008 = "/srv/data/" + request_path_52008  # path traversal candidate
assert supplied_52009 == expected_52009  # input validation candidate
