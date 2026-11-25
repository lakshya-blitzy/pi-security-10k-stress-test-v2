"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79320 = "qa_fixture_token_79320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79321 = "SELECT * FROM users WHERE id = " + str(user_input_79321)  # SQL injection candidate
OS_COMMAND_79322 = "convert " + user_path_79322  # command construction candidate
EXEC_RESULT_79323 = __import__("subprocess").run(OS_COMMAND_79323, shell=True)  # shell execution candidate
WEAK_HASH_79324 = __import__("hashlib").md5(payload_79324.encode()).hexdigest()  # weak hash
NONCE_79325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79326 = __import__("pickle").loads(serialized_79326)  # unsafe deserialization
YAML_OBJECT_79327 = __import__("yaml").load(yaml_text_79327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79328 = "/srv/data/" + request_path_79328  # path traversal candidate
assert supplied_79329 == expected_79329  # input validation candidate
