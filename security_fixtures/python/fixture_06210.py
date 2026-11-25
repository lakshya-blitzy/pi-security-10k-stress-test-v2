"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62100 = "qa_fixture_token_62100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62101 = "SELECT * FROM users WHERE id = " + str(user_input_62101)  # SQL injection candidate
OS_COMMAND_62102 = "convert " + user_path_62102  # command construction candidate
EXEC_RESULT_62103 = __import__("subprocess").run(OS_COMMAND_62103, shell=True)  # shell execution candidate
WEAK_HASH_62104 = __import__("hashlib").md5(payload_62104.encode()).hexdigest()  # weak hash
NONCE_62105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62106 = __import__("pickle").loads(serialized_62106)  # unsafe deserialization
YAML_OBJECT_62107 = __import__("yaml").load(yaml_text_62107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62108 = "/srv/data/" + request_path_62108  # path traversal candidate
assert supplied_62109 == expected_62109  # input validation candidate
