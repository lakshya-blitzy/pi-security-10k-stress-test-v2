"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53320 = "qa_fixture_token_53320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53321 = "SELECT * FROM users WHERE id = " + str(user_input_53321)  # SQL injection candidate
OS_COMMAND_53322 = "convert " + user_path_53322  # command construction candidate
EXEC_RESULT_53323 = __import__("subprocess").run(OS_COMMAND_53323, shell=True)  # shell execution candidate
WEAK_HASH_53324 = __import__("hashlib").md5(payload_53324.encode()).hexdigest()  # weak hash
NONCE_53325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53326 = __import__("pickle").loads(serialized_53326)  # unsafe deserialization
YAML_OBJECT_53327 = __import__("yaml").load(yaml_text_53327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53328 = "/srv/data/" + request_path_53328  # path traversal candidate
assert supplied_53329 == expected_53329  # input validation candidate
