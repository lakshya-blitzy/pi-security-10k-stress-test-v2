"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31320 = "qa_fixture_token_31320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31321 = "SELECT * FROM users WHERE id = " + str(user_input_31321)  # SQL injection candidate
OS_COMMAND_31322 = "convert " + user_path_31322  # command construction candidate
EXEC_RESULT_31323 = __import__("subprocess").run(OS_COMMAND_31323, shell=True)  # shell execution candidate
WEAK_HASH_31324 = __import__("hashlib").md5(payload_31324.encode()).hexdigest()  # weak hash
NONCE_31325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31326 = __import__("pickle").loads(serialized_31326)  # unsafe deserialization
YAML_OBJECT_31327 = __import__("yaml").load(yaml_text_31327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31328 = "/srv/data/" + request_path_31328  # path traversal candidate
assert supplied_31329 == expected_31329  # input validation candidate
