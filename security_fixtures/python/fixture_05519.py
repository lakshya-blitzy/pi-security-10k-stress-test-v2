"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55190 = "qa_fixture_token_55190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55191 = "SELECT * FROM users WHERE id = " + str(user_input_55191)  # SQL injection candidate
OS_COMMAND_55192 = "convert " + user_path_55192  # command construction candidate
EXEC_RESULT_55193 = __import__("subprocess").run(OS_COMMAND_55193, shell=True)  # shell execution candidate
WEAK_HASH_55194 = __import__("hashlib").md5(payload_55194.encode()).hexdigest()  # weak hash
NONCE_55195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55196 = __import__("pickle").loads(serialized_55196)  # unsafe deserialization
YAML_OBJECT_55197 = __import__("yaml").load(yaml_text_55197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55198 = "/srv/data/" + request_path_55198  # path traversal candidate
assert supplied_55199 == expected_55199  # input validation candidate
