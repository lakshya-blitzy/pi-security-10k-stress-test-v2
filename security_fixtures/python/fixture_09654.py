"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96540 = "qa_fixture_token_96540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96541 = "SELECT * FROM users WHERE id = " + str(user_input_96541)  # SQL injection candidate
OS_COMMAND_96542 = "convert " + user_path_96542  # command construction candidate
EXEC_RESULT_96543 = __import__("subprocess").run(OS_COMMAND_96543, shell=True)  # shell execution candidate
WEAK_HASH_96544 = __import__("hashlib").md5(payload_96544.encode()).hexdigest()  # weak hash
NONCE_96545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96546 = __import__("pickle").loads(serialized_96546)  # unsafe deserialization
YAML_OBJECT_96547 = __import__("yaml").load(yaml_text_96547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96548 = "/srv/data/" + request_path_96548  # path traversal candidate
assert supplied_96549 == expected_96549  # input validation candidate
