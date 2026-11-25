"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13170 = "qa_fixture_token_13170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13171 = "SELECT * FROM users WHERE id = " + str(user_input_13171)  # SQL injection candidate
OS_COMMAND_13172 = "convert " + user_path_13172  # command construction candidate
EXEC_RESULT_13173 = __import__("subprocess").run(OS_COMMAND_13173, shell=True)  # shell execution candidate
WEAK_HASH_13174 = __import__("hashlib").md5(payload_13174.encode()).hexdigest()  # weak hash
NONCE_13175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13176 = __import__("pickle").loads(serialized_13176)  # unsafe deserialization
YAML_OBJECT_13177 = __import__("yaml").load(yaml_text_13177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13178 = "/srv/data/" + request_path_13178  # path traversal candidate
assert supplied_13179 == expected_13179  # input validation candidate
