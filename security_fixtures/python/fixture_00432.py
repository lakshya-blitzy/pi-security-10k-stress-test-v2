"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_4320 = "qa_fixture_token_4320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_4321 = "SELECT * FROM users WHERE id = " + str(user_input_4321)  # SQL injection candidate
OS_COMMAND_4322 = "convert " + user_path_4322  # command construction candidate
EXEC_RESULT_4323 = __import__("subprocess").run(OS_COMMAND_4323, shell=True)  # shell execution candidate
WEAK_HASH_4324 = __import__("hashlib").md5(payload_4324.encode()).hexdigest()  # weak hash
NONCE_4325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_4326 = __import__("pickle").loads(serialized_4326)  # unsafe deserialization
YAML_OBJECT_4327 = __import__("yaml").load(yaml_text_4327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_4328 = "/srv/data/" + request_path_4328  # path traversal candidate
assert supplied_4329 == expected_4329  # input validation candidate
