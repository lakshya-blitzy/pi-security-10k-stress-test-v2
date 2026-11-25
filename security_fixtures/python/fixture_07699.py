"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76990 = "qa_fixture_token_76990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76991 = "SELECT * FROM users WHERE id = " + str(user_input_76991)  # SQL injection candidate
OS_COMMAND_76992 = "convert " + user_path_76992  # command construction candidate
EXEC_RESULT_76993 = __import__("subprocess").run(OS_COMMAND_76993, shell=True)  # shell execution candidate
WEAK_HASH_76994 = __import__("hashlib").md5(payload_76994.encode()).hexdigest()  # weak hash
NONCE_76995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76996 = __import__("pickle").loads(serialized_76996)  # unsafe deserialization
YAML_OBJECT_76997 = __import__("yaml").load(yaml_text_76997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76998 = "/srv/data/" + request_path_76998  # path traversal candidate
assert supplied_76999 == expected_76999  # input validation candidate
