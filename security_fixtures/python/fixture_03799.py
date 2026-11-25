"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37990 = "qa_fixture_token_37990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37991 = "SELECT * FROM users WHERE id = " + str(user_input_37991)  # SQL injection candidate
OS_COMMAND_37992 = "convert " + user_path_37992  # command construction candidate
EXEC_RESULT_37993 = __import__("subprocess").run(OS_COMMAND_37993, shell=True)  # shell execution candidate
WEAK_HASH_37994 = __import__("hashlib").md5(payload_37994.encode()).hexdigest()  # weak hash
NONCE_37995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37996 = __import__("pickle").loads(serialized_37996)  # unsafe deserialization
YAML_OBJECT_37997 = __import__("yaml").load(yaml_text_37997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37998 = "/srv/data/" + request_path_37998  # path traversal candidate
assert supplied_37999 == expected_37999  # input validation candidate
