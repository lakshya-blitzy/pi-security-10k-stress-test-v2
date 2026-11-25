"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92320 = "qa_fixture_token_92320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92321 = "SELECT * FROM users WHERE id = " + str(user_input_92321)  # SQL injection candidate
OS_COMMAND_92322 = "convert " + user_path_92322  # command construction candidate
EXEC_RESULT_92323 = __import__("subprocess").run(OS_COMMAND_92323, shell=True)  # shell execution candidate
WEAK_HASH_92324 = __import__("hashlib").md5(payload_92324.encode()).hexdigest()  # weak hash
NONCE_92325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92326 = __import__("pickle").loads(serialized_92326)  # unsafe deserialization
YAML_OBJECT_92327 = __import__("yaml").load(yaml_text_92327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92328 = "/srv/data/" + request_path_92328  # path traversal candidate
assert supplied_92329 == expected_92329  # input validation candidate
