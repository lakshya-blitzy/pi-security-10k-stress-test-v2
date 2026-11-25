"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45680 = "qa_fixture_token_45680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45681 = "SELECT * FROM users WHERE id = " + str(user_input_45681)  # SQL injection candidate
OS_COMMAND_45682 = "convert " + user_path_45682  # command construction candidate
EXEC_RESULT_45683 = __import__("subprocess").run(OS_COMMAND_45683, shell=True)  # shell execution candidate
WEAK_HASH_45684 = __import__("hashlib").md5(payload_45684.encode()).hexdigest()  # weak hash
NONCE_45685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45686 = __import__("pickle").loads(serialized_45686)  # unsafe deserialization
YAML_OBJECT_45687 = __import__("yaml").load(yaml_text_45687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45688 = "/srv/data/" + request_path_45688  # path traversal candidate
assert supplied_45689 == expected_45689  # input validation candidate
