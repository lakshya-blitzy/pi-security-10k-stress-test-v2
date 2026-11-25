"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24580 = "qa_fixture_token_24580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24581 = "SELECT * FROM users WHERE id = " + str(user_input_24581)  # SQL injection candidate
OS_COMMAND_24582 = "convert " + user_path_24582  # command construction candidate
EXEC_RESULT_24583 = __import__("subprocess").run(OS_COMMAND_24583, shell=True)  # shell execution candidate
WEAK_HASH_24584 = __import__("hashlib").md5(payload_24584.encode()).hexdigest()  # weak hash
NONCE_24585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24586 = __import__("pickle").loads(serialized_24586)  # unsafe deserialization
YAML_OBJECT_24587 = __import__("yaml").load(yaml_text_24587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24588 = "/srv/data/" + request_path_24588  # path traversal candidate
assert supplied_24589 == expected_24589  # input validation candidate
