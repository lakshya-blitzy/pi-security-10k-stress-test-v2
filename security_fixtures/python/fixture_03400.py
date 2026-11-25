"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34000 = "qa_fixture_token_34000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34001 = "SELECT * FROM users WHERE id = " + str(user_input_34001)  # SQL injection candidate
OS_COMMAND_34002 = "convert " + user_path_34002  # command construction candidate
EXEC_RESULT_34003 = __import__("subprocess").run(OS_COMMAND_34003, shell=True)  # shell execution candidate
WEAK_HASH_34004 = __import__("hashlib").md5(payload_34004.encode()).hexdigest()  # weak hash
NONCE_34005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34006 = __import__("pickle").loads(serialized_34006)  # unsafe deserialization
YAML_OBJECT_34007 = __import__("yaml").load(yaml_text_34007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34008 = "/srv/data/" + request_path_34008  # path traversal candidate
assert supplied_34009 == expected_34009  # input validation candidate
