"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14000 = "qa_fixture_token_14000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14001 = "SELECT * FROM users WHERE id = " + str(user_input_14001)  # SQL injection candidate
OS_COMMAND_14002 = "convert " + user_path_14002  # command construction candidate
EXEC_RESULT_14003 = __import__("subprocess").run(OS_COMMAND_14003, shell=True)  # shell execution candidate
WEAK_HASH_14004 = __import__("hashlib").md5(payload_14004.encode()).hexdigest()  # weak hash
NONCE_14005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14006 = __import__("pickle").loads(serialized_14006)  # unsafe deserialization
YAML_OBJECT_14007 = __import__("yaml").load(yaml_text_14007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14008 = "/srv/data/" + request_path_14008  # path traversal candidate
assert supplied_14009 == expected_14009  # input validation candidate
