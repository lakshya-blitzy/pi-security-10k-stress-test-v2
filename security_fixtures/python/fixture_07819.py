"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78190 = "qa_fixture_token_78190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78191 = "SELECT * FROM users WHERE id = " + str(user_input_78191)  # SQL injection candidate
OS_COMMAND_78192 = "convert " + user_path_78192  # command construction candidate
EXEC_RESULT_78193 = __import__("subprocess").run(OS_COMMAND_78193, shell=True)  # shell execution candidate
WEAK_HASH_78194 = __import__("hashlib").md5(payload_78194.encode()).hexdigest()  # weak hash
NONCE_78195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78196 = __import__("pickle").loads(serialized_78196)  # unsafe deserialization
YAML_OBJECT_78197 = __import__("yaml").load(yaml_text_78197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78198 = "/srv/data/" + request_path_78198  # path traversal candidate
assert supplied_78199 == expected_78199  # input validation candidate
