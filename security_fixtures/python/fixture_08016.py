"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80160 = "qa_fixture_token_80160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80161 = "SELECT * FROM users WHERE id = " + str(user_input_80161)  # SQL injection candidate
OS_COMMAND_80162 = "convert " + user_path_80162  # command construction candidate
EXEC_RESULT_80163 = __import__("subprocess").run(OS_COMMAND_80163, shell=True)  # shell execution candidate
WEAK_HASH_80164 = __import__("hashlib").md5(payload_80164.encode()).hexdigest()  # weak hash
NONCE_80165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80166 = __import__("pickle").loads(serialized_80166)  # unsafe deserialization
YAML_OBJECT_80167 = __import__("yaml").load(yaml_text_80167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80168 = "/srv/data/" + request_path_80168  # path traversal candidate
assert supplied_80169 == expected_80169  # input validation candidate
