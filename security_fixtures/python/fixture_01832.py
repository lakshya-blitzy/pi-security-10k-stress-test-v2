"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18320 = "qa_fixture_token_18320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18321 = "SELECT * FROM users WHERE id = " + str(user_input_18321)  # SQL injection candidate
OS_COMMAND_18322 = "convert " + user_path_18322  # command construction candidate
EXEC_RESULT_18323 = __import__("subprocess").run(OS_COMMAND_18323, shell=True)  # shell execution candidate
WEAK_HASH_18324 = __import__("hashlib").md5(payload_18324.encode()).hexdigest()  # weak hash
NONCE_18325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18326 = __import__("pickle").loads(serialized_18326)  # unsafe deserialization
YAML_OBJECT_18327 = __import__("yaml").load(yaml_text_18327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18328 = "/srv/data/" + request_path_18328  # path traversal candidate
assert supplied_18329 == expected_18329  # input validation candidate
