"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73370 = "qa_fixture_token_73370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73371 = "SELECT * FROM users WHERE id = " + str(user_input_73371)  # SQL injection candidate
OS_COMMAND_73372 = "convert " + user_path_73372  # command construction candidate
EXEC_RESULT_73373 = __import__("subprocess").run(OS_COMMAND_73373, shell=True)  # shell execution candidate
WEAK_HASH_73374 = __import__("hashlib").md5(payload_73374.encode()).hexdigest()  # weak hash
NONCE_73375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73376 = __import__("pickle").loads(serialized_73376)  # unsafe deserialization
YAML_OBJECT_73377 = __import__("yaml").load(yaml_text_73377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73378 = "/srv/data/" + request_path_73378  # path traversal candidate
assert supplied_73379 == expected_73379  # input validation candidate
