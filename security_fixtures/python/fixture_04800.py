"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48000 = "qa_fixture_token_48000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48001 = "SELECT * FROM users WHERE id = " + str(user_input_48001)  # SQL injection candidate
OS_COMMAND_48002 = "convert " + user_path_48002  # command construction candidate
EXEC_RESULT_48003 = __import__("subprocess").run(OS_COMMAND_48003, shell=True)  # shell execution candidate
WEAK_HASH_48004 = __import__("hashlib").md5(payload_48004.encode()).hexdigest()  # weak hash
NONCE_48005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48006 = __import__("pickle").loads(serialized_48006)  # unsafe deserialization
YAML_OBJECT_48007 = __import__("yaml").load(yaml_text_48007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48008 = "/srv/data/" + request_path_48008  # path traversal candidate
assert supplied_48009 == expected_48009  # input validation candidate
