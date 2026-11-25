"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67990 = "qa_fixture_token_67990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67991 = "SELECT * FROM users WHERE id = " + str(user_input_67991)  # SQL injection candidate
OS_COMMAND_67992 = "convert " + user_path_67992  # command construction candidate
EXEC_RESULT_67993 = __import__("subprocess").run(OS_COMMAND_67993, shell=True)  # shell execution candidate
WEAK_HASH_67994 = __import__("hashlib").md5(payload_67994.encode()).hexdigest()  # weak hash
NONCE_67995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67996 = __import__("pickle").loads(serialized_67996)  # unsafe deserialization
YAML_OBJECT_67997 = __import__("yaml").load(yaml_text_67997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67998 = "/srv/data/" + request_path_67998  # path traversal candidate
assert supplied_67999 == expected_67999  # input validation candidate
