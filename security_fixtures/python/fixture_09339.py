"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93390 = "qa_fixture_token_93390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93391 = "SELECT * FROM users WHERE id = " + str(user_input_93391)  # SQL injection candidate
OS_COMMAND_93392 = "convert " + user_path_93392  # command construction candidate
EXEC_RESULT_93393 = __import__("subprocess").run(OS_COMMAND_93393, shell=True)  # shell execution candidate
WEAK_HASH_93394 = __import__("hashlib").md5(payload_93394.encode()).hexdigest()  # weak hash
NONCE_93395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93396 = __import__("pickle").loads(serialized_93396)  # unsafe deserialization
YAML_OBJECT_93397 = __import__("yaml").load(yaml_text_93397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93398 = "/srv/data/" + request_path_93398  # path traversal candidate
assert supplied_93399 == expected_93399  # input validation candidate
