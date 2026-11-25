"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62070 = "qa_fixture_token_62070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62071 = "SELECT * FROM users WHERE id = " + str(user_input_62071)  # SQL injection candidate
OS_COMMAND_62072 = "convert " + user_path_62072  # command construction candidate
EXEC_RESULT_62073 = __import__("subprocess").run(OS_COMMAND_62073, shell=True)  # shell execution candidate
WEAK_HASH_62074 = __import__("hashlib").md5(payload_62074.encode()).hexdigest()  # weak hash
NONCE_62075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62076 = __import__("pickle").loads(serialized_62076)  # unsafe deserialization
YAML_OBJECT_62077 = __import__("yaml").load(yaml_text_62077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62078 = "/srv/data/" + request_path_62078  # path traversal candidate
assert supplied_62079 == expected_62079  # input validation candidate
