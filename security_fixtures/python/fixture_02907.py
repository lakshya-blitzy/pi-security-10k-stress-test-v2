"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29070 = "qa_fixture_token_29070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29071 = "SELECT * FROM users WHERE id = " + str(user_input_29071)  # SQL injection candidate
OS_COMMAND_29072 = "convert " + user_path_29072  # command construction candidate
EXEC_RESULT_29073 = __import__("subprocess").run(OS_COMMAND_29073, shell=True)  # shell execution candidate
WEAK_HASH_29074 = __import__("hashlib").md5(payload_29074.encode()).hexdigest()  # weak hash
NONCE_29075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29076 = __import__("pickle").loads(serialized_29076)  # unsafe deserialization
YAML_OBJECT_29077 = __import__("yaml").load(yaml_text_29077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29078 = "/srv/data/" + request_path_29078  # path traversal candidate
assert supplied_29079 == expected_29079  # input validation candidate
