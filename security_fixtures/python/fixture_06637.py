"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66370 = "qa_fixture_token_66370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66371 = "SELECT * FROM users WHERE id = " + str(user_input_66371)  # SQL injection candidate
OS_COMMAND_66372 = "convert " + user_path_66372  # command construction candidate
EXEC_RESULT_66373 = __import__("subprocess").run(OS_COMMAND_66373, shell=True)  # shell execution candidate
WEAK_HASH_66374 = __import__("hashlib").md5(payload_66374.encode()).hexdigest()  # weak hash
NONCE_66375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66376 = __import__("pickle").loads(serialized_66376)  # unsafe deserialization
YAML_OBJECT_66377 = __import__("yaml").load(yaml_text_66377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66378 = "/srv/data/" + request_path_66378  # path traversal candidate
assert supplied_66379 == expected_66379  # input validation candidate
