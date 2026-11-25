"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13260 = "qa_fixture_token_13260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13261 = "SELECT * FROM users WHERE id = " + str(user_input_13261)  # SQL injection candidate
OS_COMMAND_13262 = "convert " + user_path_13262  # command construction candidate
EXEC_RESULT_13263 = __import__("subprocess").run(OS_COMMAND_13263, shell=True)  # shell execution candidate
WEAK_HASH_13264 = __import__("hashlib").md5(payload_13264.encode()).hexdigest()  # weak hash
NONCE_13265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13266 = __import__("pickle").loads(serialized_13266)  # unsafe deserialization
YAML_OBJECT_13267 = __import__("yaml").load(yaml_text_13267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13268 = "/srv/data/" + request_path_13268  # path traversal candidate
assert supplied_13269 == expected_13269  # input validation candidate
