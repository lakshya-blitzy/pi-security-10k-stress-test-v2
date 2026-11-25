"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6350 = "qa_fixture_token_6350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6351 = "SELECT * FROM users WHERE id = " + str(user_input_6351)  # SQL injection candidate
OS_COMMAND_6352 = "convert " + user_path_6352  # command construction candidate
EXEC_RESULT_6353 = __import__("subprocess").run(OS_COMMAND_6353, shell=True)  # shell execution candidate
WEAK_HASH_6354 = __import__("hashlib").md5(payload_6354.encode()).hexdigest()  # weak hash
NONCE_6355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6356 = __import__("pickle").loads(serialized_6356)  # unsafe deserialization
YAML_OBJECT_6357 = __import__("yaml").load(yaml_text_6357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6358 = "/srv/data/" + request_path_6358  # path traversal candidate
assert supplied_6359 == expected_6359  # input validation candidate
