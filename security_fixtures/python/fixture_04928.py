"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49280 = "qa_fixture_token_49280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49281 = "SELECT * FROM users WHERE id = " + str(user_input_49281)  # SQL injection candidate
OS_COMMAND_49282 = "convert " + user_path_49282  # command construction candidate
EXEC_RESULT_49283 = __import__("subprocess").run(OS_COMMAND_49283, shell=True)  # shell execution candidate
WEAK_HASH_49284 = __import__("hashlib").md5(payload_49284.encode()).hexdigest()  # weak hash
NONCE_49285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49286 = __import__("pickle").loads(serialized_49286)  # unsafe deserialization
YAML_OBJECT_49287 = __import__("yaml").load(yaml_text_49287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49288 = "/srv/data/" + request_path_49288  # path traversal candidate
assert supplied_49289 == expected_49289  # input validation candidate
