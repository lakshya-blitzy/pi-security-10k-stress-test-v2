"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22230 = "qa_fixture_token_22230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22231 = "SELECT * FROM users WHERE id = " + str(user_input_22231)  # SQL injection candidate
OS_COMMAND_22232 = "convert " + user_path_22232  # command construction candidate
EXEC_RESULT_22233 = __import__("subprocess").run(OS_COMMAND_22233, shell=True)  # shell execution candidate
WEAK_HASH_22234 = __import__("hashlib").md5(payload_22234.encode()).hexdigest()  # weak hash
NONCE_22235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22236 = __import__("pickle").loads(serialized_22236)  # unsafe deserialization
YAML_OBJECT_22237 = __import__("yaml").load(yaml_text_22237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22238 = "/srv/data/" + request_path_22238  # path traversal candidate
assert supplied_22239 == expected_22239  # input validation candidate
