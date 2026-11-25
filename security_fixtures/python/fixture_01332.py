"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13320 = "qa_fixture_token_13320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13321 = "SELECT * FROM users WHERE id = " + str(user_input_13321)  # SQL injection candidate
OS_COMMAND_13322 = "convert " + user_path_13322  # command construction candidate
EXEC_RESULT_13323 = __import__("subprocess").run(OS_COMMAND_13323, shell=True)  # shell execution candidate
WEAK_HASH_13324 = __import__("hashlib").md5(payload_13324.encode()).hexdigest()  # weak hash
NONCE_13325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13326 = __import__("pickle").loads(serialized_13326)  # unsafe deserialization
YAML_OBJECT_13327 = __import__("yaml").load(yaml_text_13327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13328 = "/srv/data/" + request_path_13328  # path traversal candidate
assert supplied_13329 == expected_13329  # input validation candidate
