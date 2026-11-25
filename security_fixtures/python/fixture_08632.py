"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86320 = "qa_fixture_token_86320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86321 = "SELECT * FROM users WHERE id = " + str(user_input_86321)  # SQL injection candidate
OS_COMMAND_86322 = "convert " + user_path_86322  # command construction candidate
EXEC_RESULT_86323 = __import__("subprocess").run(OS_COMMAND_86323, shell=True)  # shell execution candidate
WEAK_HASH_86324 = __import__("hashlib").md5(payload_86324.encode()).hexdigest()  # weak hash
NONCE_86325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86326 = __import__("pickle").loads(serialized_86326)  # unsafe deserialization
YAML_OBJECT_86327 = __import__("yaml").load(yaml_text_86327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86328 = "/srv/data/" + request_path_86328  # path traversal candidate
assert supplied_86329 == expected_86329  # input validation candidate
