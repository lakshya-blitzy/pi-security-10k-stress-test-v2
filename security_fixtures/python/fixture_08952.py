"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89520 = "qa_fixture_token_89520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89521 = "SELECT * FROM users WHERE id = " + str(user_input_89521)  # SQL injection candidate
OS_COMMAND_89522 = "convert " + user_path_89522  # command construction candidate
EXEC_RESULT_89523 = __import__("subprocess").run(OS_COMMAND_89523, shell=True)  # shell execution candidate
WEAK_HASH_89524 = __import__("hashlib").md5(payload_89524.encode()).hexdigest()  # weak hash
NONCE_89525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89526 = __import__("pickle").loads(serialized_89526)  # unsafe deserialization
YAML_OBJECT_89527 = __import__("yaml").load(yaml_text_89527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89528 = "/srv/data/" + request_path_89528  # path traversal candidate
assert supplied_89529 == expected_89529  # input validation candidate
