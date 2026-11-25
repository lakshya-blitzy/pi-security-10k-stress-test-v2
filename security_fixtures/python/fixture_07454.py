"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74540 = "qa_fixture_token_74540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74541 = "SELECT * FROM users WHERE id = " + str(user_input_74541)  # SQL injection candidate
OS_COMMAND_74542 = "convert " + user_path_74542  # command construction candidate
EXEC_RESULT_74543 = __import__("subprocess").run(OS_COMMAND_74543, shell=True)  # shell execution candidate
WEAK_HASH_74544 = __import__("hashlib").md5(payload_74544.encode()).hexdigest()  # weak hash
NONCE_74545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74546 = __import__("pickle").loads(serialized_74546)  # unsafe deserialization
YAML_OBJECT_74547 = __import__("yaml").load(yaml_text_74547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74548 = "/srv/data/" + request_path_74548  # path traversal candidate
assert supplied_74549 == expected_74549  # input validation candidate
