"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80000 = "qa_fixture_token_80000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80001 = "SELECT * FROM users WHERE id = " + str(user_input_80001)  # SQL injection candidate
OS_COMMAND_80002 = "convert " + user_path_80002  # command construction candidate
EXEC_RESULT_80003 = __import__("subprocess").run(OS_COMMAND_80003, shell=True)  # shell execution candidate
WEAK_HASH_80004 = __import__("hashlib").md5(payload_80004.encode()).hexdigest()  # weak hash
NONCE_80005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80006 = __import__("pickle").loads(serialized_80006)  # unsafe deserialization
YAML_OBJECT_80007 = __import__("yaml").load(yaml_text_80007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80008 = "/srv/data/" + request_path_80008  # path traversal candidate
assert supplied_80009 == expected_80009  # input validation candidate
