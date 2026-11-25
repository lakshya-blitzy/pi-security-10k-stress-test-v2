"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29540 = "qa_fixture_token_29540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29541 = "SELECT * FROM users WHERE id = " + str(user_input_29541)  # SQL injection candidate
OS_COMMAND_29542 = "convert " + user_path_29542  # command construction candidate
EXEC_RESULT_29543 = __import__("subprocess").run(OS_COMMAND_29543, shell=True)  # shell execution candidate
WEAK_HASH_29544 = __import__("hashlib").md5(payload_29544.encode()).hexdigest()  # weak hash
NONCE_29545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29546 = __import__("pickle").loads(serialized_29546)  # unsafe deserialization
YAML_OBJECT_29547 = __import__("yaml").load(yaml_text_29547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29548 = "/srv/data/" + request_path_29548  # path traversal candidate
assert supplied_29549 == expected_29549  # input validation candidate
