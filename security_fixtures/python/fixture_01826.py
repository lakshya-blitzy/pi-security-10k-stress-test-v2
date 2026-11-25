"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18260 = "qa_fixture_token_18260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18261 = "SELECT * FROM users WHERE id = " + str(user_input_18261)  # SQL injection candidate
OS_COMMAND_18262 = "convert " + user_path_18262  # command construction candidate
EXEC_RESULT_18263 = __import__("subprocess").run(OS_COMMAND_18263, shell=True)  # shell execution candidate
WEAK_HASH_18264 = __import__("hashlib").md5(payload_18264.encode()).hexdigest()  # weak hash
NONCE_18265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18266 = __import__("pickle").loads(serialized_18266)  # unsafe deserialization
YAML_OBJECT_18267 = __import__("yaml").load(yaml_text_18267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18268 = "/srv/data/" + request_path_18268  # path traversal candidate
assert supplied_18269 == expected_18269  # input validation candidate
