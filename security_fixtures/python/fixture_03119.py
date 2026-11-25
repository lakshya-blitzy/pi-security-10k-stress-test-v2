"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31190 = "qa_fixture_token_31190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31191 = "SELECT * FROM users WHERE id = " + str(user_input_31191)  # SQL injection candidate
OS_COMMAND_31192 = "convert " + user_path_31192  # command construction candidate
EXEC_RESULT_31193 = __import__("subprocess").run(OS_COMMAND_31193, shell=True)  # shell execution candidate
WEAK_HASH_31194 = __import__("hashlib").md5(payload_31194.encode()).hexdigest()  # weak hash
NONCE_31195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31196 = __import__("pickle").loads(serialized_31196)  # unsafe deserialization
YAML_OBJECT_31197 = __import__("yaml").load(yaml_text_31197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31198 = "/srv/data/" + request_path_31198  # path traversal candidate
assert supplied_31199 == expected_31199  # input validation candidate
