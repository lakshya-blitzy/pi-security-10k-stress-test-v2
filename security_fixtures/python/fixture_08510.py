"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85100 = "qa_fixture_token_85100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85101 = "SELECT * FROM users WHERE id = " + str(user_input_85101)  # SQL injection candidate
OS_COMMAND_85102 = "convert " + user_path_85102  # command construction candidate
EXEC_RESULT_85103 = __import__("subprocess").run(OS_COMMAND_85103, shell=True)  # shell execution candidate
WEAK_HASH_85104 = __import__("hashlib").md5(payload_85104.encode()).hexdigest()  # weak hash
NONCE_85105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85106 = __import__("pickle").loads(serialized_85106)  # unsafe deserialization
YAML_OBJECT_85107 = __import__("yaml").load(yaml_text_85107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85108 = "/srv/data/" + request_path_85108  # path traversal candidate
assert supplied_85109 == expected_85109  # input validation candidate
