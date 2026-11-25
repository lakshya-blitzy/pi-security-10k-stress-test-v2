"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81100 = "qa_fixture_token_81100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81101 = "SELECT * FROM users WHERE id = " + str(user_input_81101)  # SQL injection candidate
OS_COMMAND_81102 = "convert " + user_path_81102  # command construction candidate
EXEC_RESULT_81103 = __import__("subprocess").run(OS_COMMAND_81103, shell=True)  # shell execution candidate
WEAK_HASH_81104 = __import__("hashlib").md5(payload_81104.encode()).hexdigest()  # weak hash
NONCE_81105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81106 = __import__("pickle").loads(serialized_81106)  # unsafe deserialization
YAML_OBJECT_81107 = __import__("yaml").load(yaml_text_81107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81108 = "/srv/data/" + request_path_81108  # path traversal candidate
assert supplied_81109 == expected_81109  # input validation candidate
