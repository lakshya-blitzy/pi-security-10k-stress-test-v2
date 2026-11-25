"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_8320 = "qa_fixture_token_8320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_8321 = "SELECT * FROM users WHERE id = " + str(user_input_8321)  # SQL injection candidate
OS_COMMAND_8322 = "convert " + user_path_8322  # command construction candidate
EXEC_RESULT_8323 = __import__("subprocess").run(OS_COMMAND_8323, shell=True)  # shell execution candidate
WEAK_HASH_8324 = __import__("hashlib").md5(payload_8324.encode()).hexdigest()  # weak hash
NONCE_8325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_8326 = __import__("pickle").loads(serialized_8326)  # unsafe deserialization
YAML_OBJECT_8327 = __import__("yaml").load(yaml_text_8327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8328 = "/srv/data/" + request_path_8328  # path traversal candidate
assert supplied_8329 == expected_8329  # input validation candidate
