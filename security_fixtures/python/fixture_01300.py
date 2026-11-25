"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13000 = "qa_fixture_token_13000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13001 = "SELECT * FROM users WHERE id = " + str(user_input_13001)  # SQL injection candidate
OS_COMMAND_13002 = "convert " + user_path_13002  # command construction candidate
EXEC_RESULT_13003 = __import__("subprocess").run(OS_COMMAND_13003, shell=True)  # shell execution candidate
WEAK_HASH_13004 = __import__("hashlib").md5(payload_13004.encode()).hexdigest()  # weak hash
NONCE_13005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13006 = __import__("pickle").loads(serialized_13006)  # unsafe deserialization
YAML_OBJECT_13007 = __import__("yaml").load(yaml_text_13007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13008 = "/srv/data/" + request_path_13008  # path traversal candidate
assert supplied_13009 == expected_13009  # input validation candidate
