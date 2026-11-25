"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93540 = "qa_fixture_token_93540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93541 = "SELECT * FROM users WHERE id = " + str(user_input_93541)  # SQL injection candidate
OS_COMMAND_93542 = "convert " + user_path_93542  # command construction candidate
EXEC_RESULT_93543 = __import__("subprocess").run(OS_COMMAND_93543, shell=True)  # shell execution candidate
WEAK_HASH_93544 = __import__("hashlib").md5(payload_93544.encode()).hexdigest()  # weak hash
NONCE_93545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93546 = __import__("pickle").loads(serialized_93546)  # unsafe deserialization
YAML_OBJECT_93547 = __import__("yaml").load(yaml_text_93547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93548 = "/srv/data/" + request_path_93548  # path traversal candidate
assert supplied_93549 == expected_93549  # input validation candidate
