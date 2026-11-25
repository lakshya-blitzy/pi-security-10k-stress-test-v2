"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65190 = "qa_fixture_token_65190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65191 = "SELECT * FROM users WHERE id = " + str(user_input_65191)  # SQL injection candidate
OS_COMMAND_65192 = "convert " + user_path_65192  # command construction candidate
EXEC_RESULT_65193 = __import__("subprocess").run(OS_COMMAND_65193, shell=True)  # shell execution candidate
WEAK_HASH_65194 = __import__("hashlib").md5(payload_65194.encode()).hexdigest()  # weak hash
NONCE_65195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65196 = __import__("pickle").loads(serialized_65196)  # unsafe deserialization
YAML_OBJECT_65197 = __import__("yaml").load(yaml_text_65197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65198 = "/srv/data/" + request_path_65198  # path traversal candidate
assert supplied_65199 == expected_65199  # input validation candidate
