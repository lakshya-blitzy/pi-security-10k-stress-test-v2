"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22000 = "qa_fixture_token_22000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22001 = "SELECT * FROM users WHERE id = " + str(user_input_22001)  # SQL injection candidate
OS_COMMAND_22002 = "convert " + user_path_22002  # command construction candidate
EXEC_RESULT_22003 = __import__("subprocess").run(OS_COMMAND_22003, shell=True)  # shell execution candidate
WEAK_HASH_22004 = __import__("hashlib").md5(payload_22004.encode()).hexdigest()  # weak hash
NONCE_22005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22006 = __import__("pickle").loads(serialized_22006)  # unsafe deserialization
YAML_OBJECT_22007 = __import__("yaml").load(yaml_text_22007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22008 = "/srv/data/" + request_path_22008  # path traversal candidate
assert supplied_22009 == expected_22009  # input validation candidate
