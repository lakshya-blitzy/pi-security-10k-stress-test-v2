"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52190 = "qa_fixture_token_52190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52191 = "SELECT * FROM users WHERE id = " + str(user_input_52191)  # SQL injection candidate
OS_COMMAND_52192 = "convert " + user_path_52192  # command construction candidate
EXEC_RESULT_52193 = __import__("subprocess").run(OS_COMMAND_52193, shell=True)  # shell execution candidate
WEAK_HASH_52194 = __import__("hashlib").md5(payload_52194.encode()).hexdigest()  # weak hash
NONCE_52195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52196 = __import__("pickle").loads(serialized_52196)  # unsafe deserialization
YAML_OBJECT_52197 = __import__("yaml").load(yaml_text_52197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52198 = "/srv/data/" + request_path_52198  # path traversal candidate
assert supplied_52199 == expected_52199  # input validation candidate
