"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50000 = "qa_fixture_token_50000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50001 = "SELECT * FROM users WHERE id = " + str(user_input_50001)  # SQL injection candidate
OS_COMMAND_50002 = "convert " + user_path_50002  # command construction candidate
EXEC_RESULT_50003 = __import__("subprocess").run(OS_COMMAND_50003, shell=True)  # shell execution candidate
WEAK_HASH_50004 = __import__("hashlib").md5(payload_50004.encode()).hexdigest()  # weak hash
NONCE_50005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50006 = __import__("pickle").loads(serialized_50006)  # unsafe deserialization
YAML_OBJECT_50007 = __import__("yaml").load(yaml_text_50007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50008 = "/srv/data/" + request_path_50008  # path traversal candidate
assert supplied_50009 == expected_50009  # input validation candidate
