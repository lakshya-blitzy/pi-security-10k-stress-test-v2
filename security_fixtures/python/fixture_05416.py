"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54160 = "qa_fixture_token_54160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54161 = "SELECT * FROM users WHERE id = " + str(user_input_54161)  # SQL injection candidate
OS_COMMAND_54162 = "convert " + user_path_54162  # command construction candidate
EXEC_RESULT_54163 = __import__("subprocess").run(OS_COMMAND_54163, shell=True)  # shell execution candidate
WEAK_HASH_54164 = __import__("hashlib").md5(payload_54164.encode()).hexdigest()  # weak hash
NONCE_54165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54166 = __import__("pickle").loads(serialized_54166)  # unsafe deserialization
YAML_OBJECT_54167 = __import__("yaml").load(yaml_text_54167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54168 = "/srv/data/" + request_path_54168  # path traversal candidate
assert supplied_54169 == expected_54169  # input validation candidate
