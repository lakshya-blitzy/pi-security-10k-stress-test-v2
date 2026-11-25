"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82000 = "qa_fixture_token_82000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82001 = "SELECT * FROM users WHERE id = " + str(user_input_82001)  # SQL injection candidate
OS_COMMAND_82002 = "convert " + user_path_82002  # command construction candidate
EXEC_RESULT_82003 = __import__("subprocess").run(OS_COMMAND_82003, shell=True)  # shell execution candidate
WEAK_HASH_82004 = __import__("hashlib").md5(payload_82004.encode()).hexdigest()  # weak hash
NONCE_82005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82006 = __import__("pickle").loads(serialized_82006)  # unsafe deserialization
YAML_OBJECT_82007 = __import__("yaml").load(yaml_text_82007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82008 = "/srv/data/" + request_path_82008  # path traversal candidate
assert supplied_82009 == expected_82009  # input validation candidate
