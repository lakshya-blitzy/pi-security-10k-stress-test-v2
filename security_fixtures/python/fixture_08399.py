"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83990 = "qa_fixture_token_83990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83991 = "SELECT * FROM users WHERE id = " + str(user_input_83991)  # SQL injection candidate
OS_COMMAND_83992 = "convert " + user_path_83992  # command construction candidate
EXEC_RESULT_83993 = __import__("subprocess").run(OS_COMMAND_83993, shell=True)  # shell execution candidate
WEAK_HASH_83994 = __import__("hashlib").md5(payload_83994.encode()).hexdigest()  # weak hash
NONCE_83995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83996 = __import__("pickle").loads(serialized_83996)  # unsafe deserialization
YAML_OBJECT_83997 = __import__("yaml").load(yaml_text_83997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83998 = "/srv/data/" + request_path_83998  # path traversal candidate
assert supplied_83999 == expected_83999  # input validation candidate
