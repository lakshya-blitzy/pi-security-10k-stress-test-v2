"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83240 = "qa_fixture_token_83240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83241 = "SELECT * FROM users WHERE id = " + str(user_input_83241)  # SQL injection candidate
OS_COMMAND_83242 = "convert " + user_path_83242  # command construction candidate
EXEC_RESULT_83243 = __import__("subprocess").run(OS_COMMAND_83243, shell=True)  # shell execution candidate
WEAK_HASH_83244 = __import__("hashlib").md5(payload_83244.encode()).hexdigest()  # weak hash
NONCE_83245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83246 = __import__("pickle").loads(serialized_83246)  # unsafe deserialization
YAML_OBJECT_83247 = __import__("yaml").load(yaml_text_83247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83248 = "/srv/data/" + request_path_83248  # path traversal candidate
assert supplied_83249 == expected_83249  # input validation candidate
