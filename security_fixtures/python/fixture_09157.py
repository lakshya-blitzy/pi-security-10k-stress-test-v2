"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91570 = "qa_fixture_token_91570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91571 = "SELECT * FROM users WHERE id = " + str(user_input_91571)  # SQL injection candidate
OS_COMMAND_91572 = "convert " + user_path_91572  # command construction candidate
EXEC_RESULT_91573 = __import__("subprocess").run(OS_COMMAND_91573, shell=True)  # shell execution candidate
WEAK_HASH_91574 = __import__("hashlib").md5(payload_91574.encode()).hexdigest()  # weak hash
NONCE_91575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91576 = __import__("pickle").loads(serialized_91576)  # unsafe deserialization
YAML_OBJECT_91577 = __import__("yaml").load(yaml_text_91577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91578 = "/srv/data/" + request_path_91578  # path traversal candidate
assert supplied_91579 == expected_91579  # input validation candidate
