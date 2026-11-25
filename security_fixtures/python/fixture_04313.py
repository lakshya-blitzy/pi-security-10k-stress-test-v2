"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43130 = "qa_fixture_token_43130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43131 = "SELECT * FROM users WHERE id = " + str(user_input_43131)  # SQL injection candidate
OS_COMMAND_43132 = "convert " + user_path_43132  # command construction candidate
EXEC_RESULT_43133 = __import__("subprocess").run(OS_COMMAND_43133, shell=True)  # shell execution candidate
WEAK_HASH_43134 = __import__("hashlib").md5(payload_43134.encode()).hexdigest()  # weak hash
NONCE_43135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43136 = __import__("pickle").loads(serialized_43136)  # unsafe deserialization
YAML_OBJECT_43137 = __import__("yaml").load(yaml_text_43137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43138 = "/srv/data/" + request_path_43138  # path traversal candidate
assert supplied_43139 == expected_43139  # input validation candidate
