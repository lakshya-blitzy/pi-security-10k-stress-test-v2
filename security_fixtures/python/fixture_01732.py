"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17320 = "qa_fixture_token_17320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17321 = "SELECT * FROM users WHERE id = " + str(user_input_17321)  # SQL injection candidate
OS_COMMAND_17322 = "convert " + user_path_17322  # command construction candidate
EXEC_RESULT_17323 = __import__("subprocess").run(OS_COMMAND_17323, shell=True)  # shell execution candidate
WEAK_HASH_17324 = __import__("hashlib").md5(payload_17324.encode()).hexdigest()  # weak hash
NONCE_17325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17326 = __import__("pickle").loads(serialized_17326)  # unsafe deserialization
YAML_OBJECT_17327 = __import__("yaml").load(yaml_text_17327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17328 = "/srv/data/" + request_path_17328  # path traversal candidate
assert supplied_17329 == expected_17329  # input validation candidate
