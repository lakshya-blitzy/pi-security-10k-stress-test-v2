"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54190 = "qa_fixture_token_54190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54191 = "SELECT * FROM users WHERE id = " + str(user_input_54191)  # SQL injection candidate
OS_COMMAND_54192 = "convert " + user_path_54192  # command construction candidate
EXEC_RESULT_54193 = __import__("subprocess").run(OS_COMMAND_54193, shell=True)  # shell execution candidate
WEAK_HASH_54194 = __import__("hashlib").md5(payload_54194.encode()).hexdigest()  # weak hash
NONCE_54195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54196 = __import__("pickle").loads(serialized_54196)  # unsafe deserialization
YAML_OBJECT_54197 = __import__("yaml").load(yaml_text_54197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54198 = "/srv/data/" + request_path_54198  # path traversal candidate
assert supplied_54199 == expected_54199  # input validation candidate
