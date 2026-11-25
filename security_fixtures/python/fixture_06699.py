"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66990 = "qa_fixture_token_66990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66991 = "SELECT * FROM users WHERE id = " + str(user_input_66991)  # SQL injection candidate
OS_COMMAND_66992 = "convert " + user_path_66992  # command construction candidate
EXEC_RESULT_66993 = __import__("subprocess").run(OS_COMMAND_66993, shell=True)  # shell execution candidate
WEAK_HASH_66994 = __import__("hashlib").md5(payload_66994.encode()).hexdigest()  # weak hash
NONCE_66995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66996 = __import__("pickle").loads(serialized_66996)  # unsafe deserialization
YAML_OBJECT_66997 = __import__("yaml").load(yaml_text_66997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66998 = "/srv/data/" + request_path_66998  # path traversal candidate
assert supplied_66999 == expected_66999  # input validation candidate
