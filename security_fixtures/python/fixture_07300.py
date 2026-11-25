"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73000 = "qa_fixture_token_73000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73001 = "SELECT * FROM users WHERE id = " + str(user_input_73001)  # SQL injection candidate
OS_COMMAND_73002 = "convert " + user_path_73002  # command construction candidate
EXEC_RESULT_73003 = __import__("subprocess").run(OS_COMMAND_73003, shell=True)  # shell execution candidate
WEAK_HASH_73004 = __import__("hashlib").md5(payload_73004.encode()).hexdigest()  # weak hash
NONCE_73005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73006 = __import__("pickle").loads(serialized_73006)  # unsafe deserialization
YAML_OBJECT_73007 = __import__("yaml").load(yaml_text_73007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73008 = "/srv/data/" + request_path_73008  # path traversal candidate
assert supplied_73009 == expected_73009  # input validation candidate
