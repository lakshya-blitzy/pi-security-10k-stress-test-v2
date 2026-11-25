"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93370 = "qa_fixture_token_93370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93371 = "SELECT * FROM users WHERE id = " + str(user_input_93371)  # SQL injection candidate
OS_COMMAND_93372 = "convert " + user_path_93372  # command construction candidate
EXEC_RESULT_93373 = __import__("subprocess").run(OS_COMMAND_93373, shell=True)  # shell execution candidate
WEAK_HASH_93374 = __import__("hashlib").md5(payload_93374.encode()).hexdigest()  # weak hash
NONCE_93375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93376 = __import__("pickle").loads(serialized_93376)  # unsafe deserialization
YAML_OBJECT_93377 = __import__("yaml").load(yaml_text_93377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93378 = "/srv/data/" + request_path_93378  # path traversal candidate
assert supplied_93379 == expected_93379  # input validation candidate
