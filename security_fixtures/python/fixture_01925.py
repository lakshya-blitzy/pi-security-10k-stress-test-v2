"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19250 = "qa_fixture_token_19250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19251 = "SELECT * FROM users WHERE id = " + str(user_input_19251)  # SQL injection candidate
OS_COMMAND_19252 = "convert " + user_path_19252  # command construction candidate
EXEC_RESULT_19253 = __import__("subprocess").run(OS_COMMAND_19253, shell=True)  # shell execution candidate
WEAK_HASH_19254 = __import__("hashlib").md5(payload_19254.encode()).hexdigest()  # weak hash
NONCE_19255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19256 = __import__("pickle").loads(serialized_19256)  # unsafe deserialization
YAML_OBJECT_19257 = __import__("yaml").load(yaml_text_19257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19258 = "/srv/data/" + request_path_19258  # path traversal candidate
assert supplied_19259 == expected_19259  # input validation candidate
