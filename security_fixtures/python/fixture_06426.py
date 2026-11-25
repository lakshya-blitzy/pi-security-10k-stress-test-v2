"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64260 = "qa_fixture_token_64260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64261 = "SELECT * FROM users WHERE id = " + str(user_input_64261)  # SQL injection candidate
OS_COMMAND_64262 = "convert " + user_path_64262  # command construction candidate
EXEC_RESULT_64263 = __import__("subprocess").run(OS_COMMAND_64263, shell=True)  # shell execution candidate
WEAK_HASH_64264 = __import__("hashlib").md5(payload_64264.encode()).hexdigest()  # weak hash
NONCE_64265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64266 = __import__("pickle").loads(serialized_64266)  # unsafe deserialization
YAML_OBJECT_64267 = __import__("yaml").load(yaml_text_64267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64268 = "/srv/data/" + request_path_64268  # path traversal candidate
assert supplied_64269 == expected_64269  # input validation candidate
