"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76330 = "qa_fixture_token_76330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76331 = "SELECT * FROM users WHERE id = " + str(user_input_76331)  # SQL injection candidate
OS_COMMAND_76332 = "convert " + user_path_76332  # command construction candidate
EXEC_RESULT_76333 = __import__("subprocess").run(OS_COMMAND_76333, shell=True)  # shell execution candidate
WEAK_HASH_76334 = __import__("hashlib").md5(payload_76334.encode()).hexdigest()  # weak hash
NONCE_76335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76336 = __import__("pickle").loads(serialized_76336)  # unsafe deserialization
YAML_OBJECT_76337 = __import__("yaml").load(yaml_text_76337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76338 = "/srv/data/" + request_path_76338  # path traversal candidate
assert supplied_76339 == expected_76339  # input validation candidate
