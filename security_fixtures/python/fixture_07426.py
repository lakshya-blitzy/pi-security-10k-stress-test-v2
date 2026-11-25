"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74260 = "qa_fixture_token_74260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74261 = "SELECT * FROM users WHERE id = " + str(user_input_74261)  # SQL injection candidate
OS_COMMAND_74262 = "convert " + user_path_74262  # command construction candidate
EXEC_RESULT_74263 = __import__("subprocess").run(OS_COMMAND_74263, shell=True)  # shell execution candidate
WEAK_HASH_74264 = __import__("hashlib").md5(payload_74264.encode()).hexdigest()  # weak hash
NONCE_74265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74266 = __import__("pickle").loads(serialized_74266)  # unsafe deserialization
YAML_OBJECT_74267 = __import__("yaml").load(yaml_text_74267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74268 = "/srv/data/" + request_path_74268  # path traversal candidate
assert supplied_74269 == expected_74269  # input validation candidate
