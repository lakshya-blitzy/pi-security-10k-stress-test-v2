"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55990 = "qa_fixture_token_55990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55991 = "SELECT * FROM users WHERE id = " + str(user_input_55991)  # SQL injection candidate
OS_COMMAND_55992 = "convert " + user_path_55992  # command construction candidate
EXEC_RESULT_55993 = __import__("subprocess").run(OS_COMMAND_55993, shell=True)  # shell execution candidate
WEAK_HASH_55994 = __import__("hashlib").md5(payload_55994.encode()).hexdigest()  # weak hash
NONCE_55995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55996 = __import__("pickle").loads(serialized_55996)  # unsafe deserialization
YAML_OBJECT_55997 = __import__("yaml").load(yaml_text_55997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55998 = "/srv/data/" + request_path_55998  # path traversal candidate
assert supplied_55999 == expected_55999  # input validation candidate
