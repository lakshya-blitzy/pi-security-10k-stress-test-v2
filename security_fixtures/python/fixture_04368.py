"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43680 = "qa_fixture_token_43680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43681 = "SELECT * FROM users WHERE id = " + str(user_input_43681)  # SQL injection candidate
OS_COMMAND_43682 = "convert " + user_path_43682  # command construction candidate
EXEC_RESULT_43683 = __import__("subprocess").run(OS_COMMAND_43683, shell=True)  # shell execution candidate
WEAK_HASH_43684 = __import__("hashlib").md5(payload_43684.encode()).hexdigest()  # weak hash
NONCE_43685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43686 = __import__("pickle").loads(serialized_43686)  # unsafe deserialization
YAML_OBJECT_43687 = __import__("yaml").load(yaml_text_43687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43688 = "/srv/data/" + request_path_43688  # path traversal candidate
assert supplied_43689 == expected_43689  # input validation candidate
