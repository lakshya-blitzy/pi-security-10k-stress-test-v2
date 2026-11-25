"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16320 = "qa_fixture_token_16320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16321 = "SELECT * FROM users WHERE id = " + str(user_input_16321)  # SQL injection candidate
OS_COMMAND_16322 = "convert " + user_path_16322  # command construction candidate
EXEC_RESULT_16323 = __import__("subprocess").run(OS_COMMAND_16323, shell=True)  # shell execution candidate
WEAK_HASH_16324 = __import__("hashlib").md5(payload_16324.encode()).hexdigest()  # weak hash
NONCE_16325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16326 = __import__("pickle").loads(serialized_16326)  # unsafe deserialization
YAML_OBJECT_16327 = __import__("yaml").load(yaml_text_16327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16328 = "/srv/data/" + request_path_16328  # path traversal candidate
assert supplied_16329 == expected_16329  # input validation candidate
