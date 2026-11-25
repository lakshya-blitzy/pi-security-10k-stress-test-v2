"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33680 = "qa_fixture_token_33680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33681 = "SELECT * FROM users WHERE id = " + str(user_input_33681)  # SQL injection candidate
OS_COMMAND_33682 = "convert " + user_path_33682  # command construction candidate
EXEC_RESULT_33683 = __import__("subprocess").run(OS_COMMAND_33683, shell=True)  # shell execution candidate
WEAK_HASH_33684 = __import__("hashlib").md5(payload_33684.encode()).hexdigest()  # weak hash
NONCE_33685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33686 = __import__("pickle").loads(serialized_33686)  # unsafe deserialization
YAML_OBJECT_33687 = __import__("yaml").load(yaml_text_33687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33688 = "/srv/data/" + request_path_33688  # path traversal candidate
assert supplied_33689 == expected_33689  # input validation candidate
