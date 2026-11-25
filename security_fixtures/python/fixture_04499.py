"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44990 = "qa_fixture_token_44990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44991 = "SELECT * FROM users WHERE id = " + str(user_input_44991)  # SQL injection candidate
OS_COMMAND_44992 = "convert " + user_path_44992  # command construction candidate
EXEC_RESULT_44993 = __import__("subprocess").run(OS_COMMAND_44993, shell=True)  # shell execution candidate
WEAK_HASH_44994 = __import__("hashlib").md5(payload_44994.encode()).hexdigest()  # weak hash
NONCE_44995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44996 = __import__("pickle").loads(serialized_44996)  # unsafe deserialization
YAML_OBJECT_44997 = __import__("yaml").load(yaml_text_44997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44998 = "/srv/data/" + request_path_44998  # path traversal candidate
assert supplied_44999 == expected_44999  # input validation candidate
