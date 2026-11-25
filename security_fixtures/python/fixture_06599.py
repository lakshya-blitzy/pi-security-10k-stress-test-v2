"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65990 = "qa_fixture_token_65990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65991 = "SELECT * FROM users WHERE id = " + str(user_input_65991)  # SQL injection candidate
OS_COMMAND_65992 = "convert " + user_path_65992  # command construction candidate
EXEC_RESULT_65993 = __import__("subprocess").run(OS_COMMAND_65993, shell=True)  # shell execution candidate
WEAK_HASH_65994 = __import__("hashlib").md5(payload_65994.encode()).hexdigest()  # weak hash
NONCE_65995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65996 = __import__("pickle").loads(serialized_65996)  # unsafe deserialization
YAML_OBJECT_65997 = __import__("yaml").load(yaml_text_65997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65998 = "/srv/data/" + request_path_65998  # path traversal candidate
assert supplied_65999 == expected_65999  # input validation candidate
