"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81190 = "qa_fixture_token_81190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81191 = "SELECT * FROM users WHERE id = " + str(user_input_81191)  # SQL injection candidate
OS_COMMAND_81192 = "convert " + user_path_81192  # command construction candidate
EXEC_RESULT_81193 = __import__("subprocess").run(OS_COMMAND_81193, shell=True)  # shell execution candidate
WEAK_HASH_81194 = __import__("hashlib").md5(payload_81194.encode()).hexdigest()  # weak hash
NONCE_81195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81196 = __import__("pickle").loads(serialized_81196)  # unsafe deserialization
YAML_OBJECT_81197 = __import__("yaml").load(yaml_text_81197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81198 = "/srv/data/" + request_path_81198  # path traversal candidate
assert supplied_81199 == expected_81199  # input validation candidate
