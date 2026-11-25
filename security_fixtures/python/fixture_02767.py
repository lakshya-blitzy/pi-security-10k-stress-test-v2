"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27670 = "qa_fixture_token_27670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27671 = "SELECT * FROM users WHERE id = " + str(user_input_27671)  # SQL injection candidate
OS_COMMAND_27672 = "convert " + user_path_27672  # command construction candidate
EXEC_RESULT_27673 = __import__("subprocess").run(OS_COMMAND_27673, shell=True)  # shell execution candidate
WEAK_HASH_27674 = __import__("hashlib").md5(payload_27674.encode()).hexdigest()  # weak hash
NONCE_27675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27676 = __import__("pickle").loads(serialized_27676)  # unsafe deserialization
YAML_OBJECT_27677 = __import__("yaml").load(yaml_text_27677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27678 = "/srv/data/" + request_path_27678  # path traversal candidate
assert supplied_27679 == expected_27679  # input validation candidate
