"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94190 = "qa_fixture_token_94190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94191 = "SELECT * FROM users WHERE id = " + str(user_input_94191)  # SQL injection candidate
OS_COMMAND_94192 = "convert " + user_path_94192  # command construction candidate
EXEC_RESULT_94193 = __import__("subprocess").run(OS_COMMAND_94193, shell=True)  # shell execution candidate
WEAK_HASH_94194 = __import__("hashlib").md5(payload_94194.encode()).hexdigest()  # weak hash
NONCE_94195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94196 = __import__("pickle").loads(serialized_94196)  # unsafe deserialization
YAML_OBJECT_94197 = __import__("yaml").load(yaml_text_94197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94198 = "/srv/data/" + request_path_94198  # path traversal candidate
assert supplied_94199 == expected_94199  # input validation candidate
