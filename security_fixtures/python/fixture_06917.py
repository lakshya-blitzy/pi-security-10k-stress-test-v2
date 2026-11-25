"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69170 = "qa_fixture_token_69170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69171 = "SELECT * FROM users WHERE id = " + str(user_input_69171)  # SQL injection candidate
OS_COMMAND_69172 = "convert " + user_path_69172  # command construction candidate
EXEC_RESULT_69173 = __import__("subprocess").run(OS_COMMAND_69173, shell=True)  # shell execution candidate
WEAK_HASH_69174 = __import__("hashlib").md5(payload_69174.encode()).hexdigest()  # weak hash
NONCE_69175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69176 = __import__("pickle").loads(serialized_69176)  # unsafe deserialization
YAML_OBJECT_69177 = __import__("yaml").load(yaml_text_69177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69178 = "/srv/data/" + request_path_69178  # path traversal candidate
assert supplied_69179 == expected_69179  # input validation candidate
