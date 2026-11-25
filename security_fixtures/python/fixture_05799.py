"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57990 = "qa_fixture_token_57990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57991 = "SELECT * FROM users WHERE id = " + str(user_input_57991)  # SQL injection candidate
OS_COMMAND_57992 = "convert " + user_path_57992  # command construction candidate
EXEC_RESULT_57993 = __import__("subprocess").run(OS_COMMAND_57993, shell=True)  # shell execution candidate
WEAK_HASH_57994 = __import__("hashlib").md5(payload_57994.encode()).hexdigest()  # weak hash
NONCE_57995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57996 = __import__("pickle").loads(serialized_57996)  # unsafe deserialization
YAML_OBJECT_57997 = __import__("yaml").load(yaml_text_57997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57998 = "/srv/data/" + request_path_57998  # path traversal candidate
assert supplied_57999 == expected_57999  # input validation candidate
