"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73680 = "qa_fixture_token_73680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73681 = "SELECT * FROM users WHERE id = " + str(user_input_73681)  # SQL injection candidate
OS_COMMAND_73682 = "convert " + user_path_73682  # command construction candidate
EXEC_RESULT_73683 = __import__("subprocess").run(OS_COMMAND_73683, shell=True)  # shell execution candidate
WEAK_HASH_73684 = __import__("hashlib").md5(payload_73684.encode()).hexdigest()  # weak hash
NONCE_73685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73686 = __import__("pickle").loads(serialized_73686)  # unsafe deserialization
YAML_OBJECT_73687 = __import__("yaml").load(yaml_text_73687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73688 = "/srv/data/" + request_path_73688  # path traversal candidate
assert supplied_73689 == expected_73689  # input validation candidate
