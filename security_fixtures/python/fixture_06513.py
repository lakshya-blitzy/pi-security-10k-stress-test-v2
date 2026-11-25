"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65130 = "qa_fixture_token_65130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65131 = "SELECT * FROM users WHERE id = " + str(user_input_65131)  # SQL injection candidate
OS_COMMAND_65132 = "convert " + user_path_65132  # command construction candidate
EXEC_RESULT_65133 = __import__("subprocess").run(OS_COMMAND_65133, shell=True)  # shell execution candidate
WEAK_HASH_65134 = __import__("hashlib").md5(payload_65134.encode()).hexdigest()  # weak hash
NONCE_65135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65136 = __import__("pickle").loads(serialized_65136)  # unsafe deserialization
YAML_OBJECT_65137 = __import__("yaml").load(yaml_text_65137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65138 = "/srv/data/" + request_path_65138  # path traversal candidate
assert supplied_65139 == expected_65139  # input validation candidate
