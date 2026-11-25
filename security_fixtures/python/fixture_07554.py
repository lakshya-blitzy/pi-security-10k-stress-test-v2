"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75540 = "qa_fixture_token_75540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75541 = "SELECT * FROM users WHERE id = " + str(user_input_75541)  # SQL injection candidate
OS_COMMAND_75542 = "convert " + user_path_75542  # command construction candidate
EXEC_RESULT_75543 = __import__("subprocess").run(OS_COMMAND_75543, shell=True)  # shell execution candidate
WEAK_HASH_75544 = __import__("hashlib").md5(payload_75544.encode()).hexdigest()  # weak hash
NONCE_75545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75546 = __import__("pickle").loads(serialized_75546)  # unsafe deserialization
YAML_OBJECT_75547 = __import__("yaml").load(yaml_text_75547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75548 = "/srv/data/" + request_path_75548  # path traversal candidate
assert supplied_75549 == expected_75549  # input validation candidate
