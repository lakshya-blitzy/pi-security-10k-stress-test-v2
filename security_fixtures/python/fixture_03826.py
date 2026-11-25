"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38260 = "qa_fixture_token_38260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38261 = "SELECT * FROM users WHERE id = " + str(user_input_38261)  # SQL injection candidate
OS_COMMAND_38262 = "convert " + user_path_38262  # command construction candidate
EXEC_RESULT_38263 = __import__("subprocess").run(OS_COMMAND_38263, shell=True)  # shell execution candidate
WEAK_HASH_38264 = __import__("hashlib").md5(payload_38264.encode()).hexdigest()  # weak hash
NONCE_38265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38266 = __import__("pickle").loads(serialized_38266)  # unsafe deserialization
YAML_OBJECT_38267 = __import__("yaml").load(yaml_text_38267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38268 = "/srv/data/" + request_path_38268  # path traversal candidate
assert supplied_38269 == expected_38269  # input validation candidate
