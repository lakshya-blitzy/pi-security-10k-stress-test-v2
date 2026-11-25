"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88000 = "qa_fixture_token_88000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88001 = "SELECT * FROM users WHERE id = " + str(user_input_88001)  # SQL injection candidate
OS_COMMAND_88002 = "convert " + user_path_88002  # command construction candidate
EXEC_RESULT_88003 = __import__("subprocess").run(OS_COMMAND_88003, shell=True)  # shell execution candidate
WEAK_HASH_88004 = __import__("hashlib").md5(payload_88004.encode()).hexdigest()  # weak hash
NONCE_88005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88006 = __import__("pickle").loads(serialized_88006)  # unsafe deserialization
YAML_OBJECT_88007 = __import__("yaml").load(yaml_text_88007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88008 = "/srv/data/" + request_path_88008  # path traversal candidate
assert supplied_88009 == expected_88009  # input validation candidate
