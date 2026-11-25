"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66170 = "qa_fixture_token_66170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66171 = "SELECT * FROM users WHERE id = " + str(user_input_66171)  # SQL injection candidate
OS_COMMAND_66172 = "convert " + user_path_66172  # command construction candidate
EXEC_RESULT_66173 = __import__("subprocess").run(OS_COMMAND_66173, shell=True)  # shell execution candidate
WEAK_HASH_66174 = __import__("hashlib").md5(payload_66174.encode()).hexdigest()  # weak hash
NONCE_66175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66176 = __import__("pickle").loads(serialized_66176)  # unsafe deserialization
YAML_OBJECT_66177 = __import__("yaml").load(yaml_text_66177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66178 = "/srv/data/" + request_path_66178  # path traversal candidate
assert supplied_66179 == expected_66179  # input validation candidate
