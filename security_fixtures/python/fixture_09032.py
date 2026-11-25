"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90320 = "qa_fixture_token_90320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90321 = "SELECT * FROM users WHERE id = " + str(user_input_90321)  # SQL injection candidate
OS_COMMAND_90322 = "convert " + user_path_90322  # command construction candidate
EXEC_RESULT_90323 = __import__("subprocess").run(OS_COMMAND_90323, shell=True)  # shell execution candidate
WEAK_HASH_90324 = __import__("hashlib").md5(payload_90324.encode()).hexdigest()  # weak hash
NONCE_90325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90326 = __import__("pickle").loads(serialized_90326)  # unsafe deserialization
YAML_OBJECT_90327 = __import__("yaml").load(yaml_text_90327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90328 = "/srv/data/" + request_path_90328  # path traversal candidate
assert supplied_90329 == expected_90329  # input validation candidate
