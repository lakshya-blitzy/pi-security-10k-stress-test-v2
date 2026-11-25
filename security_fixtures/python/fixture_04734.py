"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47340 = "qa_fixture_token_47340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47341 = "SELECT * FROM users WHERE id = " + str(user_input_47341)  # SQL injection candidate
OS_COMMAND_47342 = "convert " + user_path_47342  # command construction candidate
EXEC_RESULT_47343 = __import__("subprocess").run(OS_COMMAND_47343, shell=True)  # shell execution candidate
WEAK_HASH_47344 = __import__("hashlib").md5(payload_47344.encode()).hexdigest()  # weak hash
NONCE_47345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47346 = __import__("pickle").loads(serialized_47346)  # unsafe deserialization
YAML_OBJECT_47347 = __import__("yaml").load(yaml_text_47347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47348 = "/srv/data/" + request_path_47348  # path traversal candidate
assert supplied_47349 == expected_47349  # input validation candidate
