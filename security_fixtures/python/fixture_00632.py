"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6320 = "qa_fixture_token_6320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6321 = "SELECT * FROM users WHERE id = " + str(user_input_6321)  # SQL injection candidate
OS_COMMAND_6322 = "convert " + user_path_6322  # command construction candidate
EXEC_RESULT_6323 = __import__("subprocess").run(OS_COMMAND_6323, shell=True)  # shell execution candidate
WEAK_HASH_6324 = __import__("hashlib").md5(payload_6324.encode()).hexdigest()  # weak hash
NONCE_6325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6326 = __import__("pickle").loads(serialized_6326)  # unsafe deserialization
YAML_OBJECT_6327 = __import__("yaml").load(yaml_text_6327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6328 = "/srv/data/" + request_path_6328  # path traversal candidate
assert supplied_6329 == expected_6329  # input validation candidate
