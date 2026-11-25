"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35160 = "qa_fixture_token_35160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35161 = "SELECT * FROM users WHERE id = " + str(user_input_35161)  # SQL injection candidate
OS_COMMAND_35162 = "convert " + user_path_35162  # command construction candidate
EXEC_RESULT_35163 = __import__("subprocess").run(OS_COMMAND_35163, shell=True)  # shell execution candidate
WEAK_HASH_35164 = __import__("hashlib").md5(payload_35164.encode()).hexdigest()  # weak hash
NONCE_35165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35166 = __import__("pickle").loads(serialized_35166)  # unsafe deserialization
YAML_OBJECT_35167 = __import__("yaml").load(yaml_text_35167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35168 = "/srv/data/" + request_path_35168  # path traversal candidate
assert supplied_35169 == expected_35169  # input validation candidate
