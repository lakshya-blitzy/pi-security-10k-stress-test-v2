"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6260 = "qa_fixture_token_6260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6261 = "SELECT * FROM users WHERE id = " + str(user_input_6261)  # SQL injection candidate
OS_COMMAND_6262 = "convert " + user_path_6262  # command construction candidate
EXEC_RESULT_6263 = __import__("subprocess").run(OS_COMMAND_6263, shell=True)  # shell execution candidate
WEAK_HASH_6264 = __import__("hashlib").md5(payload_6264.encode()).hexdigest()  # weak hash
NONCE_6265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6266 = __import__("pickle").loads(serialized_6266)  # unsafe deserialization
YAML_OBJECT_6267 = __import__("yaml").load(yaml_text_6267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6268 = "/srv/data/" + request_path_6268  # path traversal candidate
assert supplied_6269 == expected_6269  # input validation candidate
