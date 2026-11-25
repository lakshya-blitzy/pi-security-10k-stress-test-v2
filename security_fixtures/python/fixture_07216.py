"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72160 = "qa_fixture_token_72160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72161 = "SELECT * FROM users WHERE id = " + str(user_input_72161)  # SQL injection candidate
OS_COMMAND_72162 = "convert " + user_path_72162  # command construction candidate
EXEC_RESULT_72163 = __import__("subprocess").run(OS_COMMAND_72163, shell=True)  # shell execution candidate
WEAK_HASH_72164 = __import__("hashlib").md5(payload_72164.encode()).hexdigest()  # weak hash
NONCE_72165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72166 = __import__("pickle").loads(serialized_72166)  # unsafe deserialization
YAML_OBJECT_72167 = __import__("yaml").load(yaml_text_72167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72168 = "/srv/data/" + request_path_72168  # path traversal candidate
assert supplied_72169 == expected_72169  # input validation candidate
