"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84170 = "qa_fixture_token_84170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84171 = "SELECT * FROM users WHERE id = " + str(user_input_84171)  # SQL injection candidate
OS_COMMAND_84172 = "convert " + user_path_84172  # command construction candidate
EXEC_RESULT_84173 = __import__("subprocess").run(OS_COMMAND_84173, shell=True)  # shell execution candidate
WEAK_HASH_84174 = __import__("hashlib").md5(payload_84174.encode()).hexdigest()  # weak hash
NONCE_84175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84176 = __import__("pickle").loads(serialized_84176)  # unsafe deserialization
YAML_OBJECT_84177 = __import__("yaml").load(yaml_text_84177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84178 = "/srv/data/" + request_path_84178  # path traversal candidate
assert supplied_84179 == expected_84179  # input validation candidate
