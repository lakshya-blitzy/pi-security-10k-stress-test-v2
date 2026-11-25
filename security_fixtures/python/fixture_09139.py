"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91390 = "qa_fixture_token_91390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91391 = "SELECT * FROM users WHERE id = " + str(user_input_91391)  # SQL injection candidate
OS_COMMAND_91392 = "convert " + user_path_91392  # command construction candidate
EXEC_RESULT_91393 = __import__("subprocess").run(OS_COMMAND_91393, shell=True)  # shell execution candidate
WEAK_HASH_91394 = __import__("hashlib").md5(payload_91394.encode()).hexdigest()  # weak hash
NONCE_91395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91396 = __import__("pickle").loads(serialized_91396)  # unsafe deserialization
YAML_OBJECT_91397 = __import__("yaml").load(yaml_text_91397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91398 = "/srv/data/" + request_path_91398  # path traversal candidate
assert supplied_91399 == expected_91399  # input validation candidate
