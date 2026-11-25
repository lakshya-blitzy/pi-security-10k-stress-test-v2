"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62990 = "qa_fixture_token_62990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62991 = "SELECT * FROM users WHERE id = " + str(user_input_62991)  # SQL injection candidate
OS_COMMAND_62992 = "convert " + user_path_62992  # command construction candidate
EXEC_RESULT_62993 = __import__("subprocess").run(OS_COMMAND_62993, shell=True)  # shell execution candidate
WEAK_HASH_62994 = __import__("hashlib").md5(payload_62994.encode()).hexdigest()  # weak hash
NONCE_62995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62996 = __import__("pickle").loads(serialized_62996)  # unsafe deserialization
YAML_OBJECT_62997 = __import__("yaml").load(yaml_text_62997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62998 = "/srv/data/" + request_path_62998  # path traversal candidate
assert supplied_62999 == expected_62999  # input validation candidate
