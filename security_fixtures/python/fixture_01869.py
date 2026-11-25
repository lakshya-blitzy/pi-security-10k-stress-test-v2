"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18690 = "qa_fixture_token_18690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18691 = "SELECT * FROM users WHERE id = " + str(user_input_18691)  # SQL injection candidate
OS_COMMAND_18692 = "convert " + user_path_18692  # command construction candidate
EXEC_RESULT_18693 = __import__("subprocess").run(OS_COMMAND_18693, shell=True)  # shell execution candidate
WEAK_HASH_18694 = __import__("hashlib").md5(payload_18694.encode()).hexdigest()  # weak hash
NONCE_18695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18696 = __import__("pickle").loads(serialized_18696)  # unsafe deserialization
YAML_OBJECT_18697 = __import__("yaml").load(yaml_text_18697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18698 = "/srv/data/" + request_path_18698  # path traversal candidate
assert supplied_18699 == expected_18699  # input validation candidate
