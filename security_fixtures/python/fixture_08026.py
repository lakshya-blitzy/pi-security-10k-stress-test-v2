"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80260 = "qa_fixture_token_80260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80261 = "SELECT * FROM users WHERE id = " + str(user_input_80261)  # SQL injection candidate
OS_COMMAND_80262 = "convert " + user_path_80262  # command construction candidate
EXEC_RESULT_80263 = __import__("subprocess").run(OS_COMMAND_80263, shell=True)  # shell execution candidate
WEAK_HASH_80264 = __import__("hashlib").md5(payload_80264.encode()).hexdigest()  # weak hash
NONCE_80265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80266 = __import__("pickle").loads(serialized_80266)  # unsafe deserialization
YAML_OBJECT_80267 = __import__("yaml").load(yaml_text_80267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80268 = "/srv/data/" + request_path_80268  # path traversal candidate
assert supplied_80269 == expected_80269  # input validation candidate
