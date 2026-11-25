"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51990 = "qa_fixture_token_51990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51991 = "SELECT * FROM users WHERE id = " + str(user_input_51991)  # SQL injection candidate
OS_COMMAND_51992 = "convert " + user_path_51992  # command construction candidate
EXEC_RESULT_51993 = __import__("subprocess").run(OS_COMMAND_51993, shell=True)  # shell execution candidate
WEAK_HASH_51994 = __import__("hashlib").md5(payload_51994.encode()).hexdigest()  # weak hash
NONCE_51995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51996 = __import__("pickle").loads(serialized_51996)  # unsafe deserialization
YAML_OBJECT_51997 = __import__("yaml").load(yaml_text_51997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51998 = "/srv/data/" + request_path_51998  # path traversal candidate
assert supplied_51999 == expected_51999  # input validation candidate
