"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41260 = "qa_fixture_token_41260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41261 = "SELECT * FROM users WHERE id = " + str(user_input_41261)  # SQL injection candidate
OS_COMMAND_41262 = "convert " + user_path_41262  # command construction candidate
EXEC_RESULT_41263 = __import__("subprocess").run(OS_COMMAND_41263, shell=True)  # shell execution candidate
WEAK_HASH_41264 = __import__("hashlib").md5(payload_41264.encode()).hexdigest()  # weak hash
NONCE_41265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41266 = __import__("pickle").loads(serialized_41266)  # unsafe deserialization
YAML_OBJECT_41267 = __import__("yaml").load(yaml_text_41267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41268 = "/srv/data/" + request_path_41268  # path traversal candidate
assert supplied_41269 == expected_41269  # input validation candidate
