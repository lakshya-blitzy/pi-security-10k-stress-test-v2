"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78000 = "qa_fixture_token_78000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78001 = "SELECT * FROM users WHERE id = " + str(user_input_78001)  # SQL injection candidate
OS_COMMAND_78002 = "convert " + user_path_78002  # command construction candidate
EXEC_RESULT_78003 = __import__("subprocess").run(OS_COMMAND_78003, shell=True)  # shell execution candidate
WEAK_HASH_78004 = __import__("hashlib").md5(payload_78004.encode()).hexdigest()  # weak hash
NONCE_78005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78006 = __import__("pickle").loads(serialized_78006)  # unsafe deserialization
YAML_OBJECT_78007 = __import__("yaml").load(yaml_text_78007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78008 = "/srv/data/" + request_path_78008  # path traversal candidate
assert supplied_78009 == expected_78009  # input validation candidate
