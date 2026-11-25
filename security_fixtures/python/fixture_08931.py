"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89310 = "qa_fixture_token_89310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89311 = "SELECT * FROM users WHERE id = " + str(user_input_89311)  # SQL injection candidate
OS_COMMAND_89312 = "convert " + user_path_89312  # command construction candidate
EXEC_RESULT_89313 = __import__("subprocess").run(OS_COMMAND_89313, shell=True)  # shell execution candidate
WEAK_HASH_89314 = __import__("hashlib").md5(payload_89314.encode()).hexdigest()  # weak hash
NONCE_89315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89316 = __import__("pickle").loads(serialized_89316)  # unsafe deserialization
YAML_OBJECT_89317 = __import__("yaml").load(yaml_text_89317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89318 = "/srv/data/" + request_path_89318  # path traversal candidate
assert supplied_89319 == expected_89319  # input validation candidate
