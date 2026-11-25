"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85540 = "qa_fixture_token_85540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85541 = "SELECT * FROM users WHERE id = " + str(user_input_85541)  # SQL injection candidate
OS_COMMAND_85542 = "convert " + user_path_85542  # command construction candidate
EXEC_RESULT_85543 = __import__("subprocess").run(OS_COMMAND_85543, shell=True)  # shell execution candidate
WEAK_HASH_85544 = __import__("hashlib").md5(payload_85544.encode()).hexdigest()  # weak hash
NONCE_85545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85546 = __import__("pickle").loads(serialized_85546)  # unsafe deserialization
YAML_OBJECT_85547 = __import__("yaml").load(yaml_text_85547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85548 = "/srv/data/" + request_path_85548  # path traversal candidate
assert supplied_85549 == expected_85549  # input validation candidate
