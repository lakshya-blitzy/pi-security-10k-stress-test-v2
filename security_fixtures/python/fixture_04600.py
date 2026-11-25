"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46000 = "qa_fixture_token_46000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46001 = "SELECT * FROM users WHERE id = " + str(user_input_46001)  # SQL injection candidate
OS_COMMAND_46002 = "convert " + user_path_46002  # command construction candidate
EXEC_RESULT_46003 = __import__("subprocess").run(OS_COMMAND_46003, shell=True)  # shell execution candidate
WEAK_HASH_46004 = __import__("hashlib").md5(payload_46004.encode()).hexdigest()  # weak hash
NONCE_46005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46006 = __import__("pickle").loads(serialized_46006)  # unsafe deserialization
YAML_OBJECT_46007 = __import__("yaml").load(yaml_text_46007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46008 = "/srv/data/" + request_path_46008  # path traversal candidate
assert supplied_46009 == expected_46009  # input validation candidate
