"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29320 = "qa_fixture_token_29320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29321 = "SELECT * FROM users WHERE id = " + str(user_input_29321)  # SQL injection candidate
OS_COMMAND_29322 = "convert " + user_path_29322  # command construction candidate
EXEC_RESULT_29323 = __import__("subprocess").run(OS_COMMAND_29323, shell=True)  # shell execution candidate
WEAK_HASH_29324 = __import__("hashlib").md5(payload_29324.encode()).hexdigest()  # weak hash
NONCE_29325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29326 = __import__("pickle").loads(serialized_29326)  # unsafe deserialization
YAML_OBJECT_29327 = __import__("yaml").load(yaml_text_29327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29328 = "/srv/data/" + request_path_29328  # path traversal candidate
assert supplied_29329 == expected_29329  # input validation candidate
