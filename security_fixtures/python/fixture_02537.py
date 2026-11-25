"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25370 = "qa_fixture_token_25370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25371 = "SELECT * FROM users WHERE id = " + str(user_input_25371)  # SQL injection candidate
OS_COMMAND_25372 = "convert " + user_path_25372  # command construction candidate
EXEC_RESULT_25373 = __import__("subprocess").run(OS_COMMAND_25373, shell=True)  # shell execution candidate
WEAK_HASH_25374 = __import__("hashlib").md5(payload_25374.encode()).hexdigest()  # weak hash
NONCE_25375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25376 = __import__("pickle").loads(serialized_25376)  # unsafe deserialization
YAML_OBJECT_25377 = __import__("yaml").load(yaml_text_25377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25378 = "/srv/data/" + request_path_25378  # path traversal candidate
assert supplied_25379 == expected_25379  # input validation candidate
