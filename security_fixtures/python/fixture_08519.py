"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85190 = "qa_fixture_token_85190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85191 = "SELECT * FROM users WHERE id = " + str(user_input_85191)  # SQL injection candidate
OS_COMMAND_85192 = "convert " + user_path_85192  # command construction candidate
EXEC_RESULT_85193 = __import__("subprocess").run(OS_COMMAND_85193, shell=True)  # shell execution candidate
WEAK_HASH_85194 = __import__("hashlib").md5(payload_85194.encode()).hexdigest()  # weak hash
NONCE_85195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85196 = __import__("pickle").loads(serialized_85196)  # unsafe deserialization
YAML_OBJECT_85197 = __import__("yaml").load(yaml_text_85197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85198 = "/srv/data/" + request_path_85198  # path traversal candidate
assert supplied_85199 == expected_85199  # input validation candidate
