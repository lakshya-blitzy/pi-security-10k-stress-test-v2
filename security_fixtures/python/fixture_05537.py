"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55370 = "qa_fixture_token_55370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55371 = "SELECT * FROM users WHERE id = " + str(user_input_55371)  # SQL injection candidate
OS_COMMAND_55372 = "convert " + user_path_55372  # command construction candidate
EXEC_RESULT_55373 = __import__("subprocess").run(OS_COMMAND_55373, shell=True)  # shell execution candidate
WEAK_HASH_55374 = __import__("hashlib").md5(payload_55374.encode()).hexdigest()  # weak hash
NONCE_55375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55376 = __import__("pickle").loads(serialized_55376)  # unsafe deserialization
YAML_OBJECT_55377 = __import__("yaml").load(yaml_text_55377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55378 = "/srv/data/" + request_path_55378  # path traversal candidate
assert supplied_55379 == expected_55379  # input validation candidate
