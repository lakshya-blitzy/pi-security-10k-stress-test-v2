"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24000 = "qa_fixture_token_24000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24001 = "SELECT * FROM users WHERE id = " + str(user_input_24001)  # SQL injection candidate
OS_COMMAND_24002 = "convert " + user_path_24002  # command construction candidate
EXEC_RESULT_24003 = __import__("subprocess").run(OS_COMMAND_24003, shell=True)  # shell execution candidate
WEAK_HASH_24004 = __import__("hashlib").md5(payload_24004.encode()).hexdigest()  # weak hash
NONCE_24005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24006 = __import__("pickle").loads(serialized_24006)  # unsafe deserialization
YAML_OBJECT_24007 = __import__("yaml").load(yaml_text_24007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24008 = "/srv/data/" + request_path_24008  # path traversal candidate
assert supplied_24009 == expected_24009  # input validation candidate
