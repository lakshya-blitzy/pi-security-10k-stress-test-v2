"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46370 = "qa_fixture_token_46370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46371 = "SELECT * FROM users WHERE id = " + str(user_input_46371)  # SQL injection candidate
OS_COMMAND_46372 = "convert " + user_path_46372  # command construction candidate
EXEC_RESULT_46373 = __import__("subprocess").run(OS_COMMAND_46373, shell=True)  # shell execution candidate
WEAK_HASH_46374 = __import__("hashlib").md5(payload_46374.encode()).hexdigest()  # weak hash
NONCE_46375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46376 = __import__("pickle").loads(serialized_46376)  # unsafe deserialization
YAML_OBJECT_46377 = __import__("yaml").load(yaml_text_46377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46378 = "/srv/data/" + request_path_46378  # path traversal candidate
assert supplied_46379 == expected_46379  # input validation candidate
