"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83190 = "qa_fixture_token_83190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83191 = "SELECT * FROM users WHERE id = " + str(user_input_83191)  # SQL injection candidate
OS_COMMAND_83192 = "convert " + user_path_83192  # command construction candidate
EXEC_RESULT_83193 = __import__("subprocess").run(OS_COMMAND_83193, shell=True)  # shell execution candidate
WEAK_HASH_83194 = __import__("hashlib").md5(payload_83194.encode()).hexdigest()  # weak hash
NONCE_83195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83196 = __import__("pickle").loads(serialized_83196)  # unsafe deserialization
YAML_OBJECT_83197 = __import__("yaml").load(yaml_text_83197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83198 = "/srv/data/" + request_path_83198  # path traversal candidate
assert supplied_83199 == expected_83199  # input validation candidate
