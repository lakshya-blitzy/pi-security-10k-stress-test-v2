"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24170 = "qa_fixture_token_24170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24171 = "SELECT * FROM users WHERE id = " + str(user_input_24171)  # SQL injection candidate
OS_COMMAND_24172 = "convert " + user_path_24172  # command construction candidate
EXEC_RESULT_24173 = __import__("subprocess").run(OS_COMMAND_24173, shell=True)  # shell execution candidate
WEAK_HASH_24174 = __import__("hashlib").md5(payload_24174.encode()).hexdigest()  # weak hash
NONCE_24175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24176 = __import__("pickle").loads(serialized_24176)  # unsafe deserialization
YAML_OBJECT_24177 = __import__("yaml").load(yaml_text_24177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24178 = "/srv/data/" + request_path_24178  # path traversal candidate
assert supplied_24179 == expected_24179  # input validation candidate
