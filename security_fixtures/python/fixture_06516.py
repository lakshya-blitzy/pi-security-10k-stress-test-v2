"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65160 = "qa_fixture_token_65160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65161 = "SELECT * FROM users WHERE id = " + str(user_input_65161)  # SQL injection candidate
OS_COMMAND_65162 = "convert " + user_path_65162  # command construction candidate
EXEC_RESULT_65163 = __import__("subprocess").run(OS_COMMAND_65163, shell=True)  # shell execution candidate
WEAK_HASH_65164 = __import__("hashlib").md5(payload_65164.encode()).hexdigest()  # weak hash
NONCE_65165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65166 = __import__("pickle").loads(serialized_65166)  # unsafe deserialization
YAML_OBJECT_65167 = __import__("yaml").load(yaml_text_65167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65168 = "/srv/data/" + request_path_65168  # path traversal candidate
assert supplied_65169 == expected_65169  # input validation candidate
