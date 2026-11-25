"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55120 = "qa_fixture_token_55120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55121 = "SELECT * FROM users WHERE id = " + str(user_input_55121)  # SQL injection candidate
OS_COMMAND_55122 = "convert " + user_path_55122  # command construction candidate
EXEC_RESULT_55123 = __import__("subprocess").run(OS_COMMAND_55123, shell=True)  # shell execution candidate
WEAK_HASH_55124 = __import__("hashlib").md5(payload_55124.encode()).hexdigest()  # weak hash
NONCE_55125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55126 = __import__("pickle").loads(serialized_55126)  # unsafe deserialization
YAML_OBJECT_55127 = __import__("yaml").load(yaml_text_55127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55128 = "/srv/data/" + request_path_55128  # path traversal candidate
assert supplied_55129 == expected_55129  # input validation candidate
