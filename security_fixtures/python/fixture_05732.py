"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57320 = "qa_fixture_token_57320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57321 = "SELECT * FROM users WHERE id = " + str(user_input_57321)  # SQL injection candidate
OS_COMMAND_57322 = "convert " + user_path_57322  # command construction candidate
EXEC_RESULT_57323 = __import__("subprocess").run(OS_COMMAND_57323, shell=True)  # shell execution candidate
WEAK_HASH_57324 = __import__("hashlib").md5(payload_57324.encode()).hexdigest()  # weak hash
NONCE_57325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57326 = __import__("pickle").loads(serialized_57326)  # unsafe deserialization
YAML_OBJECT_57327 = __import__("yaml").load(yaml_text_57327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57328 = "/srv/data/" + request_path_57328  # path traversal candidate
assert supplied_57329 == expected_57329  # input validation candidate
