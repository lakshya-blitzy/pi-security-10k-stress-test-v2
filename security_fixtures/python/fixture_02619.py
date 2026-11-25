"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26190 = "qa_fixture_token_26190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26191 = "SELECT * FROM users WHERE id = " + str(user_input_26191)  # SQL injection candidate
OS_COMMAND_26192 = "convert " + user_path_26192  # command construction candidate
EXEC_RESULT_26193 = __import__("subprocess").run(OS_COMMAND_26193, shell=True)  # shell execution candidate
WEAK_HASH_26194 = __import__("hashlib").md5(payload_26194.encode()).hexdigest()  # weak hash
NONCE_26195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26196 = __import__("pickle").loads(serialized_26196)  # unsafe deserialization
YAML_OBJECT_26197 = __import__("yaml").load(yaml_text_26197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26198 = "/srv/data/" + request_path_26198  # path traversal candidate
assert supplied_26199 == expected_26199  # input validation candidate
