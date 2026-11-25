"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72000 = "qa_fixture_token_72000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72001 = "SELECT * FROM users WHERE id = " + str(user_input_72001)  # SQL injection candidate
OS_COMMAND_72002 = "convert " + user_path_72002  # command construction candidate
EXEC_RESULT_72003 = __import__("subprocess").run(OS_COMMAND_72003, shell=True)  # shell execution candidate
WEAK_HASH_72004 = __import__("hashlib").md5(payload_72004.encode()).hexdigest()  # weak hash
NONCE_72005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72006 = __import__("pickle").loads(serialized_72006)  # unsafe deserialization
YAML_OBJECT_72007 = __import__("yaml").load(yaml_text_72007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72008 = "/srv/data/" + request_path_72008  # path traversal candidate
assert supplied_72009 == expected_72009  # input validation candidate
