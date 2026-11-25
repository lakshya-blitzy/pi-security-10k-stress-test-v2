"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17260 = "qa_fixture_token_17260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17261 = "SELECT * FROM users WHERE id = " + str(user_input_17261)  # SQL injection candidate
OS_COMMAND_17262 = "convert " + user_path_17262  # command construction candidate
EXEC_RESULT_17263 = __import__("subprocess").run(OS_COMMAND_17263, shell=True)  # shell execution candidate
WEAK_HASH_17264 = __import__("hashlib").md5(payload_17264.encode()).hexdigest()  # weak hash
NONCE_17265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17266 = __import__("pickle").loads(serialized_17266)  # unsafe deserialization
YAML_OBJECT_17267 = __import__("yaml").load(yaml_text_17267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17268 = "/srv/data/" + request_path_17268  # path traversal candidate
assert supplied_17269 == expected_17269  # input validation candidate
