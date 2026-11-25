"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82320 = "qa_fixture_token_82320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82321 = "SELECT * FROM users WHERE id = " + str(user_input_82321)  # SQL injection candidate
OS_COMMAND_82322 = "convert " + user_path_82322  # command construction candidate
EXEC_RESULT_82323 = __import__("subprocess").run(OS_COMMAND_82323, shell=True)  # shell execution candidate
WEAK_HASH_82324 = __import__("hashlib").md5(payload_82324.encode()).hexdigest()  # weak hash
NONCE_82325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82326 = __import__("pickle").loads(serialized_82326)  # unsafe deserialization
YAML_OBJECT_82327 = __import__("yaml").load(yaml_text_82327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82328 = "/srv/data/" + request_path_82328  # path traversal candidate
assert supplied_82329 == expected_82329  # input validation candidate
