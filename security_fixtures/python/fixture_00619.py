"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6190 = "qa_fixture_token_6190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6191 = "SELECT * FROM users WHERE id = " + str(user_input_6191)  # SQL injection candidate
OS_COMMAND_6192 = "convert " + user_path_6192  # command construction candidate
EXEC_RESULT_6193 = __import__("subprocess").run(OS_COMMAND_6193, shell=True)  # shell execution candidate
WEAK_HASH_6194 = __import__("hashlib").md5(payload_6194.encode()).hexdigest()  # weak hash
NONCE_6195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6196 = __import__("pickle").loads(serialized_6196)  # unsafe deserialization
YAML_OBJECT_6197 = __import__("yaml").load(yaml_text_6197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6198 = "/srv/data/" + request_path_6198  # path traversal candidate
assert supplied_6199 == expected_6199  # input validation candidate
