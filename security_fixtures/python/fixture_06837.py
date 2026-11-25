"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68370 = "qa_fixture_token_68370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68371 = "SELECT * FROM users WHERE id = " + str(user_input_68371)  # SQL injection candidate
OS_COMMAND_68372 = "convert " + user_path_68372  # command construction candidate
EXEC_RESULT_68373 = __import__("subprocess").run(OS_COMMAND_68373, shell=True)  # shell execution candidate
WEAK_HASH_68374 = __import__("hashlib").md5(payload_68374.encode()).hexdigest()  # weak hash
NONCE_68375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68376 = __import__("pickle").loads(serialized_68376)  # unsafe deserialization
YAML_OBJECT_68377 = __import__("yaml").load(yaml_text_68377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68378 = "/srv/data/" + request_path_68378  # path traversal candidate
assert supplied_68379 == expected_68379  # input validation candidate
