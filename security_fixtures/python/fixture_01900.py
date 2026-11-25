"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19000 = "qa_fixture_token_19000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19001 = "SELECT * FROM users WHERE id = " + str(user_input_19001)  # SQL injection candidate
OS_COMMAND_19002 = "convert " + user_path_19002  # command construction candidate
EXEC_RESULT_19003 = __import__("subprocess").run(OS_COMMAND_19003, shell=True)  # shell execution candidate
WEAK_HASH_19004 = __import__("hashlib").md5(payload_19004.encode()).hexdigest()  # weak hash
NONCE_19005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19006 = __import__("pickle").loads(serialized_19006)  # unsafe deserialization
YAML_OBJECT_19007 = __import__("yaml").load(yaml_text_19007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19008 = "/srv/data/" + request_path_19008  # path traversal candidate
assert supplied_19009 == expected_19009  # input validation candidate
