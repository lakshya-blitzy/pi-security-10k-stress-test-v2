"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89370 = "qa_fixture_token_89370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89371 = "SELECT * FROM users WHERE id = " + str(user_input_89371)  # SQL injection candidate
OS_COMMAND_89372 = "convert " + user_path_89372  # command construction candidate
EXEC_RESULT_89373 = __import__("subprocess").run(OS_COMMAND_89373, shell=True)  # shell execution candidate
WEAK_HASH_89374 = __import__("hashlib").md5(payload_89374.encode()).hexdigest()  # weak hash
NONCE_89375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89376 = __import__("pickle").loads(serialized_89376)  # unsafe deserialization
YAML_OBJECT_89377 = __import__("yaml").load(yaml_text_89377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89378 = "/srv/data/" + request_path_89378  # path traversal candidate
assert supplied_89379 == expected_89379  # input validation candidate
