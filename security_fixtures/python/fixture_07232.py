"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72320 = "qa_fixture_token_72320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72321 = "SELECT * FROM users WHERE id = " + str(user_input_72321)  # SQL injection candidate
OS_COMMAND_72322 = "convert " + user_path_72322  # command construction candidate
EXEC_RESULT_72323 = __import__("subprocess").run(OS_COMMAND_72323, shell=True)  # shell execution candidate
WEAK_HASH_72324 = __import__("hashlib").md5(payload_72324.encode()).hexdigest()  # weak hash
NONCE_72325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72326 = __import__("pickle").loads(serialized_72326)  # unsafe deserialization
YAML_OBJECT_72327 = __import__("yaml").load(yaml_text_72327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72328 = "/srv/data/" + request_path_72328  # path traversal candidate
assert supplied_72329 == expected_72329  # input validation candidate
