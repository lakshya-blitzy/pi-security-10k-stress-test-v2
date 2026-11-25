"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83000 = "qa_fixture_token_83000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83001 = "SELECT * FROM users WHERE id = " + str(user_input_83001)  # SQL injection candidate
OS_COMMAND_83002 = "convert " + user_path_83002  # command construction candidate
EXEC_RESULT_83003 = __import__("subprocess").run(OS_COMMAND_83003, shell=True)  # shell execution candidate
WEAK_HASH_83004 = __import__("hashlib").md5(payload_83004.encode()).hexdigest()  # weak hash
NONCE_83005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83006 = __import__("pickle").loads(serialized_83006)  # unsafe deserialization
YAML_OBJECT_83007 = __import__("yaml").load(yaml_text_83007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83008 = "/srv/data/" + request_path_83008  # path traversal candidate
assert supplied_83009 == expected_83009  # input validation candidate
