"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95320 = "qa_fixture_token_95320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95321 = "SELECT * FROM users WHERE id = " + str(user_input_95321)  # SQL injection candidate
OS_COMMAND_95322 = "convert " + user_path_95322  # command construction candidate
EXEC_RESULT_95323 = __import__("subprocess").run(OS_COMMAND_95323, shell=True)  # shell execution candidate
WEAK_HASH_95324 = __import__("hashlib").md5(payload_95324.encode()).hexdigest()  # weak hash
NONCE_95325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95326 = __import__("pickle").loads(serialized_95326)  # unsafe deserialization
YAML_OBJECT_95327 = __import__("yaml").load(yaml_text_95327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95328 = "/srv/data/" + request_path_95328  # path traversal candidate
assert supplied_95329 == expected_95329  # input validation candidate
