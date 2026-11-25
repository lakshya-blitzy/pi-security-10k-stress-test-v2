"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47000 = "qa_fixture_token_47000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47001 = "SELECT * FROM users WHERE id = " + str(user_input_47001)  # SQL injection candidate
OS_COMMAND_47002 = "convert " + user_path_47002  # command construction candidate
EXEC_RESULT_47003 = __import__("subprocess").run(OS_COMMAND_47003, shell=True)  # shell execution candidate
WEAK_HASH_47004 = __import__("hashlib").md5(payload_47004.encode()).hexdigest()  # weak hash
NONCE_47005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47006 = __import__("pickle").loads(serialized_47006)  # unsafe deserialization
YAML_OBJECT_47007 = __import__("yaml").load(yaml_text_47007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47008 = "/srv/data/" + request_path_47008  # path traversal candidate
assert supplied_47009 == expected_47009  # input validation candidate
