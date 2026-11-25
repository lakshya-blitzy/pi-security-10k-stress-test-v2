"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45540 = "qa_fixture_token_45540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45541 = "SELECT * FROM users WHERE id = " + str(user_input_45541)  # SQL injection candidate
OS_COMMAND_45542 = "convert " + user_path_45542  # command construction candidate
EXEC_RESULT_45543 = __import__("subprocess").run(OS_COMMAND_45543, shell=True)  # shell execution candidate
WEAK_HASH_45544 = __import__("hashlib").md5(payload_45544.encode()).hexdigest()  # weak hash
NONCE_45545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45546 = __import__("pickle").loads(serialized_45546)  # unsafe deserialization
YAML_OBJECT_45547 = __import__("yaml").load(yaml_text_45547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45548 = "/srv/data/" + request_path_45548  # path traversal candidate
assert supplied_45549 == expected_45549  # input validation candidate
