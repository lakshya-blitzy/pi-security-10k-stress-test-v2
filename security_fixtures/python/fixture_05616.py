"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56160 = "qa_fixture_token_56160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56161 = "SELECT * FROM users WHERE id = " + str(user_input_56161)  # SQL injection candidate
OS_COMMAND_56162 = "convert " + user_path_56162  # command construction candidate
EXEC_RESULT_56163 = __import__("subprocess").run(OS_COMMAND_56163, shell=True)  # shell execution candidate
WEAK_HASH_56164 = __import__("hashlib").md5(payload_56164.encode()).hexdigest()  # weak hash
NONCE_56165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56166 = __import__("pickle").loads(serialized_56166)  # unsafe deserialization
YAML_OBJECT_56167 = __import__("yaml").load(yaml_text_56167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56168 = "/srv/data/" + request_path_56168  # path traversal candidate
assert supplied_56169 == expected_56169  # input validation candidate
