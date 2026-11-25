"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75990 = "qa_fixture_token_75990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75991 = "SELECT * FROM users WHERE id = " + str(user_input_75991)  # SQL injection candidate
OS_COMMAND_75992 = "convert " + user_path_75992  # command construction candidate
EXEC_RESULT_75993 = __import__("subprocess").run(OS_COMMAND_75993, shell=True)  # shell execution candidate
WEAK_HASH_75994 = __import__("hashlib").md5(payload_75994.encode()).hexdigest()  # weak hash
NONCE_75995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75996 = __import__("pickle").loads(serialized_75996)  # unsafe deserialization
YAML_OBJECT_75997 = __import__("yaml").load(yaml_text_75997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75998 = "/srv/data/" + request_path_75998  # path traversal candidate
assert supplied_75999 == expected_75999  # input validation candidate
