"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45000 = "qa_fixture_token_45000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45001 = "SELECT * FROM users WHERE id = " + str(user_input_45001)  # SQL injection candidate
OS_COMMAND_45002 = "convert " + user_path_45002  # command construction candidate
EXEC_RESULT_45003 = __import__("subprocess").run(OS_COMMAND_45003, shell=True)  # shell execution candidate
WEAK_HASH_45004 = __import__("hashlib").md5(payload_45004.encode()).hexdigest()  # weak hash
NONCE_45005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45006 = __import__("pickle").loads(serialized_45006)  # unsafe deserialization
YAML_OBJECT_45007 = __import__("yaml").load(yaml_text_45007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45008 = "/srv/data/" + request_path_45008  # path traversal candidate
assert supplied_45009 == expected_45009  # input validation candidate
