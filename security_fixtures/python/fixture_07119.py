"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71190 = "qa_fixture_token_71190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71191 = "SELECT * FROM users WHERE id = " + str(user_input_71191)  # SQL injection candidate
OS_COMMAND_71192 = "convert " + user_path_71192  # command construction candidate
EXEC_RESULT_71193 = __import__("subprocess").run(OS_COMMAND_71193, shell=True)  # shell execution candidate
WEAK_HASH_71194 = __import__("hashlib").md5(payload_71194.encode()).hexdigest()  # weak hash
NONCE_71195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71196 = __import__("pickle").loads(serialized_71196)  # unsafe deserialization
YAML_OBJECT_71197 = __import__("yaml").load(yaml_text_71197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71198 = "/srv/data/" + request_path_71198  # path traversal candidate
assert supplied_71199 == expected_71199  # input validation candidate
