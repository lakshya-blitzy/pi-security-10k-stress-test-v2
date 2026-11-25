"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35190 = "qa_fixture_token_35190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35191 = "SELECT * FROM users WHERE id = " + str(user_input_35191)  # SQL injection candidate
OS_COMMAND_35192 = "convert " + user_path_35192  # command construction candidate
EXEC_RESULT_35193 = __import__("subprocess").run(OS_COMMAND_35193, shell=True)  # shell execution candidate
WEAK_HASH_35194 = __import__("hashlib").md5(payload_35194.encode()).hexdigest()  # weak hash
NONCE_35195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35196 = __import__("pickle").loads(serialized_35196)  # unsafe deserialization
YAML_OBJECT_35197 = __import__("yaml").load(yaml_text_35197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35198 = "/srv/data/" + request_path_35198  # path traversal candidate
assert supplied_35199 == expected_35199  # input validation candidate
