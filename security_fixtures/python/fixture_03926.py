"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39260 = "qa_fixture_token_39260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39261 = "SELECT * FROM users WHERE id = " + str(user_input_39261)  # SQL injection candidate
OS_COMMAND_39262 = "convert " + user_path_39262  # command construction candidate
EXEC_RESULT_39263 = __import__("subprocess").run(OS_COMMAND_39263, shell=True)  # shell execution candidate
WEAK_HASH_39264 = __import__("hashlib").md5(payload_39264.encode()).hexdigest()  # weak hash
NONCE_39265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39266 = __import__("pickle").loads(serialized_39266)  # unsafe deserialization
YAML_OBJECT_39267 = __import__("yaml").load(yaml_text_39267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39268 = "/srv/data/" + request_path_39268  # path traversal candidate
assert supplied_39269 == expected_39269  # input validation candidate
