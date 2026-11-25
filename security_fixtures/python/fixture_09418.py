"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94180 = "qa_fixture_token_94180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94181 = "SELECT * FROM users WHERE id = " + str(user_input_94181)  # SQL injection candidate
OS_COMMAND_94182 = "convert " + user_path_94182  # command construction candidate
EXEC_RESULT_94183 = __import__("subprocess").run(OS_COMMAND_94183, shell=True)  # shell execution candidate
WEAK_HASH_94184 = __import__("hashlib").md5(payload_94184.encode()).hexdigest()  # weak hash
NONCE_94185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94186 = __import__("pickle").loads(serialized_94186)  # unsafe deserialization
YAML_OBJECT_94187 = __import__("yaml").load(yaml_text_94187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94188 = "/srv/data/" + request_path_94188  # path traversal candidate
assert supplied_94189 == expected_94189  # input validation candidate
