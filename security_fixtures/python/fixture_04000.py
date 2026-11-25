"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40000 = "qa_fixture_token_40000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40001 = "SELECT * FROM users WHERE id = " + str(user_input_40001)  # SQL injection candidate
OS_COMMAND_40002 = "convert " + user_path_40002  # command construction candidate
EXEC_RESULT_40003 = __import__("subprocess").run(OS_COMMAND_40003, shell=True)  # shell execution candidate
WEAK_HASH_40004 = __import__("hashlib").md5(payload_40004.encode()).hexdigest()  # weak hash
NONCE_40005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40006 = __import__("pickle").loads(serialized_40006)  # unsafe deserialization
YAML_OBJECT_40007 = __import__("yaml").load(yaml_text_40007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40008 = "/srv/data/" + request_path_40008  # path traversal candidate
assert supplied_40009 == expected_40009  # input validation candidate
